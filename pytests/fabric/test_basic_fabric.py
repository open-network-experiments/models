from artifacts.fabric import fabric as onex

def test_simple_fabric_with_oversubscription():
    config = onex.api().config()
    config.fabric.spine_pod_rack.spines.add(count=1)
    config.fabric.spine_pod_rack.pods.add(count=2, pod_profile_name=["Pod Profile 1"])

    pod_profile = config.fabric.spine_pod_rack.pod_profiles.add(name="Pod Profile 1")
    pod_profile.pod_switch.count = 1
    rack_profile = config.fabric.spine_pod_rack.rack_profiles.add(
        name="Rack Profile 1",
        tor_to_pod_oversubscription="2:1"
    )
    pod_profile.rack.rack_profile_names = [ rack_profile.name ]
    pod_profile.rack.count = 2

    config.hosts.add(name="Data Storage 1", address="1.1.1.1")
    config.hosts.add(name="Compute 1", address="3.3.3.3")
    config.hosts.add(name="Compute 2", address="4.4.4.4")

def test_qos_ingress_admission():
    config = onex.api().config()

    # Objective: Dedicate 1MB to each port in the pod switch

    # 1. create a qos profile with the respective buffer settings
    qos_profile = config.fabric.qos_profiles.add(name='restricted ingress admission')
    qos_profile.ingress_admission.shared_buffer_bytes = 0
    qos_profile.ingress_admission.reserved_buffer_bytes = 1 * 1024 * 1024

    # 2. create a topology with a single pod (and 1 switch in the pod),
    #    assign the qos profile to it
    pod_profile = config.fabric.spine_pod_rack.pod_profiles.add(name="Pod Profile 1")
    config.fabric.spine_pod_rack.pods.add(count=1, pod_profile_name=[pod_profile.name])
    pod_profile.pod_switch.count = 1
    pod_profile.pod_switch.qos_profile_name = qos_profile.name
    pod_profile.rack.count = 2
    rack_profile = config.fabric.spine_pod_rack.rack_profiles.add("Rack Profile 1")
    pod_profile.rack.rack_profile_names = [ rack_profile.name ]
    rack_profile.tor_qos_profile_name = qos_profile.name

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

    config.fabric.spine_pod_rack.pods.add(count=1, pod_profile_name=["Pod Profile 1"])
    pod_profile = config.fabric.spine_pod_rack.pod_profiles.add(name="Pod Profile 1")
    pod_profile.pod_switch.count = 1
    pod_profile.pod_switch.qos_profile_name = qos_profile.name

    assert config.serialize()
