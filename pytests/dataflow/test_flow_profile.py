from typing import NamedTuple
from artifacts.onex_model.onex_model import onex_model

def test_flow_profile_network_tcpip_parameters():
    config = onex_model.api().config()
    fp = config.dataflow.flow_profiles.add(name='Test F Profile', data_size=1)

    ip = fp.tcpip.ip
    ip.dscp = 123

    tcp = fp.tcpip.tcp
    tcp.mss = 1500
    tcp.initcwnd = 100
    tcp.receive_buf = 40000
    tcp.send_buf = 50000
    tcp.delayed_ack = True
    tcp.selective_ack = True
    tcp.min_rto = 100
    tcp.ecn = True
    tcp.congestion_algorithm = tcp.DCTCP
    tcp.enable_timestamp = True

    tcp.source_port.single_value.value = 2000
    tcp.destination_port.single_value.value = 3000

    assert config.serialize()


def test_flow_profile_network_roce_parameters():
    config = onex_model.api().config()
    fp = config.dataflow.flow_profiles.add(name='Test F Profile', data_size=1)

    roce = fp.rdma.rocev2
    roce.verb = "read"

    assert config.serialize()
