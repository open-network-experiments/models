from artifacts.onex_model import onex_model as onex

def test_port_mirroring():
    config = onex.api().config()
    mirror = config.insights.port_mirroring.add(name="Ingress frames port")
    mirror.mirror_type = onex.InsightsPortMirroring.INGRESS_FRAMES
    mirror.source_port = "Spine Switch 1 Port 1"
    mirror.destination_port = 10

    config.serialize()