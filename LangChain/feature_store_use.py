import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, StringPromptTemplate
from pprint import pprint
from feast import FeatureStore

path = "/Users/chenqirong/特征库/my_feature_repo/feature_repo"
feature_store = FeatureStore(repo_path = path)

template = """你是陈其荣的智能助手，我会给你网约车司机的统计分析指标。

如果司机的下单率超过0.5，请你对司机说一句赞美的话；否则，请你对司机说一个关于天气的笑话安慰他。

以下是司机的统计指标:
下单率: {conv_rate}
成交率: {acc_rate}
日均行程: {avg_daily_trips}

请问你要对司机说的话是："""

prompt_template = PromptTemplate.from_template(template)

def prompt_format_by_feature(prompt_template, entry_id, feature_store):
    driver_id = entry_id
    feature_vector = feature_store.get_online_features(
        features=[
            "driver_hourly_stats:conv_rate",
            "driver_hourly_stats:acc_rate",
            "driver_hourly_stats:avg_daily_trips",
        ],
        entity_rows=[{"driver_id": driver_id}],
    ).to_dict()
    return prompt_template.format(
        conv_rate=feature_vector["conv_rate"][0],
        acc_rate=feature_vector["acc_rate"][0],
        avg_daily_trips=feature_vector["avg_daily_trips"][0]
    )

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

for driver_id in [1001, 1002, 1003, 1004, 1005, 1006]:
    print("=== llm 对 %s 司机的回答" % driver_id)
    # 传入参数值，生成prompt
    prompt = prompt_format_by_feature(prompt_template, driver_id, feature_store)
    # 输出大模型返回数据
    print(llm(prompt))