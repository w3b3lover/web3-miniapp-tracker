import argparse

from src.config import DATA_FILE
from src.formatter import format_app
from src.loader import load_miniapps
from src.tag_utils import filter_by_tag
from src.tracker import MiniAppTracker


def build_tracker() -> MiniAppTracker:
    tracker = MiniAppTracker()

    for app in load_miniapps(DATA_FILE):
        tracker.add_app(app)

    return tracker


def main():
    parser = argparse.ArgumentParser(description="Web3 mini app tracker")
    parser.add_argument("--status", help="Filter mini apps by status")
    parser.add_argument("--category", help="Filter mini apps by category")
    parser.add_argument("--search", help="Search mini apps by keyword")
    parser.add_argument("--tag", help="Filter mini apps by tag")

    args = parser.parse_args()
    tracker = build_tracker()

    apps = tracker.list_apps()

    if args.status:
        apps = tracker.filter_by_status(args.status)

    if args.category:
        apps = tracker.filter_by_category(args.category)

    if args.search:
        apps = tracker.search(args.search)

    if args.tag:
        apps = filter_by_tag(tracker, args.tag)

    for app in apps:
        print(format_app(app))


if __name__ == "__main__":
    main()
