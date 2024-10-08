# page-gutenberg-vs-reddit-via-streamlit
不进行缓存, 直接从 xlsx 中读取数据

从 xlsx 中读取数据， 1. 处理一下 tokens, 能够独立的看到整个文本的 token 序列。 2. 计算 sts & relevance 的 spearmanr, pearsonr 相关性系数。