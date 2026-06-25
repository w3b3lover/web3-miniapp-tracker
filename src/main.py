from src.config import DATA_FILE
from src.csv_exporter import export_apps_csv
from src.exporter import export_text_report
from src.loader import load_miniapps
from src.markdown_exporter import export_markdown_report
from src.report import build_summary
from src.tracker import MiniAppTracker


def main():
    tracker = MiniAppTracker()
    apps = load_miniapps(DATA_FILE)

    for app in apps:
        tracker.add_app(app)

    summary = build_summary(tracker)
    print(summary)

    export_text_report(summary, "reports/summary.txt")
    export_apps_csv(tracker, "reports/miniapps.csv")
    export_markdown_report(tracker, "reports/miniapps.md")


if __name__ == "__main__":
    main()
