import os
from langchain.llms import OpenAI

# 把OpenAI的key存放在环境变量中
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  

# 加载OpenAI llm
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# 向openai输入“你好！”，并打印结果
print(llm.predict("你好！"))

llm = OpenAI(openai_api_key=OPENAI_API_KEY)