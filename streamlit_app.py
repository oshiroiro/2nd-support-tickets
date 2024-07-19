import streamlit as st

# フォームのタイトル
st.title("お問い合わせフォーム")

# 問い合わせの種類を選択するセレクトボックス
query_type = st.selectbox(
    "お問い合わせの種類を選択してください",
    ["技術的な問題", "販売に関する問い合わせ", "その他"]
)

# 共通の入力フィールド
name = st.text_input("お名前")
email = st.text_input("メールアドレス")

# 問い合わせの種類に応じて追加の入力フィールドを表示
if query_type == "技術的な問題":
    problem_description = st.text_area("問題の詳細を記入してください")
    screenshot = st.file_uploader("スクリーンショットをアップロード（任意）")

elif query_type == "販売に関する問い合わせ":
    product = st.text_input("製品名")
    purchase_date = st.date_input("購入日")

elif query_type == "その他":
    other_query = st.text_area("お問い合わせ内容を記入してください")

# 送信ボタン
if st.button("送信"):
    if query_type == "技術的な問題":
        st.write("技術的な問題として受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("問題の詳細:", problem_description)
        if screenshot is not None:
            st.write("スクリーンショットがアップロードされました。")
        
    elif query_type == "販売に関する問い合わせ":
        st.write("販売に関する問い合わせとして受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("製品名:", product)
        st.write("購入日:", purchase_date)
        
    elif query_type == "その他":
        st.write("その他のお問い合わせとして受け付けました。")
        st.write("お名前:", name)
        st.write("メールアドレス:", email)
        st.write("お問い合わせ内容:", other_query)

    st.success("お問い合わせありがとうございます。")
