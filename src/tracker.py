from src.models import MiniApp


class MiniAppTracker:
    def __init__(self):
        self.apps = []

    def add_app(self, app: MiniApp):
        self.apps.append(app)

    def list_apps(self):
        return self.apps

    def count_apps(self):
        return len(self.apps)

    def filter_by_status(self, status: str):
        return [
            app for app in self.apps
            if app.status.lower() == status.lower()
        ]

    def filter_by_category(self, category: str):
        return [
            app for app in self.apps
            if app.category.lower() == category.lower()
        ]

    def search(self, keyword: str):
        keyword = keyword.lower()

        return [
            app for app in self.apps
            if keyword in app.name.lower()
            or keyword in app.category.lower()
            or keyword in app.notes.lower()
            or keyword in " ".join(app.tags).lower()
        ]
