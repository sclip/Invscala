import eel
from src.gui.elems import static_build
from src.data.instrument.guitar import guitar


@eel.expose
def setup():
    static_build.init()
    guitar.guitar.build()
    eel.finish_setup()


def load():
    guitar.guitar.init()


@eel.expose
def invalidate():
    pass
