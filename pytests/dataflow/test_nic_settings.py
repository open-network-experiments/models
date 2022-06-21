from typing import NamedTuple
from unicodedata import name
from artifacts.onex_model import onex_model

def test_nic_parameters():
    config = onex_model.api().config()

    host = config.hosts.add(name="Host 1", address="1.1.1.1")
    host_management = config.dataflow.host_management.add(
        host_name=host.name
    )
    host_management.eth_nic.management_address="192.168.0.100"
    host_management.eth_nic.nic_name='eth1'
    host_management.eth_nic.nic_rx_buffer=1024*1024*1024
    host_management.eth_nic.nic_tx_buffer=1024*1024*1024
    host_management.eth_nic.nic_speed=100000
    assert config.serialize()
