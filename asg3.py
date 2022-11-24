emp_data = [{"EmpId":1,
             "Ename":"A",
			 "Sal":1000,
             "Projects":[1,6,77]},
			{"EmpId":2,
             "Ename":"B",
			 "Sal":2000,
             "Projects":[11,61,77,62]},
			 {"EmpId":3,
             "Ename":"C",
			 "Sal":3000,
             "Projects":[61,77]}
			 ]

# Print names of emps who are working in project 61
for emp in emp_data:
    # print(emp)
    # print(emp["Projects"])
    for project in emp["Projects"]:
        if project == 61:
            print(emp["Ename"])
"""
# Print names of emps whose sal >= 2000
for emp in emp_data:
    # print(emp) 
    # print(emp["Sal"])
    
    if emp["Sal"] >= 2000:
        print(emp["EmpId"])
"""
       

    