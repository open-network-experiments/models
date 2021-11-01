from artifacts.fabric import fabric as onex

def test_simple_fabric_with_oversubscription():
    api = onex.api()
    config = api.config()

    config.fabric.choice = config.fabric.SPINE_POD_RACK
    config.fabric.spine_pod_rack.spines.add(count=1)
    config.fabric.spine_pod_rack.pods.add(count=2, pod_profile_name=["Pod Profile 1"])

    pod_profile = config.fabric.spine_pod_rack.pod_profiles.add(name="Pod Profile 1")
    pod_profile.pod_switch.count = 1

    pod_profile.rack.rack_profile_names = ["Rack Profile 1"]

    config.fabric.spine_pod_rack.rack_profiles.add(
        name="Rack Profile 1",
        tor_to_pod_oversubscription="2:1"
    )

    storage_host = config.hosts.add(name="Data Storage 1", address="1.1.1.1")
    compute1 = config.hosts.add(name="Compute 1", address="3.3.3.3")
    compute2 = config.hosts.add(name="Compute 2", address="4.4.4.4")

    print(config.serialize())
