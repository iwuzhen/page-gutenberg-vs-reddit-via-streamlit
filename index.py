import pandas as pd
import os
import pathlib
import streamlit as st
import json

from scipy.stats import pearsonr, spearmanr

module_path = os.path.dirname(__file__)
DATA_PATH = pathlib.Path(module_path).joinpath('./data/data.xlsx')

title='''
# 古登堡 vs reddit

两个数据源：古登堡和reddit

方法：每段文本取8000字符，计算文本两两的相似度（STS和tokens平均google距离）

info(sheet)：包含所有文本的信息

其他sheet计算的两两相似度
'''

st.markdown(title)


st.markdown("## 古登堡 _info")
df = pd.read_excel(DATA_PATH, sheet_name='古登堡_info')
df['tokens'] = df['tokens'].map(lambda x:list(json.loads(x)[0].keys()))
st.dataframe(df,hide_index=True,    column_config={
        "id": "id",
        "text": "text",
        "tokens": st.column_config.ListColumn(
            "tokens", 
            width="large",
        ),
    },)

# st.markdown("## 古登堡 STS 相关度")
df1 = pd.read_excel(DATA_PATH, sheet_name='古登堡STS相关度')
# st.dataframe(df1,hide_index=True,)

# st.markdown("## 古登堡 tokens 相关度")
df2 = pd.read_excel(DATA_PATH, sheet_name='古登堡tokens相关度')
# st.dataframe(df2,hide_index=True,)

df = pd.merge(df1, df2, on=['idA', 'idB'])

st.markdown("## 古登堡 reddit STS, google distance, relevance ")
st.dataframe(df,hide_index=True,)

# v1,_ = spearmanr(df["STS"],df["google_distance"]) 
# v2,_ = spearmanr(df["relevance"],df["google_distance"]) 
v3,_ = spearmanr(df["STS"],df["relevance"]) 

docs = [{
    '相关系数算法': "spearmanr",
    # 'STS - google_distance': v1,
    # 'relevance - google_distance': v2,
    'STS - relevance': v3,
}]

# v1,_ = pearsonr(df["STS"],df["google_distance"]) 
# v2,_ = pearsonr(df["relevance"],df["google_distance"]) 
v3,_ = pearsonr(df["STS"],df["relevance"]) 

docs.append({
    '相关系数算法': "pearsonr",
    # 'STS - google_distance': v1,
    # 'relevance - google_distance': v2,
    'STS - relevance': v3,
})
df = pd.DataFrame(docs)

st.markdown("## 古登堡书籍 STS - relevance 相关系数")
st.dataframe(df,hide_index=True,)



st.markdown("## reddit info")
df = pd.read_excel(DATA_PATH, sheet_name='reddit_info')
df['tokens'] = df['tokens'].map(lambda x:list(json.loads(x)[0].keys()))
st.dataframe(df,hide_index=True,column_config={
        "id": "id",
        "title": st.column_config.TextColumn(
            "title",
            width="medium",
        ),
        "text": "text",
        "tokens": st.column_config.ListColumn(
            "tokens", 
            width="large",
        ),
    })

# st.markdown("## reddit STS 相关度")
df1 = pd.read_excel(DATA_PATH, sheet_name='redditSTS相关度')
# st.dataframe(df1,hide_index=True,)

# st.markdown("## reddit tokens 相关度")
df2 = pd.read_excel(DATA_PATH, sheet_name='reddit tokens相关度')
# st.dataframe(df2,hide_index=True,)


df = pd.merge(df1, df2, on=['idA', 'idB'])
st.markdown("## reddit STS, google distance, relevance ")
st.dataframe(df,hide_index=True,)


v3,_ = spearmanr(df["STS"],df["relevance"]) 

docs = [{
    '相关系数算法': "spearmanr",
    'STS - relevance': v3,
}]

v3,_ = pearsonr(df["STS"],df["relevance"]) 

docs.append({
    '相关系数算法': "pearsonr",
    'STS - relevance': v3,
})
df = pd.DataFrame(docs)

st.markdown("## reddit STS - relevance 相关系数")
st.dataframe(df,hide_index=True,)

