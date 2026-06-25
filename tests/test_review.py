from src.models import MiniApp
from src.review import build_review_line, get_score_label


def test_score_label_excellent():
    app = MiniApp(name="Startale App", category="Super App", status="Testing", score=9)

    assert get_score_label(app) == "Excellent"


def test_score_label_good():
    app = MiniApp(name="Pocket Knights", category="Game", status="Watching", score=8)

    assert get_score_label(app) == "Good"


def test_review_line():
    app = MiniApp(name="NekoCat Play", category="Game", status="Reviewing", score=7)

    assert "NekoCat Play" in build_review_line(app)
