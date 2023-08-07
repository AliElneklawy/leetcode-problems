import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(columns=['score', 'rank'])
    res['rank'] = scores['score'].rank(method='dense', ascending=False)
    res['score'] = scores['score']
    res = res.sort_values(by='rank')
    return res
