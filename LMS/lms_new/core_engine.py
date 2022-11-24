
def lms_engine(p_md, p_cust_name, p_cust_cs, p_cust_loan_amt):
    for lkp in p_md:
        # print(lkp)
        if p_cust_cs >=lkp["cs_start"] and p_cust_cs<=lkp["cs_end"] and p_cust_loan_amt >=lkp["loan_amt_start"] and p_cust_loan_amt<=lkp["loan_amt_end"]:
            # print(lkp["interest"])
            # print(lkp["duration"])
            total_amt = p_cust_loan_amt + (p_cust_loan_amt * (lkp["interest"]/100))
            print(p_cust_name,"Your Loan is approved, details:")
            print('Principal',p_cust_loan_amt)
            print('Interest Amt',(p_cust_loan_amt * (lkp["interest"]/100)))
            print('total',total_amt)
            break