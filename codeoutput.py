# def employee(name,salary=20000):        #meraki q1.
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

# def primeorNot(num):     #meraki q2
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#            print(num,"is not a prime number")
# primeorNot(406)


# def greet(*names):    #meraki q3
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# def sumofdigits(number):    # meraki q4
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# print(sumofdigits(123))

def  meal(day,time):     #meraki q5
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        elif time=="lunch":
            return "dal rice"
        elif time=="dinner":
            return "paneer and  chapati"
        else :
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "fried rice"
        elif time=="lunch":
            return "aloo rice"
        elif time=="dinner":
            return "chhole bhature"
        else :
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "aloo"
        elif time=="lunch":
            return "rajma rice"
        elif time=="dinner"    :
            return "veg-chapati"
        else :
            return "time not found"
print(meal("sunday","lunch"))
print(meal("monday","dinner"))