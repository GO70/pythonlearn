#!/usr/bin/python
#Filename:using_list.py

#This is my shopping list
shoplist = ['apple','mango','carrot','banana']

print'I have',len(shoplist),'items to purchase.'

print'These items are:',
for item in shoplist:
	print item,
print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist
print 'I will sort my shopping list'
shoplist.sort()
print 'Sorted shopping list is',shoplist

print 'The first item i will buy is',shoplist[0]
olditme = shoplist[0]
del shoplist[0]
print 'I bought the',olditme
print 'My shopping list is now',shoplist
