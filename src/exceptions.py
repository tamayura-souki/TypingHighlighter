class BadConfigError(Exception):
    """raise 設定ファイルが上手く読み込めないとき"""
    def __init__(self, bad_item):
        super().__init__(BadConfigError.build_message(bad_item))

    def build_message(bad_item) -> str:
        return f"設定ファイル(config.json)が壊れています。ソフトをダウンロードし直すか、ファイルを修正してください。{bad_item} の項目がありません。"