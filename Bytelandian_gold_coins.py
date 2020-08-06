import math
#Need to create a recursive function for this so that 24=27
def exchange(num):
    nv=0
    for i in range(1,4):
        xi=math.floor(num/(i+1))
        if xi<12:
            ni=xi
        else:
            ni=exchange(xi)
        nv+=ni
    return nv
    
while True:
    inputs=[]
    try:
        for i in range (10):
            inputs.append(int(input()))
    except:
        break
        
for val in inputs:
    new_value=exchange(val)
    if val<new_value:
        print(new_value)
    else:
        print(val)