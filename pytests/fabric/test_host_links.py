from os import link
from artifacts.onex_model import onex_model as onex
from artifacts.onex_model.onex_model.onex_model import FabricL1SettingsProfile, FabricL1SettingsProfileAutonegotiation, FabricL1SettingsProfileAutonegotiationDisabled, SwitchHostLink

def test_autoneg():
    config = onex.api().config()

    # host
    host1 = config.hosts.add(name="Host 1", address="1.1.1.1")
    host2 = config.hosts.add(name="Host 2", address="4.4.4.4")

    # fabric
    config.fabric.clos.spine.count = 1
    config.fabric.clos.pods.add(count=2, pod_profile_name="Pod Profile 1")

    # layer 1 setting profiles
    l1_profile_1 = config.fabric.layer1_profiles.add(name='200G Autoneg')
    l1_profile_1.link_speed = FabricL1SettingsProfile.SPEED_200_GBPS
    l1_profile_1.autonegotiation.choice = FabricL1SettingsProfileAutonegotiation.ENABLED
    l1_profile_1.autonegotiation.enabled.advertise_fec = True


    l1_profile_2 = config.fabric.layer1_profiles.add(name='100G Manual RS FEC')
    l1_profile_2.link_speed = FabricL1SettingsProfile.SPEED_100_GBPS
    l1_profile_2.autonegotiation.choice = FabricL1SettingsProfileAutonegotiation.DISABLED
    l1_profile_2.autonegotiation.disabled.fec_mode = FabricL1SettingsProfileAutonegotiationDisabled.REED_SOLOMON

    # host link
    host1_link = config.fabric.clos.host_links.add(host_name=host1.name)
    host1_link.front_panel_port = 1
    host1_link.host_type = SwitchHostLink.EXTERNAL
    host1_link.l1_profile_name =l1_profile_1.name

    print(config.serialize())
    