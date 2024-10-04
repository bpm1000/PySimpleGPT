# Auto Translation Tool

このプロジェクトは、入力されたテキストを複数の言語に翻訳するためのツールです。OpenAIのAPIを利用しており、GUIにはPySimpleGUIを使用しています。

## 概要
- ユーザーが指定した文章を、選択した言語に翻訳します。
- 対応言語：英語、フランス語、ドイツ語、スペイン語、ロシア語、中国語、韓国語、日本語

## 必要な環境
- Python 3.x
- 必要なパッケージ（後述）

## インストール手順

### 1. GitHubからリポジトリをクローンする
以下のコマンドでリポジトリをクローンします：

```bash
git clone https://github.com/username/auto_translation.git
cd auto_translation
```

### 2. 必要なパッケージのインストール
次のコマンドを実行して必要なパッケージをインストールしてください：

```bash
pip install openai PySimpleGUI
```

## APIキーの設定
1. [OpenAI APIキー](https://platform.openai.com/signup)を取得します。
2. `auto_translation.py` ファイルの `openai.api_key` の部分に、自分のAPIキーを設定します：

```python
# OpenAI APIキー（必ず自身のAPIキーを使ってください）
openai.api_key = "your-api-key-here"
```

**注意**：APIキーは公開しないようにしてください。

## 使用方法
1. ターミナルまたはコマンドプロンプトで次のコマンドを実行します：

```bash
python auto_translation.py
```

2. プログラムが起動すると、以下の画面が表示されます：
   - 翻訳したいテキストを入力します。
   - 翻訳先の言語をプルダウンメニューから選択します。
   - 「実行」ボタンをクリックすると、翻訳結果が表示されます。

## 注意事項
- このツールでは、OpenAIのAPIを使用するため、APIキーが必要です。
- APIの使用には料金が発生することがあるため、使用量に注意してください。

## ライセンス
MITライセンスの下で公開されています。詳しくは[LICENSE](LICENSE)ファイルを参照してください。
