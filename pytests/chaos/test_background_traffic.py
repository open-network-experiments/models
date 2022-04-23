from artifacts.onex_model.onex_model import onex_model

def test_background_traffic():
    api = onex_model.api()
    config = api.config()

    flow1 = config.chaos.background_traffic.flows.add(name="Flow 1")
    flow1.injection_port = "Spine Switch 1 Port 1"
    flow1.stateless.packet.src_address = "1.1.1.1"
    flow1.stateless.packet.dst_address = "2.2.2.2"
    flow1.stateless.packet.src_port = 10000
    flow1.stateless.packet.dst_port = 50000
    flow1.stateless.packet.size = 1518
    flow1.stateless.packet.l4_protocol = 'udp'
    flow1.stateless.packet.ds_field.dscp = 10
    flow1.stateless.rate = 20
    flow1.stateless.transmission_mode = 'continuous'
    
    flow2 = config.chaos.background_traffic.flows.add(name="Flow 2")
    flow2.injection_port = "Spine Switch 1 Port 1"
    flow2.stateless.packet.src_address = "1.1.1.12"
    flow2.stateless.packet.dst_address = "20.2.2.2"
    flow2.stateless.packet.src_port = 10000
    flow2.stateless.packet.dst_port = 50000
    flow2.stateless.packet.size = 1518
    flow2.stateless.packet.l4_protocol = 'tcp'
    flow2.stateless.packet.ds_field.ecn = 2
    flow2.stateless.rate = 10
    flow2.stateless.transmission_mode = 'burst'
    flow2.stateless.burst.transmit_duration = 1000
    flow2.stateless.burst.transmit_gap = 100

    assert config.serialize()