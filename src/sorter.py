from src.models import MiniApp


def sort_by_name(apps: list[MiniApp]):
    return sorted(apps, key=lambda app: app.name.lower())


def sort_by_score(apps: list[MiniApp], reverse: bool = True):
    return sorted(apps, key=lambda app: app.score, reverse=reverse)


def get_top_apps(apps: list[MiniApp], limit: int = 3):
    return sort_by_score(apps)[:limit]
