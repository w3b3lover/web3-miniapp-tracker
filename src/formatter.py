from src.models import MiniApp
from src.review import get_score_label


def format_app(app: MiniApp) -> str:
    return f"{app.name} | {app.category} | {app.status} | {app.score}/10"


def format_app_details(app: MiniApp) -> str:
    tags = ", ".join(app.tags) if app.tags else "No tags"

    lines = [
        f"Name: {app.name}",
        f"Category: {app.category}",
        f"Status: {app.status}",
        f"Ecosystem: {app.ecosystem}",
        f"Website: {app.website}",
        f"Score: {app.score}/10",
        f"Review: {get_score_label(app)}",
        f"Tags: {tags}",
        f"Notes: {app.notes}",
    ]

    return "\n".join(lines)
