from artifacts.onex_model import onex_model as onex

def test_autoneg():
    config = onex.api().config()

    # host
    host1 = config.hosts.add(name="Host 1", address="1.1.1.1")
    host2 = config.hosts.add(name="Host 2", address="4.4.4.4")

    # fabric
    config.fabric.clos.spine.count = 1
    config.fabric.clos.pods.add(count=2, pod_profile_name="Pod Profile 1")

    # layer 1 setting profiles
    l1_profile_1 = config.layer1_profiles.add(name='200G Autoneg')
    l1_profile_1.link_speed = onex.L1SettingsProfile.SPEED_200_GBPS
    l1_profile_1.autonegotiation.advertise_fec = True


    l1_profile_2 = config.layer1_profiles.add(name='100G Manual RS FEC')
    l1_profile_2.link_speed = onex.L1SettingsProfile.SPEED_100_GBPS
    l1_profile_2.manual.fec_mode = onex.L1SettingsProfileManual.REED_SOLOMON

    host1.l1_profile_name =l1_profile_1.name
    host2.l1_profile_name =l1_profile_1.name

    # host link
    host1_link = config.fabric.clos.host_links.add(host_name=host1.name)
    host1_link.front_panel_port = 1
    host1_link.host_type = onex.SwitchHostLink.EXTERNAL
    host1_link.spine = 1

    config.serialize()
    