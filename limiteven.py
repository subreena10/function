def show_numbers(limit):
    i=0
    while i<=20:
        if i%2==0:
            print(i,"even")
        else: 
            print(i,"not even")
        i+=1
show_numbers(20)