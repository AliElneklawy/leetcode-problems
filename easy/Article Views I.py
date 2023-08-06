import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return(pd.DataFrame(views.query('author_id == viewer_id')['viewer_id'].unique()).rename({0:'id'}, axis=1).sort_values(by='id'))
