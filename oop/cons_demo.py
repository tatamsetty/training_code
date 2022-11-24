class Tinitiate:

    # a class Variable
    ti_var   = 100

    def __init__(self, p_var1, p_var2):
        # These are Instance variables
        a = 10
        self.var1 = p_var1
        self.var2 = p_var2

    def cons_user(self):
        print(self.var1, self.var2)
       
    def add_num_to_class_var(self,in_num):
        # print(self.ti_var)
        print(in_num + self.ti_var)
  
  
# OBJECT of the CLASS Tinitiate
tiObject = Tinitiate(1,2)
tiObject.cons_user()
