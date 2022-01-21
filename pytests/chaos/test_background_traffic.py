from artifacts.onex_model.onex_model import onex_model

def test_background_traffic():
    api = onex_model.api()
    config = api.config()

    flow1 = config.chaos.background_traffic.flows.add(name="Flow 1")
    flow1.fabric_entry_point.front_panel_port.front_panel_port = 1
    stateless_flow = flow1.stateless.add(name='UDP DSCP 46')
    stateless_flow.packet.src_address = "1.1.1.1"
    stateless_flow.packet.dst_address = "2.2.2.2"
    stateless_flow.packet.src_port = 10000
    stateless_flow.packet.dst_port = 50000
    stateless_flow.packet.size = 1518
    stateless_flow.packet.l4_protocol = 'udp'
    stateless_flow.rate = 20
    stateless_flow.rate_unit = 'Gbps'

    flow2 = config.chaos.background_traffic.flows.add(name="Flow 2")
    flow2.fabric_entry_point.switch_reference.spine.switch_index = 1

    assert config.serialize()