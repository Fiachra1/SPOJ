import math


#Need to create a recursive function for this so that 24=27
def exchange(num):
    exch=0
    exch_check=0
    for i in range(2,5):
        exch_check=math.floor(num/i)
        if exch_check
        exchange(exch)
    return exch
        
while True:
    try:
        coin_value=int(input())
        new_value=exchange(coin_value)
        if coin_value<new_value:
            print(new_value)
        else:
            print(coin_value)
    except:
        break
