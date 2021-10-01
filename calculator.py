# def calculator(num_x,num_y,operation):
#     if operation=="+":
#         return(num_x+num_y,"addition")
#     elif operation=="-":
#         return(num_x-num_y,"substract")
#     elif operation=="*":
#         return(num_x*num_y,"multiply")
#     elif operation=="%":
#         return(num_x%num_y,"divide")
# number_1=calculator(20,24,"+")
# print(number_1)
# number_2=calculator(90,23,"-")
# print(number_2)
# number_3=calculator(50,60,"*")
# print(number_3)
# number_4=calculator(40,4,"%")
# print(number_4)


# def calculator(num_x,num_y,operation):
#     if operation=="+":
#         return(num_x+num_y,"addition")
#     elif operation=="-":
#         return(num_x-num_y,"substract")
#     elif operation=="*":
#         return(num_x*num_y,"multiply")
#     elif operation=="%":
#         return(num_x%num_y,"divide")
# num_x=int(input("Enter a yoyur number: "))
# num_y=int(input("Enter your number: "))
# operation=input("choose operation: ")
# add_result= calculator(num_x,num_y,operation)
# print(add_result)
# result_substract=calculator(num_x,num_y,operation)
# print(result_substract)
# result_multilpy=calculator(num_x,num_y,operation)
# print(result_multilpy)
# result_divide=calculator(num_x,num_y,operation)
# print(result_divide)


def list_change(num_x,num_y):
    i=0
    a=[]
    while i <len(num_x):
        b=num_x[i]*num_y[i]
        a.append(b)
        i+=1
    print(a)
list_change([5, 10, 50, 20], [2, 20, 3, 5])
