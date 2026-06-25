from src.models import MiniApp
from src.tracker import MiniAppTracker


def test_add_miniapp():
    tracker = MiniAppTracker()
    tracker.add_app(MiniApp(name="Startale App", category="Super App", status="Testing"))

    assert tracker.count_apps() == 1


def test_search_miniapp():
    tracker = MiniAppTracker()
    tracker.add_app(MiniApp(name="NekoCat Play", category="Game", status="Reviewing"))

    assert len(tracker.search("NekoCat")) == 1
