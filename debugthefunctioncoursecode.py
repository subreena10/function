# def greet(names):     #greet()can take 1 positional argument but 4 were given.
#     for name in names:
#         print("Welcome", name)
# greet("Rinki")

# def info(name, age ="16" ):        #"16" was missing it is default parameter type syntax mistake
#     print(name + " is " + age + " years old")
# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

def studentDetails(name,currentMilestone,mentorName):  # type error  studentdetails() missing 1 requried positional arugment: mentorname
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
studentDetails("Nilam","loop","saloni panwar")