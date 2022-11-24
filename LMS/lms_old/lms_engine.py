md_loan= (
 {"cs_start":100,"cs_end":199,"loan_amt_start":10000,"loan_amt_end":14999,"interest":5  ,"duration":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":10000,"loan_amt_end":14999,"interest":4.5,"duration":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":10000,"loan_amt_end":14999,"interest":4  ,"duration":72}
,{"cs_start":400,"cs_end":499,"loan_amt_start":10000,"loan_amt_end":14999,"interest":3.5,"duration":72}
,{"cs_start":100,"cs_end":199,"loan_amt_start":15000,"loan_amt_end":19999,"interest":5  ,"duration":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":15000,"loan_amt_end":19999,"interest":4.5,"duration":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":15000,"loan_amt_end":19999,"interest":4  ,"duration":72}
,{"cs_start":400,"cs_end":499,"loan_amt_start":15000,"loan_amt_end":19999,"interest":3.5,"duration":72}
,{"cs_start":100,"cs_end":199,"loan_amt_start":20000,"loan_amt_end":24999,"interest":5  ,"duration":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":20000,"loan_amt_end":24999,"interest":4.5,"duration":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":20000,"loan_amt_end":24999,"interest":4  ,"duration":72}
,{"cs_start":400,"cs_end":499,"loan_amt_start":20000,"loan_amt_end":24999,"interest":3.5,"duration":72}
)

# Test Case 1
CustName = "A"
CustCS = 233
CustLoanAmount = 12300

# Test Case 2
CustName = "A"
CustCS = 366
CustLoanAmount = 21300

total_amt = -1

for lkp in md_loan:
    # print(lkp)
    if CustCS >=lkp["cs_start"] and CustCS<=lkp["cs_end"] and CustLoanAmount >=lkp["loan_amt_start"] and CustLoanAmount<=lkp["loan_amt_end"]:
        print(lkp["interest"])
        print(lkp["duration"])
        total_amt = CustLoanAmount + (CustLoanAmount * (lkp["interest"]/100))
        print('Principal',CustLoanAmount)
        print('Interest Amt',(CustLoanAmount * (lkp["interest"]/100)))
        print('total',total_amt)
        break