from pathlib import Path

from src.tracker import MiniAppTracker


def export_markdown_report(tracker: MiniAppTracker, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Mini App Research Report",
        "",
        f"Total mini apps: {tracker.count_apps()}",
        "",
        "## Apps"
    ]

    for app in tracker.list_apps():
        lines.extend([
            f"### {app.name}",
            f"- Category: {app.category}",
            f"- Status: {app.status}",
            f"- Ecosystem: {app.ecosystem}",
            f"- Score: {app.score}/10",
            f"- Notes: {app.notes}",
            ""
        ])

    path.write_text("\n".join(lines), encoding="utf-8")
