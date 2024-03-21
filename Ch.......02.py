'''
s1 = "hello world"
# * to access string
print(s1[5:])
# indexing and slicing---> same as list and tuple


# ? to conver to lower case
s1 = "HFREDGIOU"
print(s1.lower())


# strip()--> to eleminate the space in beginning and end of string
s1 = " where are you?"
print(s1.lstrip())


# split()---> to split the world in srtring based on a character
s1 = " where are you ?"
print(s1.split())
print(s1.split())

# * replace a specific char in the string
s1 = "where are you"
print(s1.replace('r' , '&&'))

# * title()---> to write the string in format of title
s1 = 'never give up'
print(s1.capitalize())

# * join the strings
s1 = "hellow
s2 = "world"
print(s1+s2) 

s1 = " how are you
iam fine
hey there"


#* find() --> to find the index based on a character
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))

s1 = "welcome to all"
print(s1.endswith('1'))
print(s1.startswith('w'))


s1 = "67"
print(type(s1))
print(s1.isdigit())

# * print the string in reverse manner
s1 = "welcome to all"
print(s1[::1])

# ! ---> Eg:1
# wap to find number of lower case letters

s1 = "HEY there you are"
count = 0
for i in s1:
    if i.islower():
        count+=1
        print("the total num of lower case letter: ",count)       
'''
s1 = "Lorm Ipsum is simply dummy text of the printing and typesetsetting industry. Lorem
s1= s1.strip()

  

















