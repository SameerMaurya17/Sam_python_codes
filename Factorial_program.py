# Factorial of a number

num=4
factorial=1

if num<0:
    print("Factorial for this number doesn't exist")
    
elif num == 0:
    print("The factorial for this number is 1")

else:
    for i in range(1,num+1):
    
        factorial =factorial*i
print("The factorial of",num, "is",factorial)
