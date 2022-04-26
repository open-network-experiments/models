from artifacts.onex_model import onex_model as onex

def test_state_request():
    state_request = onex.StateRequest()

    state_request.chaos.background_traffic.flow_names = ["F1", "F2"]
    state_request.chaos.background_traffic.state = 'started'

    state_request.chaos.drop_frames.config_names = ["10 percent Link 2", "Min drop Link 1"]
    state_request.chaos.drop_frames.state = 'stopped'

    state_request.serialize()


def test_state_response():
    state_response = onex.StateResponse()

    state_response.chaos.background_traffic.started = ["F1", "F2"]
    state_response.chaos.background_traffic.stopped = ["F3"]

    state_response.chaos.drop_frames.stopped = ["10 percent Link 2", "Min drop Link 1"]
    
    state_response.serialize()