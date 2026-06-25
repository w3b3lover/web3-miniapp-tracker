from src.loader import load_miniapps
from src.report import build_summary
from src.tracker import MiniAppTracker


def main():
    tracker = MiniAppTracker()
    apps = load_miniapps("data/miniapps.json")

    for app in apps:
        tracker.add_app(app)

    print(build_summary(tracker))


if __name__ == "__main__":
    main()
