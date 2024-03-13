'''
#!
Eg:3
#Take values of length and breadth of a itylis square from user and check if it is or not.
Eg:4
# #? Accept the age of 4 people and display the oldes


length=int(input())
breadth=int(input())
if length==breadth:
     print("it is a square.")
else:
    print("it is not square.")
   


# ! Eg:4
# Python program to check whether the
# given integer is a multiple of both 5 and 7
n = int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
     print("no")


# ! Eg:5
Write program to accept the cost price of a bike and display the
road tax to be paid
according to the following criteria

            cost price (in Rs)                 Tax
            >100000                              15 % + discount 6%
            >50000 and <= 100000                 5% 
            <=50000




price=int(input("entry the price:"))
total=0
if price>=100000:
   Discount=price*(6/100)
   Value=price-discount
   tax=value*(15/100)
   Total=value+tax
else:
   tax=price*(5/100)
   Total=price+tax
print("the onroad cost of bike is: ",total)


# A school has following rules for grading system:
#a. Below 25-F
#b. 25 to 45-E
#c. 45 to 50-D
#d. 50 to 60-c
#e. 60 to 80-B
# f. Above 80-A
# Ask user to enter marks and print the corresponding grade.


mark = int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark >=40 and mark<50:
    print("D")
else:
    print("Fail")



1--> short hand if else
Eg:1
= 9
=60
if a>b:
    print("A")
else:
    print("B")
?--> using short hand if else Rules


# ! code to check the given char is vowl or consonent
char= input("entry the chart")
if char=="a" or char=='e' or char =='i' or char =='o' or char =='u'
   print("is vowel")
else:
    Print("its consonent")



# ? or
char= input("entry the chart")
str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonnt")
      



#---> elif ladder using short hand if else
# eg :1
# ? find greatest among 3 varaibles using short hand if else
a=8
b=5
c=9
print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("C is greater")



# !----> for loop
# lopping can be implemented using
# for loop
# while loop


# !---> for loop
# ? for loop is for iteartion, if we know the number of time the loop have
# ? It is used to iterate the iterable eg(string, list, tuble, etc....)


# Eg:1
# To print the value from 1 to 10 using for loop


#for i in range (0, 10): #(n, n-1)
   # print(i)

# Eg:2
#for val in range(1,15,2):
#    Print(val)

for val in range(1,15,3):
     print(val)

#? Eg:3
# to decrement the value
# for val in range(10, 0, -1):
#    print(val)
# for val in range(10,0,-1):
#    print(val)


# ? Eg:4
# print the output of 7 th multiplication table  from 21 to 43
for val in range (1, 10):
    print (val*7)
for val in range (1,10+1):
    print("upendra rock",val*8)
    

#- Method:2
for val in range (1, 10):
    ans="7 x {} = {}"
    print(ans.format(val, val*7))


# ? Eg:7
for val in range(1,10):
    if val ==6:
        print(val)
        break


# ! couninue
#Eg:1
for val in range(1,10):
    if val ==6:
        continue
    print(val)


#! Practise problems
#? Print the even number between 20 to 40
for val in range(20, 41):
     if val %2=10:
        print(val)

'''

#!--------->  While loop
# While is used when we do not knoow the number of times the loop have to run
# to iterate the non iterable elemants while loop

#todo syntax


# initialisation
#while condition:
#    satetement
#    incre or decre

#! Eg:1
# to iterate number from 1 to 10

i = 0
while i<11:
     print(i)

# for loop practisee
# write a program to display sum of odd numbers and even
# numbers that fall between
# 12 and 37(including both numbers)

 
































