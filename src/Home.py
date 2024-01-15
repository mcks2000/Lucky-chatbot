import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Lucky | Chat-Bot 🤖")


#联系方式
with st.sidebar.expander("📬 联系方式"):

    st.write("**GitHub：**","[mcks2000/Lucky-chatbot](https://github.com/mcks2000/Lucky-chatbot)")
    st.write("**公众号：brother-talks** ")
    st.write("**知乎：** [二师兄 talk](https://www.zhihu.com/people/dev-daddy)")
    st.write("**邮箱** : king101125s@gmail.com")
    st.write("**Created by 二师兄**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>吉祥，你的数据智能助手 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>    
    我是吉祥，一个智能聊天机器人，融合了 Langchain 和 Streamlit 的优势。
    我使用大型语言模型提供上下文感知的互动。我的目标是帮助你更好地理解你的数据。
    我支持PDF、TXT、CSV和YouTube转录文本 🧠
    </h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Lucky's Pages
st.subheader("🚀 吉祥的页面")
st.write("""
- **Lucky-Chat**: 与矢量存储一起对数据（PDF、TXT、CSV）进行通用聊天（[索引](https://github.com/facebookresearch/faiss)有用的部分（最多4个）以响应用户）| 与[ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) 一起使用 
- **Lucky-Sheet** (beta): 在表格数据（CSV）上进行聊天| 用于精确信息| 处理整个文件| 与 [CSV_Agent](https://python.langchain.com/docs/templates/csv-agent) + [PandasAI](https://github.com/gventuri/pandas-ai) 一起用于数据操作和图形创建
- **Lucky-Youtube**: 使用 [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html) 总结YouTube视频 
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 贡献")
st.markdown("""
**吉祥正在定期开发中。请随时贡献并帮助我使它更加数据智能！!**
""", unsafe_allow_html=True)





