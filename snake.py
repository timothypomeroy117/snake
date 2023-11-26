print ("Hello World")

var1 = "none"
Var2 = 2

if var1 is "none":
  print ("It is a none variable")
else:
    print ("It is not a none variable")

occupation = ["Doctor", "Engineer", "Analyst"]
for x in occupation:
    print(x) 

sarah = bob = mike = 17
print (sarah)
print (bob)

name, age = "avi" , 22
print (age)
print (name)

age1 = 12
age2 = 18
print(age1 + age2)

firstname = "avi"
lastname = "jane"
print(firstname + " " + lastname)

sent = "avi was playing basketball"
print(sent[0:3])

shopping_list =['apples','bananas','oranges','cheese']
print (shopping_list[0])
print (shopping_list[0:2])
shopping_list.append('blueberries')
print (shopping_list)
shopping_list[0] = 'cherries'
print(shopping_list)
del shopping_list[1]
print (shopping_list)

list_num = [1,4,7,23.6]
print(max(list_num))
print(min(list_num))

students = {'bob': 12, 'rachel': 13, 'emily': 15}
print(students)
print(students['rachel'])
students['rachel'] = 14
del students['emily']
print(len(students))

tup = ('oranges', 'apples', 'bananas')
# tup[0] = 'cherries'
print(tup)
tup2 = (12,14)
tup3 = tup +tup2
print(tup3)

if 5>3:
  print ('hello')
else:
   print ('flase')
  
age = 16
if age <= 15:
   print('older')
elif age == 16:
   print('are')
elif age == 17:
   print('arnt')
elif age >= 13 and age <=18:
   print('teen')
else:
   print('younger')

list = ['apples', 'bananas', 'cherries']
tup = (2,6,10)
for item in tup:
  print(item)

for i in range(0, 11):
   print(i)
for i in range(0, 11, 2):
   print(i)
for i in range(0, 5):
   for j in range (0,3):
     print(i*j)

c = 0
while c < 5:
   c =c +1
   print(c)
c = 0
while c < 5:
   c =c +1
   if c ==3:
    break
   print(c)
c = 0
while c < 5:
   c =c +1
   if c ==3:
    continue
   print(c)

