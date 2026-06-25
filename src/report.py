from src.config import REPORT_TITLE
from src.formatter import format_app
from src.stats import count_by_category, count_by_ecosystem, count_by_status, count_by_tag, average_score
from src.tracker import MiniAppTracker


def build_summary(tracker: MiniAppTracker) -> str:
    lines = [
        REPORT_TITLE,
        f"Total mini apps: {tracker.count_apps()}",
        f"Average score: {average_score(tracker)}",
        "",
        "Mini Apps:"
    ]

    for app in tracker.list_apps():
        lines.append(f"- {format_app(app)}")

    lines.append("")
    lines.append("Categories:")

    for category, total in count_by_category(tracker).items():
        lines.append(f"- {category}: {total}")

    lines.append("")
    lines.append("Statuses:")

    for status, total in count_by_status(tracker).items():
        lines.append(f"- {status}: {total}")

    lines.append("")
    lines.append("Ecosystems:")

    for ecosystem, total in count_by_ecosystem(tracker).items():
        lines.append(f"- {ecosystem}: {total}")

    lines.append("")
    lines.append("Tags:")

    for tag, total in count_by_tag(tracker).items():
        lines.append(f"- {tag}: {total}")

    return "\n".join(lines)
