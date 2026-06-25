from src.models import MiniApp
from src.recommendations import build_action_list, recommend_next_action


def test_testing_recommendation():
    app = MiniApp(name="Startale App", category="Super App", status="Testing")

    assert recommend_next_action(app) == "Continue testing product flow"


def test_build_action_list():
    apps = [
        MiniApp(name="NekoCat Play", category="Game", status="Reviewing")
    ]

    assert len(build_action_list(apps)) == 1
