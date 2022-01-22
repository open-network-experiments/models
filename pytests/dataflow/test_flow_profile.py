from typing import NamedTuple
from artifacts.onex_model.onex_model import onex_model

def test_flow_profile_tcp():
    config = onex_model.api().config()
    fp = config.dataflow.flow_profiles.add(name='Test F Profile', data_size=1)
    tcp = fp.tcp
    tcp.initcwnd = 100
    tcp.congestion_algorithm = tcp.BBR
    tcp.receive_buf = 40000
    tcp.send_buf = 50000
    tcp.source_port.single_value.value = 2000
    tcp.destination_port.single_value.value = 3000

    assert config.serialize()
