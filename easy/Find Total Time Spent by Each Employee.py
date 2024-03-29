import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']

    return employees.groupby(['event_day', 'emp_id']).agg({'total_time':'sum'}).reset_index().sort_values(by='emp_id').rename(columns={'event_day':'day'})
