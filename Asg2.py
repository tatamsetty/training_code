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

"""
print(emp_data)             
print(emp_data[1])  
print(emp_data[1]["Sal"]) 
"""
print(emp_data[2])  
print(emp_data[2]["Projects"])  
print(emp_data[2]["Projects"][0]) # 62 