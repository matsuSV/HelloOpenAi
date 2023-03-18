import openai

# 要約対象ファイルをコマンドラインから受け取る
input_file = input("要約したい対象のファイルのパス：")
with open(input_file, encoding='utf-8') as f:
    text = f.read()

'''
model
    2023/03 時点最新値
messages
    ・1つの辞書が1つのメッセージ
    ・role（役割）
        system　→　このチャットアプリケーションのシステム
        user　　→　このチャットアプリケーションの使用者
        assistant　→　ChatGPT側
    ・content（メッセージ内容）
'''
# 最初のメッセージはsystemがチャット全体の初期化をするメッセージを設定する必要がある、お作法、おまじない
# user → assistant → user ... とチャットのやりとりを実装していく
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"この文章を要約してください。「{text}」"},
    ]
)

# ChatGPTからの返答内容を抽出する
# resにはその他にrole, timestamp, token数などがある
res_content = res["choices"][0]["message"]["content"]
with open("output.txt", "w") as f:
    f.write(res_content)
