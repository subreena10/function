def pattern(number):
    if number==1:
        return 1
    else:
        return pattern(number-1)+3
n=int(input("Enter ur number: "))
print(pattern(n))