# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


L1 ={'a':100,'b':50}
L2 ={'x':250, 'y':500}
L = L1.copy()
L.update(L2)
print(L)
if 'a' in L:
    del L['a']
    print(L)

Fruits = ['banana','apple','grapes']
color = ['yellow','red','green']
Fruit_colour = dict(zip(Fruits,color))
print (Fruit_colour)
print(len(Fruit_colour))
set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}
print(set1)
print(set2)
print(set1-set2)
