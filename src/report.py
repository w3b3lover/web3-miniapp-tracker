from src.formatter import format_app
from src.tracker import MiniAppTracker


def build_summary(tracker: MiniAppTracker) -> str:
    lines = [
        "Web3 Miniapp Tracker Summary",
        f"Total mini apps: {tracker.count_apps()}",
        "",
        "Mini Apps:"
    ]

    for app in tracker.list_apps():
        lines.append(f"- {format_app(app)}")

    return "\n".join(lines)
