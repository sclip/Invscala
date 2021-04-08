import eel
from src.gui.elems import static_build
from common.guitar import guitar


@eel.expose
def setup():
    static_build.init()
    guitar.guitar.build()
    eel.finish_setup()


def load():
    guitar.guitar.load()


@eel.expose
def invalidate():
    pass
