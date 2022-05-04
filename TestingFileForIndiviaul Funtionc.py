import pandas as pd
employeeList = pd.read_excel("EmployeeTest.xlsx")
employeeList.head()
x = (employeeList.sample(n=3))
print(x.iloc[2])