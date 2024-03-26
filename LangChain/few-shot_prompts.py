import os
from langchain.llms import OpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

examples = [
    {
        "问题": "2022年12月1日，微信的DAU是多少？",
        "回答": "您要查找的DAU是：sql( select f_dau from t_product_dau where produce_name = '微信' and date = '2022-12-01')。"
    },
    {
        "问题": "MAU的字段是什么？",
        "回答": "在t_product_dau表中，MAU的字段是 f_mau_chenqirong。"
    },
    {
        "问题": "省份的字段是什么？",
        "回答": "在t_product_dau表中，省份的字段是 f_province_chenqirong。"
    }
]

example_prompt = PromptTemplate(input_variables=["问题", "回答"], template="问题: {问题}\n{回答}")

prompt_template = FewShotPromptTemplate(
    examples=examples, 
    example_prompt=example_prompt, 
    suffix="问题: {input}", 
    input_variables=["input"]
)

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
for i in ["2023年5月1日，抖音在的DAU是多少呀？",
    "2023年5月31日，抖音在广东省的MAU是多少呀？"]:

    print("====")
    print("问题：%s" % i)
    prompt = prompt_template.format(input=i)
    print(llm(prompt))