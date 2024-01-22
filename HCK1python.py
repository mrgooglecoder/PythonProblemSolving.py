
# Write a Python program to calculate the factorial of a given number.
# recursion

def factorial_num(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_num(n-1)

 # 5  ===120
 # 5*factorial_num(4)
 # 4*factorial_num(3)
 # 3*factorial_num(2)
 # 2*factorial_num(1)
 # 2*1=2


number=int(input(" enter your number"))
if number <0:
    print("The factorial of this number does not exit")

else:
    result=factorial_num(number)
    print(f"The factorial of {number} is: ",result)



def is_plandrome(str):
#     str=str.replace(" ","").lower()
#     return str==str[::-1]   #step slicing method
# 
# 
# word =input('enter your word / number: ')
# if is_plandrome(word):
#     print(f" This {word} is a plandrome ")
# 
# else:
#     print("no its not plandrome")
