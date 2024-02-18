import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = employee.sort_values(by='salary', ascending=False)
    sorted_salary.drop_duplicates(subset=['salary'], keep="last", inplace=True)
    return pd.DataFrame({'SecondHighestSalary': [None if len(sorted_salary)<2 else sorted_salary.iloc[1,1]]})