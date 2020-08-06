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
    try:
        coin_value=int(raw_input())
        new_value=exchange(coin_value)
        if coin_value<new_value:
            print(new_value)
        else:
            print(coin_value)
    except:
        break
