t=int(input())
for cases in range (t):
    m,n=input().split()
    m= int(m)
    n=int(n)
    
    for i in range (m,n+1):
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
    print ('')
            