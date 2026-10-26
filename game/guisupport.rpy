## gui.scale() is used throughout gui.rpy to size the interface. The Ren'Py
## launcher normally bakes these numbers in when it creates a project; this
## keeps them as-is (the game is designed at 1280x720).

init -100 python in gui:

    def scale(n):
        return int(n)
