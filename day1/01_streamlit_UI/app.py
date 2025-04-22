import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
st.title("就活生さんマイページ登録！")
st.markdown("マイページを作りましょう")

# ============================================
# サイドバー 
# ============================================
st.sidebar.header("マイページです")
st.sidebar.info("まだ登録は完了していません。")

# ============================================
# 基本的なUI要素
# ============================================
st.header("弊社のマイページ！")

# テキスト入力
st.subheader("基本情報")
name = st.text_input("名前")
DOB = st.date_input("生年月日")

st.subheader("学歴")
uni = st.text_input("大学名")
uni_ent = st.date_input("大学入学日")
col1, col2 = st.columns(2)
with col1:
    uni_grad = st.date_input("卒業（予定）日")
with col2:
    option = st.selectbox(
    "卒業",
    ["済み", "予定"]
)

st.subheader("弊社を知ったきっかけ")
first_contacts = ["弊社HP", "FaceBook", "LinkedIn"]
contacts = []
for contact in first_contacts:
    if st.checkbox(contact):
        contacts.append(contact) #wth?

st.subheader("ラストステップ")
if st.checkbox("利用規約に同意する"):
    agreed = True
else:
    agreed = False

if st.button("クリックしてください"):
    if agreed:
        st.success("完了！")
    else:
        st.error("同意する！")
