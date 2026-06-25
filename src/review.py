from src.models import MiniApp


def get_score_label(app: MiniApp) -> str:
    if app.score >= 9:
        return "Excellent"

    if app.score >= 7:
        return "Good"

    if app.score >= 5:
        return "Needs review"

    return "Early review"


def build_review_line(app: MiniApp) -> str:
    label = get_score_label(app)
    return f"{app.name}: {label} ({app.score}/10)"
