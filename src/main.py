from src.config import DATA_FILE
from src.exporter import export_text_report
from src.loader import load_miniapps
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


if __name__ == "__main__":
    main()
