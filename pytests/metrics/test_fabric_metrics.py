from artifacts.onex_model import onex_model as onex

def test_port_link_status_request():
    metric_request_1 = onex.MetricsRequest()
    metric_request_1.port_link_status.port_names = ['Pod Switch 1.1 Port 10', 'ToR Switch 1.1 Port 5']
    metric_request_1.port_link_status.labels = ['speed', 'fec_mode']

    metric_request_2 = onex.MetricsRequest()
    metric_request_2.port_link_status.port_names = ['1/0', '32/0']
    metric_request_2.port_link_status.labels = ['speed', 'fec_mode']

    metric_request_1.serialize()
    metric_request_2.serialize()


def test_port_link_status_response():
    metric_response = onex.MetricsResponse()
    metric_response.port_link_status.add(port_name='Pod Switch 1.1 Port 10', front_panel_port='24/2', enabled=True, link_status = 'link_up', speed='speed_100_gbps', fec_mode='RS-FEC')
    metric_response.port_link_status.add(port_name='ToR Switch 1.1 Port 5', front_panel_port='5/0', enabled=True, link_status = 'link_down', speed='speed_100_gbps', fec_mode='RS-FEC')
    metric_response.serialize()