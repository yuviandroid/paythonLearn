#   1. instances variable 2. class    3. Local

#   2. instance method  2. Static   3.  class

# Constructor ----->   def  _ _init_ _():
# Destructor  ----->    def _ _delete_ _():

class A:
    name = 'ABCD'
    div = 'D'

    def __init__(self,x):
        self.div = x

a1 = A('P')
a2 = A('Q')

print(a1.name)
print(a2.name)

a1.name = 'R'
print(a1.name)
print(a2.name)

print(a1.div)
print(a2.div)
print(A.div)

A.div = 'B'
print(a1.div)
print(a2.div)
print(A.div)

a1.div = 'Z'
print(a1.div)
print(a2.div)
print(A.div)


