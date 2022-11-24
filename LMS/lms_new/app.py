import master_data as md
import core_engine as ce
import random

# Unit Test
# ######################
l_cust_name = "aa"
l_cust_cs = 233
l_cust_req_loan_amt = 23444


ce.lms_engine(p_md=md.md_loan, p_cust_name=l_cust_name, p_cust_cs=l_cust_cs, p_cust_loan_amt=l_cust_req_loan_amt)

# Bulk Test
# ######################
for c1 in range(1000):
    l_cust_name = "aa" + str(random.randint(1, 100000))
    l_cust_cs = random.randint(100, 499)
    l_cust_req_loan_amt = random.randint(10000, 24999)
    
    ce.lms_engine(p_md=md.md_loan, p_cust_name=l_cust_name, p_cust_cs=l_cust_cs, p_cust_loan_amt=l_cust_req_loan_amt)
