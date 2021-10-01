def check_numbers(num1,num2):
    if num1%2==0 and num2%2==0:
        print("both are even")
    else:
        print("both are not even")
check_numbers(4,6)

def check_numbers_list(num1,num2): 
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("both are even",i)
        else:
            print("both are not even",i)
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75] ,[6, 19, 24, 12, 3, 87])
