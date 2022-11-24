import datetime
from threading import Thread 

"""
print("Started at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
a=0
for c1 in range(1,500000001):
    a+=1
    
print(a)
print("Ended at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
"""

results ={}

print("Started at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))
def counter1(thread_id,st,ed):
    a=0
    for c1 in range(st,ed+1):
        a+=1
     
    results[thread_id] = a  

    
t1 = Thread(target=counter1, args=(1,1,100000000,))
t1.start()

t2 = Thread(target=counter1, args=(2,100000001,200000000,))
t2.start()

t3 = Thread(target=counter1, args=(3,200000001,300000000,))
t3.start()

t4 = Thread(target=counter1, args=(4,300000001,400000000,))
t4.start()

t5 = Thread(target=counter1, args=(5,400000001,500000000,))
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()


final=0
for v in results.values():
    final = final+v
    
print(final)    

print("Ended at: ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))