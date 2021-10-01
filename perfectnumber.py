def perfect():
    n=int(input("Enter ur number: "))
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum=sum+i
        i=i+1
    if sum==n:
        print("perfect no.")
    else:
        print("not a perfect a number.")
perfect()

# def perfect_number():
#     i=1
#     sum=0
#     while i<=1000:
#         if 
