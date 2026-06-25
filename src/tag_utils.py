from src.tracker import MiniAppTracker


def get_all_tags(tracker: MiniAppTracker):
    tags = set()

    for app in tracker.list_apps():
        for tag in app.tags:
            tags.add(tag)

    return sorted(tags)


def filter_by_tag(tracker: MiniAppTracker, tag: str):
    tag = tag.lower()

    return [
        app for app in tracker.list_apps()
        if tag in [item.lower() for item in app.tags]
    ]
