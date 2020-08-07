#define a function and memoise it for larger numbers
def prime(a,b):
    for i in range (a,b+1):
        if i==1:
            continue
        elif i==2:
            print(2)
            continue
        val=2
        while val <= i:
            if val==i:
                print(i)
                break
            elif i%val==0:
                break
            else:
                val +=1 

t=int(input())
for cases in range (t):
    m,n=input().split()
    m= int(m)
    n=int(n)
    prime(m,n)
    print ('')
            