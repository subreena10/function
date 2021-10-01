def eligible_for_veot(age):
    if age>=18:
        return("you are eiligble")
    else:
        return("not eiligble")
user=int(input("enter ur age: "))
age=eligible_for_veot(user)
print(age)
    