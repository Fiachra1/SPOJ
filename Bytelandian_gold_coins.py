import math
#Need to create a recursive function for this so that 24=27
#Need to update this to include memo (dynamic programming) . Recursion - O(2^n) Recursion incl memo -- O(n)
def exchange(num):
    nv=0
    memo=[]
    if len(memo)<num:
        for i in range(1,4):
            xi=math.floor(num/(i+1))
            if xi<12:
                ni=xi
            else:
                ni=exchange(xi)
            nv+=ni
        memo.insert(num, nv)
    else:
        nv=memo[num]
    return nv
    
inputs=[]
while True:
    try:
        input_int=int(input())
        inputs.append(input_int)
    except:
        break
    
for val in inputs:
    new_value=exchange(val)
    if val<new_value:
        print(new_value)
    else:
        print(val)