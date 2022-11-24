import json

bill = '''{      "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5.005
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":true
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 } 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                  '''

data = json.loads(bill)

# print(data)

# print(type(data['BillDetails']))

# Get Subset of JSON
# print(data["BillDetails"])
# 
# JSON Nested value, Get First Product
# print(data["BillDetails"][1]['UnitPrice'])
# 
# JSON Get All Products
# for restaurant in data["BillDetails"]:
    # print(restaurant["Product"])
# 
# dumps object to JSON string
# for restaurant in data["BillDetails"]:
    # print(data)
    # del restaurant["Product"]
    # data_new =json.dumps(data)
    # print(data_new)
# 
# dumps object to JSON string with idention
# for restaurant in data["BillDetails"]:
      # del restaurant["Product"]
      # data_new = json.dumps(data, indent=2)
      # print(data_new)
# 
# 
# dumps object to JSON string with idention and sort
for restaurant in data["BillDetails"]:
    del restaurant["Product"]
    data_new = json.dumps(data, indent=2,sort_keys=False)
    print(data_new)
