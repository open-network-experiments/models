from typing import NamedTuple
from artifacts.datamodel import datamodel as onex

def test_simple_dataflow():
    config = onex.api().config()

    aggregator = config.hosts.add(name="Aggregator", address="1.1.1.1")    
    compute1 = config.hosts.add(name="Compute 1", address="3.3.3.3")
    compute2 = config.hosts.add(name="Compute 2", address="4.4.4.4")
    data_transfer = config.dataflow.flow_profiles.add(name='data transfer', data_size=1 * 1024 * 1024 * 1024)
    
    scatter = config.dataflow.workload.add(name="Scatter").scatter
    scatter.sources = [ aggregator.name ]
    scatter.destinations = [ compute1.name, compute2.name ]
    scatter.flow_profile_name = data_transfer.name

    gather = config.dataflow.workload.add(name="Gather").gather
    gather.sources = [ compute1.name, compute2.name ]
    gather.destinations = [ aggregator.name ]
    gather.flow_profile_name = data_transfer.name    

    config.dataflow.host_management.add(host_name=aggregator.name, management_address="10.36.12.32")
    config.dataflow.host_management.add(host_name=compute1.name, management_address="10.36.12.33")
    config.dataflow.host_management.add(host_name=compute2.name, management_address="10.36.12.34")

    assert config.serialize()

def test_ml_training():
    config = onex.api().config()

    storage_host = config.hosts.add(name="Data Storage 1", address="1.1.1.1")
    compute1 = config.hosts.add(name="Compute 1", address="3.3.3.3")
    compute2 = config.hosts.add(name="Compute 2", address="4.4.4.4")

    hyperparameters = config.dataflow.flow_profiles.add(name='hyperparameters', data_size=10000)
    image_data = config.dataflow.flow_profiles.add(name='image data', data_size=10000000)
    gradients_exchange = config.dataflow.flow_profiles.add(name='receive and update gradients', data_size=1000000)
    
    init_scatter = config.dataflow.workload.add(name="transfer hyperparameters").scatter
    init_scatter.sources = [ storage_host.name ]
    init_scatter.destinations = [ compute1.name, compute2.name ]
    init_scatter.flow_profile_name = hyperparameters.name

    epoch_loop = config.dataflow.workload.add(name="Epoch loop").loop
    epoch_loop.iterations = 10

    batch_scatter = epoch_loop.children.add(name='Transfer images').scatter
    batch_scatter.sources = [ storage_host.name ]
    batch_scatter.destinations = [ compute1.name, compute2.name ]
    batch_scatter.flow_profile_name = image_data.name

    batch_compute = epoch_loop.children.add(name='Calculate gradients').compute
    batch_compute.nodes = [ compute1.name, compute2.name ]
    batch_compute.simulated.duration = 10

    batch_all_reduce = epoch_loop.children.add(name='Exchange gradients').all_reduce
    batch_all_reduce.nodes = [ compute1.name, compute2.name ]
    batch_all_reduce.flow_profile_name = gradients_exchange.name
    batch_all_reduce.type = batch_all_reduce.RING

    back_compute_optimizer = epoch_loop.children.add(name='Compute optimizer function + update model').compute
    back_compute_optimizer.nodes = [ compute1.name, compute2.name ]
    back_compute_optimizer.simulated.duration = 10
    
    assert config.serialize()

def test_dataflow_flowprofile():
    config = onex.api().config()

    flow_profile = config.dataflow.flow_profiles.add(name='hyperparameters', data_size=10000)

    flow_profile.ethernet.mtu = 1000

    flow_profile.tcp.congestionAlgorithm = flow_profile.tcp.CUBIC
    flow_profile.tcp.initcwnd = 10
    flow_profile.tcp.sendBuf = 4 * 1024 * 1024
    flow_profile.tcp.sourcePort.range.start_value = 1024
    flow_profile.tcp.sourcePort.range.increment = 1
    flow_profile.tcp.destinationPort.single_value.value = 50051

    flow_profile.data_size = 1 * 1024 * 1024 * 1024

    assert config.serialize()