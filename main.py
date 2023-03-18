import openai

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
        {"role": "user", "content": "モバイルデバイスマネジメントが活用される業界はどれですか？"},  # ChatGPTに問いたいメッセージを設定する
        {"role": "assistant", "content": "モバイルデバイスマネジメントは、企業や組織でモバイルデバイスを多く利用する業界に特に活用されています。例えば、医療、金融、小売、教育、製造業などです。これらの業界では、従業員や学生などがモバイルデバイスを利用して業務を行うことが多いため、セキュリティの強化や管理が必要になります。モバイルデバイスマネジメントは、企業や組織が従業員のモバイルデバイスを一元的に管理し、セキュリティを確保するための重要なツールとなっています。"},  # ChatGPTからのメッセージを設定する
        {"role": "user", "content": "医療、金融、小売、教育、製造業ではどのような使い方が多いですか？"},  # もう少しChatGPTに問いたい場合は上記ようにChatGPTのメッセージを設定して次の質問を設定する
    ]
)

# ChatGPTからの返答内容を抽出する
# resにはその他にrole, timestamp, token数などがある
res_content = res["choices"][0]["message"]["content"]
print(res_content)
