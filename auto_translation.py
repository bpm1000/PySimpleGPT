import openai
import PySimpleGUI as sg
sg.theme("DarkBlue13")

# OpenAI APIキー（必ず自身のAPIキーを使ってください。安全のため、公開しないように注意！）
# openai.api_key = "your-api-key-here"


selects = ["英語", "フランス語", "ドイツ語", "スペイン語", "ロシア語", "中国語", "韓国語", "日本語"]
layout = [[sg.T("入力文："), 
           sg.ML("こんにちは。私はラズパイZeroを使ってPythonとChatGPTの勉強をしています。", s=(50,3), k="in")],
          [sg.Im("dog2-b.png"),
          sg.Combo(selects, default_value = selects[0], s=(10), k="cb"),
          sg.T("に翻訳するよ。"),
          sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]
win = sg.Window("自動翻訳", layout,
                font=(None,14), size=(550,400))

def execute():
    prompt = f"以下の文章を{v['cb']}に翻訳してください。\n###{v['in']}"
    try:
        stream = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=True
        )
        win["txt"].update("")
        for chunk in stream:
            delta = chunk.choices[0].delta
            content = delta.get('content', '')
            if content:
                win["txt"].update(content, append=True)
                win.read(timeout=0)
        win["txt"].update("\n【以上です。】", append=True)
    except Exception as e:
        sg.popup_error(f"エラーが発生しました: {e}")


while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()