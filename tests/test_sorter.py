from src.models import MiniApp
from src.sorter import get_top_apps, sort_by_name, sort_by_score


def test_sort_by_name():
    apps = [
        MiniApp(name="NekoCat Play", category="Game", status="Reviewing"),
        MiniApp(name="Startale App", category="Super App", status="Testing")
    ]

    assert sort_by_name(apps)[0].name == "NekoCat Play"


def test_sort_by_score():
    apps = [
        MiniApp(name="NekoCat Play", category="Game", status="Reviewing", score=7),
        MiniApp(name="Startale App", category="Super App", status="Testing", score=9)
    ]

    assert sort_by_score(apps)[0].name == "Startale App"


def test_get_top_apps():
    apps = [
        MiniApp(name="A", category="Game", status="Watching", score=5),
        MiniApp(name="B", category="Game", status="Watching", score=9)
    ]

    assert len(get_top_apps(apps, limit=1)) == 1
