import sys
import json
from logging import Logger

from PySide2.QtWidgets import QApplication

from exceptions import BadConfigError
from logger import get_logger
from main_window import TrayWidget
from sound_effect import SoundEffect

CONFIG_PATH = "config.json"

if __name__ == '__main__':
    logger: Logger = get_logger(__name__)
    try:
        with open(CONFIG_PATH) as f:
            config_data = json.load(f)
    except FileNotFoundError as e:
        e = FileNotFoundError(f"設定ファイル {CONFIG_PATH} が見つかりません。ソフトをダウンロードしなおすか、設定ファイルを正しく配置してください。")
        logger.error(e)
        raise e

    try:
        sound_effect = SoundEffect(config_data["sound_effects"], logger)
    except KeyError as e:
        e = BadConfigError(e.args[0])
        logger.error(e)
        raise e

    app = QApplication([])
    tray = TrayWidget()
    tray.show()

    ret = app.exec_()
    sys.exit(ret)