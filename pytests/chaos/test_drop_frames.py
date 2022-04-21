from artifacts.onex_model.onex_model import onex_model

def test_background_traffic():
    api = onex_model.api()
    config = api.config()
    drop_frames_cfg1 = config.chaos.drop_frames.add(name="10 percent drop", link="Link S.1/1")
    drop_frames_cfg1.percentage = 10.5

    drop_frames_cfg1 = config.chaos.drop_frames.add(name="Min possible drop", link="Link P.2.1/1")
    drop_frames_cfg1.mode = onex_model.ChaosDropFrames.MIN_TIME

    config.serialize()