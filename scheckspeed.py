def  check_speed(speed):
    if speed<70:
        print("ok")
    elif speed>70:
        x=speed-70
        y=x/5
        print(y,"point")
        if y>12:
            print("suspended driving license.")
user=int(input("Enter ur speed: "))
check_speed(user)
   
  
        
