import csv
from pathlib import Path

from src.tracker import MiniAppTracker


def export_apps_csv(tracker: MiniAppTracker, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "category", "status", "ecosystem", "website", "tags", "notes"])

        for app in tracker.list_apps():
            writer.writerow([
                app.name,
                app.category,
                app.status,
                app.ecosystem,
                app.website,
                ", ".join(app.tags),
                app.notes
            ])
