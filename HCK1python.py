
#Challenge No1#
#Write a Python program to calculate the factorial of a given number.
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









#Challenge No2#
def is_plandrome(str):
    str=str.replace(" ","").lower()
    return str==str[::-1]   #step slicing method


word =input('enter your word / number: ')
if is_plandrome(word):
    print(f" This {word} is a plandrome ")

else:
    print("no its not plandrome")









#Challenge No3 
# Create a program to find the sum of all elements in a list.

def sum_func(n):
    total=0
    for i in n:
        total+=i
    return total

user_input=input('enter your numbers')
numbers=[int(x) for x in user_input.split()]
print(numbers)
result=sum_func(numbers)
print(result)


# challenge No4
# Write a Python function to reverse a string.


def reversed_fun(str):
    new_str=""
    for char in str:
        new_str=char+new_str
    return new_str
  # nole

string='elonmusk'
# print(string[::-1])  #step slicing
result=reversed_fun(string)
print(string)
print(result)




#CHALLENGE DAY5
#Implement a function to find the maximum of list


def my_function(lst):
    if not lst:
        return None

    max_numb=lst[0]   #34
    for i in lst:
        if i > max_numb:
            max_numb=i
    return max_numb


list=[34,67,89,100,11]
result=my_function(list)
if result is not None:
    print("the max number is: ",result)
else:
    print("this is empty list")

# max_number=max(list)
# print(max_number)



# Challenge No 6 and 7
# copy challenge No 6 from my youtube video if you want due to deletion i forget to uplaod challenge 6 code

def fib_function(n):
    fib_sequence=[]
    a,b=0,1;
    for _ in range(n):
        fib_sequence.append(a)
    return fib_sequence

user_input=int(input('enter your n numbers: '))
result=fib_function(user_input)
print(result)





#Challenge 8
# Write a function to check if two given strings are anagrams.
# list. ,tisl

def is_anagram(str1, str2):
    str1_replace=str1.replace(" ","").lower()
    str2_replace = str2.replace(" ", "").lower()

    return sorted(str1_replace) == sorted(str2_replace)


string1=input('enter your string one: ')
string2=input('enter your string two: ')

result=is_anagram(string1, string2)
if result:
    print("This is angram:",result)

else:
    print('this strings is not anagrams')
