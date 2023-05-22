#To solve this problem in MySQL, you can use a left join to 
#retrieve the unique IDs from the EmployeeUNI table based on 
#the id column in the Employees table. If a matching unique 
#ID is found, it will be displayed; otherwise, null will be shown.

SELECT EmployeeUNI.unique_id ,Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id
;