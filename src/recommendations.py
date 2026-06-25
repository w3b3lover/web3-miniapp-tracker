from src.models import MiniApp


def recommend_next_action(app: MiniApp) -> str:
    if app.status == "Testing":
        return "Continue testing product flow"

    if app.status == "Reviewing":
        return "Write detailed review notes"

    if app.status == "Watching":
        return "Monitor future updates"

    if app.status == "Researching":
        return "Collect more product details"

    return "Keep app in tracker"


def build_action_list(apps: list[MiniApp]) -> list[str]:
    return [
        f"{app.name}: {recommend_next_action(app)}"
        for app in apps
    ]
