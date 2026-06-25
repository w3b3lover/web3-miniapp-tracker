from collections import Counter

from src.tracker import MiniAppTracker


def count_by_category(tracker: MiniAppTracker):
    return Counter(app.category for app in tracker.list_apps())


def count_by_status(tracker: MiniAppTracker):
    return Counter(app.status for app in tracker.list_apps())


def count_by_ecosystem(tracker: MiniAppTracker):
    return Counter(app.ecosystem for app in tracker.list_apps())


def count_by_tag(tracker: MiniAppTracker):
    counter = Counter()

    for app in tracker.list_apps():
        for tag in app.tags:
            counter[tag] += 1

    return counter


def average_score(tracker: MiniAppTracker):
    apps = tracker.list_apps()

    if not apps:
        return 0

    total = sum(app.score for app in apps)
    return round(total / len(apps), 2)
