import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class').agg({'class':'count'}).rename(columns={'class':'count'}).reset_index()
    return pd.DataFrame(res[res['count'] >= 5]['class'])
