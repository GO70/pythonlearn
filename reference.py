#!/usr/bin/python
#Filename:reference.py

print'Simple Assignment'
shoplist=['apple','mango','cattor','banana']
mylist = shoplist

del shoplist[0]


print'shoplist is',shoplist
print'mylist is',mylist
#notice that both shoplist and mylist both print the same list whthout
#the 'apple' confirming that they point to the same object

print'Copy by making a full sice'
mylist=shoplist[:] #make a copy by doing a full slice
del mylist[0]

print'shoplist is',shoplist
print'mylist is',mylist
#notice that now the two lists are different
