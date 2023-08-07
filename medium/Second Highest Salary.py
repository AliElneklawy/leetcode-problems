import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_salaries = employee['salary'].drop_duplicates()

    sorted_salaries = unique_salaries.sort_values(ascending=False)       
    
    try:
        nth_highest = sorted_salaries.iloc[1]
    
        return pd.DataFrame({'SecondHighestSalary': [nth_highest]})
    except:
        return pd.DataFrame({'SecondHighestSalary': [None]})
