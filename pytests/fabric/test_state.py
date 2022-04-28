from artifacts.onex_model import onex_model as onex

def test_state():
    state = onex.State()
    state.chaos.background_traffic.add(flow_names = ["F1", "F2"], state='started')
    state.chaos.background_traffic.add(flow_names = ["F3"], state='stopped')
    state.chaos.drop_frames.add(config_names = ["10 percent Link 2", "Min drop Link 1"], state = 'stopped')
    state.serialize()