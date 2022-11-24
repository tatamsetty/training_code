"""
for c in range(5):
    if c == 3:
        break
    print(c)
"""

"""
for a in range(5):    
    for c in range(5):
        if c == 3:
            break
        print('c',c)
    
    break    
    print('a',a)
"""
"""
for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')    
"""
    
for c in range(3):
    if c==1:
        print('Do a very important step')
    elif c==2:
        pass # DO NOTHING
    else:
        print('normal processing')    