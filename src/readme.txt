# TypingHighlighter v0.1.1
作: 珠響そうき

YouTube等で作業配信するときに便利なソフト。タイピング時にいいかんじに音を出す。

## 使用方法
TypingHighlighter.exe をダブルクリックして実行します。
正常に実行されれば、キータイプ・マウスクリック・マウスホイールのたびに効果音が鳴ります。
終了する際は、タスクトレイのチェックマークのアイコンを右クリックして、メニューからQuitをクリックしてください。
(タスクトレイはタスクバー右側、^ マークをクリックして出てくるアイコン郡)

※重要
標準で同梱している効果音素材は、OtoLogic さんのフリー素材です。
よって、配信等で使用する場合、OtoLogic さんの著作権表記が必要になります。
音声素材を差し替えて使用する場合、著作権表記無しで使用できます。

## 動作環境
Windows10

## 設定方法
キータイプの効果音を、好きな音声に変更することができます。
音声ファイルは`.mp3`と`.wav`に対応しています。
また、`config.json`ファイルを編集することで、読み込むファイルのパスと効果音の音量を変更できます。

## 更新履歴
- 2022/04/ 0.1.1 エラー周りを分かりやすく改善・ロガーの実装
- 2022/04/13 0.1.0 タイプ音を鳴らす機能最低限の機能実装版リリース

## 著作権表記
### 付属の音声ファイル
OtoLogic - CC BY 4.0 https://otologic.jp/

### 使用したライブラリ等
Python - PSF LICENSE 3.10 https://docs.python.org/3/license.html
PySide2 - LGPLv3 https://pypi.org/project/PySide2/
pynput - LGPLv3 https://pypi.org/project/pynput/
pygame - LGPLv2.1 https://pypi.org/project/pygame/
