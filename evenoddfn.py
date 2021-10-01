def numbers():
    i=1
    while i<=20:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i+=1
numbers()









# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# def icecream(*flavours):                     #arbitetory
#     for flavour in flavours:
#         print("i love " + flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry")

# def attendance(name,status="absent"):           #default
#     print(name,"is",status," today")
# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")