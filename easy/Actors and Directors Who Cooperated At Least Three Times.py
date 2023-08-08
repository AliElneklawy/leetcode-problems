import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    g = actor_director.groupby(['actor_id', 'director_id']).agg({'timestamp':'count'}).reset_index()
    return g[g['timestamp'] >= 3].drop(columns='timestamp')
