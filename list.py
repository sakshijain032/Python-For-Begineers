#List :- It's a ordered sequence of elements that can be changed,mutated or replaced
# Each element inside a list is called an item
#.append():- It's a predefined function that adds a new value given inside the bracket at the end of the list
alphabets = ["a","b","c"]
alphabets.append("d")
print (alphabets)
#.extend() :- It store each charchter of input string as a seprate entity or element in the list
Name = ("Sakshi")
a=[]
a.extend(Name)
print (a)
#print(a.extend("Sakshi"))
# For loop is a set of statements that have to be repeated for a certain number of times
for i in range(0,5):
    print(f"value of i is{i}")

count = [1,2,3,4,5]
fruits = ['apples','oranges','banana','grapes']
change = [1,'pennies',2,'dimes',3,'quarters']
#this first kind of a loop, a for a loop goes through a list
for i in count:
    print(f"This is count{i}")
#for strings    
for fruit in fruits:
    print(f"I got{fruits}")
#LIST AND FOR LOOP    
#we can also create a empty list
elements = []
# to count till 5
for i in range(0,6):
    print(f"adding i to the elements{i}")
    elements.append(i)
print(elements)
a = 'hello I am Sakshi Jain '
elements.extend(a)
print(elements)

