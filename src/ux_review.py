from src.models import MiniApp


def onboarding_score(app: MiniApp) -> str:
    if app.score >= 9:
        return "Very clear onboarding"

    if app.score >= 7:
        return "Good onboarding"

    if app.score >= 5:
        return "Needs onboarding review"

    return "Early onboarding review"


def build_ux_note(app: MiniApp) -> str:
    return f"{app.name}: {onboarding_score(app)}"
