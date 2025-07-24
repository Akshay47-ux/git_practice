#pytho program to implement factotial using recursive functio0n 
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num *fact(num-1)

#taking  input from the user 
num=int(input("enter a number to get the factoriaal"))
result= fact(num)
if num<0:
    print("please enter a positive number")
else:
    print("the factorial of a number ",result)