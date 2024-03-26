from pprint import pprint
from feast import FeatureStore

path = "/Users/chenqirong/特征库/my_feature_repo/feature_repo"
store = FeatureStore(repo_path = path)

feature_vector = store.get_online_features(
    features=[
        'driver_hourly_stats:conv_rate',
        'driver_hourly_stats:acc_rate',
        'driver_hourly_stats:avg_daily_trips'
    ],
    entity_rows=[{"driver_id": 1001}]
).to_dict()

print("陈其荣的技术教程")
pprint(feature_vector)