from artifacts.onex_model import onex_model as onex

def test_port_metrics_request():
    metric_request_1 = onex.MetricsRequest()
    metric_request_1.port_metrics.port_names = ['Pod Switch 1.1 Port 10', 'ToR Switch 1.1 Port 5']

    metric_request_2 = onex.MetricsRequest()
    metric_request_2.port_metrics.front_panel_ports = [1, 32]
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
    port_metric_response2.config.front_panel_port = 1
    port_metric_response2.config.connected_to = 'Host 1'
    port_metric_response2.config.link_name = 'Link T.1.1/1'
    port_metric_response2.config.tx_switch = 'ToR Switch 1.1'
    port_metric_response2.config.rx_switch = 'ToR Switch 1.1'
    port_metric_response2.config.speed = 'speed_100_gbps'
    port_metric_response2.config.fec_mode = 'rs_fec'
    port_metric_response2.config.autoneg_mode = 'disabled'
    metric_response.serialize()

def test_flow_counters_port_metrics():
    metric_request = onex.MetricsRequest()
    metric_request.port_metrics.port_names = []
    metric_request.port_metrics.select_metrics = ['flow_counter_metrics']
    metric_request.serialize()

    metric_response = onex.MetricsResponse()
    port_metric_response = metric_response.port_metrics.add(port_name='ToR Switch 1.1 Port 10')
    port_metric_response.metrics.flow_counter_metrics.per_background_traffic_flow.add(flow_name="Flow 1", frames_transmitted=100)
    port_metric_response.metrics.flow_counter_metrics.per_background_traffic_flow.add(flow_name="Flow 2", frames_transmitted=200)
    print(metric_response.serialize())



def test_per_priority_group_port_metrics():
    metric_request = onex.MetricsRequest()
    metric_request.port_metrics.port_names = ['ToR Switch 1.1 Port 10']
    metric_request.port_metrics.select_metrics = ['per_priority_group_metrics']
    metric_request.serialize()

    metric_response = onex.MetricsResponse()
    port_metric_response = metric_response.port_metrics.add(port_name='ToR Switch 1.1 Port 10')
    port_metric_response.metrics.per_priority_group_metrics.add(priority_group=0, ingress_buffer_reserved_usage_current=100, ingress_buffer_shared_usage_peak=200)
    port_metric_response.metrics.per_priority_group_metrics.add(priority_group=3, ingress_buffer_reserved_usage_current=0)
    metric_response.serialize()


def test_per_egress_queue_metrics():
    metric_request = onex.MetricsRequest()
    metric_request.port_metrics.port_names = ['ToR Switch 1.1 Port 10']
    metric_request.port_metrics.select_metrics = ['per_egress_queue_metrics']
    metric_request.serialize()

    metric_response = onex.MetricsResponse()
    port_metric_response = metric_response.port_metrics.add(port_name='ToR Switch 1.1 Port 10')
    port_metric_response.metrics.per_egress_queue_metrics.add(queue_number=0, egress_buffer_reserved_usage_current=0)
    port_metric_response.metrics.per_egress_queue_metrics.add(queue_number=3, egress_buffer_reserved_usage_current=0, egress_buffer_total_usage_peak=100,multicast_buffer_total_usage_peak=0)
    metric_response.serialize()