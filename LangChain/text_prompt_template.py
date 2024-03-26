import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# 在文本模版以 {param} 的方式定义参数
prompt_template = PromptTemplate.from_template(
    "告诉我 {country} 的首都在哪里？"
)

# 加载大模型
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# 使用 prompt
for country in ["中国", "美国", "英国"]:
    # 传入参数值，生成prompt
    prompt = prompt_template.format(country=country)
    # 输出大模型返回数据
    print(llm(prompt))