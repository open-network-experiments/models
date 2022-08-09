from artifacts.onex_model import onex_model as onex


def test_qos_ingress_admission():
    config = onex.api().config()

    # Objective: Dedicate 1MB to each port in the pod switch

    # 1. create a qos profile with the respective buffer settings
    qos_profile = config.fabric.qos_profiles.add(name='restricted ingress admission')
    qos_profile.ingress_admission.shared_buffer_bytes = 0
    qos_profile.ingress_admission.reserved_buffer_bytes = 1 * 1024 * 1024
    qos_profile.ingress_admission.priority_list = [1,2]

    # 2. create a topology with a single pod (and 1 switch in the pod),
    #    assign the qos profile to it
    pod_profile = config.fabric.clos.pod_profiles.add(name="Pod Profile 1")
    config.fabric.clos.pods.add(count=1, pod_profile_name=pod_profile.name)
    pod_profile.pod_switch.count = 1
    pod_profile.pod_switch.qos_profile_name = qos_profile.name
    tor_profile = config.fabric.clos.tor_profiles.add("ToR Profile 1")
    pod_profile.tors.add(count = 2, tor_profile_name=tor_profile.name)
    tor_profile.qos_profile_name = qos_profile.name

    assert config.serialize()

def test_qos_scheduling_discipline():
    config = onex.api().config()

    qos_profile = config.fabric.qos_profiles.add(name='restricted ingress admission')

    # qos_profile.packet_classification.map_dscp_to_traffic_class = {
    #     "10": "1",
    #     "20": "2"
    # }

    qos_profile.scheduler.scheduler_mode = qos_profile.scheduler.WEIGHTED_ROUND_ROBIN
    qos_profile.scheduler.weight_list = [1, 2, 4]
    assert config.serialize()

def test_qos_wred():
    config = onex.api().config()

    qos_profile = config.fabric.qos_profiles.add(name="wred with ecn enabled")
    qos_profile.wred.ecn_marking_enabled = True
    qos_profile.wred.min_threshold_bytes = 10
    qos_profile.wred.max_threshold_bytes = 20
    qos_profile.wred.max_probability_percent = 60
    qos_profile.wred.queue_list = [1,2]
    assert config.serialize()

def test_qos_pfc():
    config = onex.api().config()
    qos_profile = config.fabric.qos_profiles.add(name="pfc")
    qos_profile.pfc.priority_list = [1,2]
    qos_profile.pfc.headroom_buffer_bytes = 5000
    qos_profile.pfc.resume_threshold_bytes = 3000
    assert config.serialize()


def test_qos_packet_classification():
    config = onex.api().config()
    qos_profile = config.fabric.qos_profiles.add(name="packet classification")
    qos_profile.packet_classification.map_dscp_to_traffic_class.add(dscp=10, traffic_class=1)
    qos_profile.packet_classification.map_dscp_to_traffic_class.add(dscp=24, traffic_class=2)
    qos_profile.packet_classification.map_traffic_class_to_queue.add(traffic_class=1, queue=1)
    qos_profile.packet_classification.map_traffic_class_to_queue.add(traffic_class=2, queue=7)
    assert config.serialize()