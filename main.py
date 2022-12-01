import streamlit as st
import pandas as pd
df = pd.read_csv('hakonn.csv.gz',index_col=0)
text_input = st.text_input('タイトル')
#タイトルに該当する歌詞を抜き取る
num = df.index[df['name'].str.startswith(text_input ,na=False)]
st.write(pd.read_json(df['hako'][num[0]]))
