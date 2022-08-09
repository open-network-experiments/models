from artifacts.onex_model import onex_model as onex

def test_simple_fabric_with_oversubscription():
    config = onex.api().config()

    datastorage1 = config.hosts.add(name="Data Storage 1", address="1.1.1.1")
    compute1 = config.hosts.add(name="Compute 1", address="3.3.3.3")
    compute2 = config.hosts.add(name="Compute 2", address="4.4.4.4")

    config.fabric.clos.spine.count = 1
    config.fabric.clos.pods.add(count=2, pod_profile_name="Pod Profile 1")

    pod_profile = config.fabric.clos.pod_profiles.add(name="Pod Profile 1")
    pod_profile.pod_switch.count = 1
    tor_profile = config.fabric.clos.tor_profiles.add(name="ToR Profile 1")
    tor_profile.tor_to_pod_oversubscription.ratio="2:1"
    pod_profile.tors.add(count=2, tor_profile_name=tor_profile.name)

    datastorage1_link = config.fabric.clos.host_links.add(host_name=datastorage1.name)
    datastorage1_link.tor.pod_index = 1
    datastorage1_link.tor.switch_index = 1
    
    compute1_link = config.fabric.clos.host_links.add(host_name=compute1.name)
    compute1_link.tor.pod_index = 2
    compute1_link.tor.switch_index = 1

    compute2_link = config.fabric.clos.host_links.add(host_name=compute2.name)
    compute2_link.tor.pod_index = 2
    compute2_link.tor.switch_index = 1

    config.serialize()


