from artifacts.datamodel import datamodel as onex

def test_background_traffic():
    config = onex.api().config()

    flow1 = config.chaos.background_traffic.flows.add(name="Flow 1")
    flow1.fabric_entry_point.front_panel_port.front_panel_port = 1
    stateless_flow = flow1.stateless.add(name='UDP DSCP 46')
    stateless_flow.rate = 20
    stateless_flow.rate_unit = 'Gbps'

    flow2 = config.chaos.background_traffic.flows.add(name="Flow 2")
    flow2.fabric_entry_point.switch_reference.spine.switch_index = 1