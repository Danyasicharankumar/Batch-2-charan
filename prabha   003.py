
'''
# ! Method Over-riding
Ploymorphism in classes using Inheritance

class bank:
 def ratio(self):
    print("All banks has repo rate")
class SBI(bank):
 def ratio(self):
    print("581 rate is 9%")
class 10B(bank):
 def ratio(self):
    print("IOB rate is 7.5%")

#1 = IOB()
#1.ratio()

#5=5 #5 = 581()
#s.ratio()



# Eg:3
# polymorphism using objects


#c1, c2 -->c1 = print(c1), print(c2)
#f1, f2


class c1:
    def f1(self):
        print("class1")


class c2(c1):
    def f1(self):
        print("class2")


obj = c2()
obj.f1()


def display(a):
    a.f1()
display(obj1)
display(obj2)



# ! ---> method overloading
# ! Eg:1
  class suming:
      def add(self, a, b, c):
          print(a+b)
'''
#! Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!= None and b!=None:
            print(a+b)
        else:
            print(a)
obj= summing()
obj.add(2)
obj.add(3, 4)
obj.add(1,2,3)























        
