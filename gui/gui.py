import eel


def init(path="gui/gui_path.txt", gui_path=None):
    if gui_path is None:
        with open(path, "r") as text:
            gui_path = text.read()
    eel.init(str(gui_path), allowed_extensions=['.js', '.html'])
    eel.start('index.html', mode="default", size=(800, 600))  # Start (this blocks and enters loop)


if __name__ == "__main__":
    init(gui_path="/web/")
