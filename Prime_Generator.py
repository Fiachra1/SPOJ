import sympy

#def prime(a, b): 
    #if a <= 2: 
        #print(2)
    #else:
        #for i in range(a, b+1): 
            #val=2
            #while val <= i:
                #if val==i:
                    #print(i)
                    #break
                #elif i%val==0:
                    #break
                #else:
                    #val +=1 

t=int(input())
for cases in range (t):
    m,n=input().split()
    m= int(m)
    n=int(n)
    for i in range (m,n+1):
        if sympy.isprime(i):
            print(i)
        else:
            continue
    
    #prime(m,n)
    print ('')
            