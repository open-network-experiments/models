from typing import NamedTuple
from unicodedata import name
from artifacts.onex_model import onex_model

def test_nic_parameters():
    config = onex_model.api().config()

    host = config.hosts.add(name="Host 1", address="1.1.1.1")
    config.dataflow.host_management.add(
        host_name=host.name,
        management_address="192.168.0.100",
        nic_name='eth1',
        nic_rx_buffer=1024*1024*1024,
        nic_tx_buffer=1024*1024*1024,
        nic_speed=100000
    )
    assert config.serialize()
