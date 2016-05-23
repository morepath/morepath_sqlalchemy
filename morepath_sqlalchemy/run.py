import morepath

from .app import App


def run():   # pragma: no cover
    morepath.autoscan()
    morepath.run(App())
