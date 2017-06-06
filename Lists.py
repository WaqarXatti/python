# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:11:55 2017

@author: rameez
"""

list1 = ['physics', 'chemistry', 1997, 2000] 
list2 = [1, 2, 3, 4, 5, 6, 7 ] 
print ("list1[0]: ", list1[0]) 
print ("list2[1:5]: ", list2[1:5]) 



list = ['physics', 'chemistry', 1997, 2000] 
print ("Value available at index 2 : ", list[2]) 
list[2] = 2001 
print ("New value available at index 2 : ", list[2]) 


list = ['physics', 'chemistry', 1997, 2000] 
print (list) 
del list[2] 
print ("After deleting value at index 2 : ", list)



list1 = ['physics', 'chemistry', 'maths'] 
print (len(list1)) 
list2=list(range(5)) #creates list of numbers between 0-4 
print (len(list2)) 


list1, list2 = ['C++','Java', 'Python'], [456, 700, 200] 
print ("Max value element : ", max(list1)) 
print ("Max value element : ", max(list2))



list1, list2 = ['C++','Java', 'Python'], [456, 700, 200] 
print ("min value element : ", min(list1)) 
print ("min value element : ", min(list2)) 



aTuple = (123, 'C++', 'Java', 'Python') 
list1 = list(aTuple) 
print ("List elements : ", list1) 
str="Hello World" 
list2=list(str) 
print ("List elements : ", list2) 


list1 = ['C++', 'Java', 'Python'] 
list1.append('C#') 
print ("updated list : ", list1) 


aList = [123, 'xyz', 'zara', 'abc', 123]; 
print ("Count for 123 : ", aList.count(123)) 
print ("Count for zara : ", aList.count('zara'))



list1 = ['physics', 'chemistry', 'maths'] 
list2=list(range(5)) #creates list of numbers between 0-4 
list1.extend('Extended List :', list2) 
print (list1)


list1 = ['physics', 'chemistry', 'maths'] 
print ('Index of chemistry', list1.index('chemistry')) 
print ('Index of C#', list1.index('C#'))



list1 = ['physics', 'chemistry', 'maths'] 
list1.insert(1, 'Biology') 
print ('Final list : ', list1)

list1 = ['physics', 'Biology', 'chemistry', 'maths'] 
list1.pop() 
print ("list now : ", list1) 
list1.pop(1) 
print ("list now : ", list1)



list1 = ['physics', 'Biology', 'chemistry', 'maths'] 
list1.remove('Biology') 
print ("list now : ", list1) 
list1.remove('maths') 
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths'] 
list1.reverse() 
print ("list now : ", list1)


list1 = ['physics', 'Biology', 'chemistry', 'maths'] 
list1.sort() 
print ("list now : ", list1)


