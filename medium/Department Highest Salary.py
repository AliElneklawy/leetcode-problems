import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id':'departmentId'})
    m = pd.merge(employee, department, on='departmentId', how='outer')
    g = m.groupby('name_y')
    return g.apply(lambda x: x[x['salary'] >= x['salary'].max()]).rename(columns={'name_y':'Department', 'name_x':'Employee', 'salary':'Salary'})[['Department', 'Employee', 'Salary']]
