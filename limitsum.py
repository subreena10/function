def numbers(limit):
    i=0
    sum1=0
    sum2=0
    while i<=20:
        if i%3==0:
            sum1+=i
            print(i,"multiply of 3")
        elif i%5==0:
            sum2+=i
            print(i,"multiply of 5")
        i+=1
    sum=sum1+sum2
    print(sum)
numbers(20)