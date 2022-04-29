from artifacts.onex_model import onex_model as onex

def test_port_metrics_request():
    metric_request_1 = onex.MetricsRequest()
    metric_request_1.port_metrics.port_names = ['Pod Switch 1.1 Port 10', 'ToR Switch 1.1 Port 5']

    metric_request_2 = onex.MetricsRequest()
    metric_request_2.port_metrics.front_panel_ports = ['1/0', '32/0']
    metric_request_2.port_metrics.select_metrics = ['frames_transmitted_broadcast', 'frames_received_broadcast']

    metric_request_1.serialize()
    metric_request_2.serialize()


def test_port_metrics_response():
    metric_response = onex.MetricsResponse()
    port_metric_response1 = metric_response.port_metrics.add(port_name='ToR Switch 1.1 Port 10')
    port_metric_response1.metrics.link_status = 'link_up'
    port_metric_response1.metrics.frames_transmitted_broadcast = 100
    port_metric_response1.metrics.frames_received_broadcast = 100


    port_metric_response2 = metric_response.port_metrics.add(port_name='ToR Switch 1.1 Port 1')
    port_metric_response2.metrics.link_status = 'link_down'
    port_metric_response2.metrics.frames_transmitted_broadcast = 100
    port_metric_response2.metrics.frames_received_broadcast = 100
    port_metric_response2.config.front_panel_port = '1/0'
    port_metric_response2.config.connected_to = 'Host 1'
    port_metric_response2.config.link_name = 'Link T.1.1/1'
    port_metric_response2.config.tx_switch = 'ToR Switch 1.1'
    port_metric_response2.config.rx_switch = 'ToR Switch 1.1'
    port_metric_response2.config.speed = 'speed_100_gbps'
    port_metric_response2.config.fec_mode = 'rs_fec'
    port_metric_response2.config.autoneg_mode = 'disabled'
    print(metric_response.serialize())