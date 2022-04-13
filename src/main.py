import sys
import json

from PySide2.QtWidgets import QApplication

from main_window import TrayWidget
from sound_effect import SoundEffect

if __name__ == '__main__':
    with open("config.json") as f:
        config_data = json.load(f)

    sound_effect = SoundEffect(config_data["sound_effects"])

    app = QApplication([])
    tray = TrayWidget()
    tray.show()

    ret = app.exec_()
    sys.exit(ret)