import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    try:
        per = ((delivery['order_date'] == delivery['customer_pref_delivery_date']).value_counts(normalize=True).loc[True] * 100).__round__(2)
        res = pd.DataFrame([{'immediate_percentage':per}])
    except:
        res = pd.DataFrame([{'immediate_percentage':0}])
    return res
