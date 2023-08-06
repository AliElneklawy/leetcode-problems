import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    sol = pd.DataFrame(columns=['employee_id', 'bonus'])
    sol['employee_id'] = employees['employee_id']
    sol['bonus'] = employees[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))]['salary']
    sol = sol.fillna(0).sort_values(by='employee_id')


    return sol
