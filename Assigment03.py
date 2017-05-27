
str1 = "This is/tb string"
print (str1)
str = "this is string example....wow!!!" 
print ("str.capitalize() : ", str.capitalize()) 

print ("str.center(40, 'a') : ", str.center(40, 'a'))

sub='i' 
print ("str.count('i') : ", str.count(sub)) 
sub='exam' 
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40)) 

#!/usr/bin/python3 
Str='this is string example....wow!!!' 
suffix='!!' 
print (Str.endswith(suffix)) 
print (Str.endswith(suffix,20)) 
suffix='exam' 
print (Str.endswith(suffix)) 
print (Str.endswith(suffix, 0, 19)) 


str = "this is\tstring example....wow!!!" 
print ("Original string: " + str) 
print ("Defualt exapanded tab: " +  str.expandtabs()) 
print ("Double exapanded tab: " +  str.expandtabs(16))

#!/usr/bin/python3 
str1 = "this is string example....wow!!!" 
str2 = "exam"; 
print (str1.find(str2)) 
print (str1.find(str2, 10)) 
print (str1.find(str2, 40))


#!/usr/bin/python3 
str1 = "this is string example....wow!!!" 
str2 = "exam"; 
print (str1.index(str2)) 
print (str1.index(str2, 10)) 
print (str1.index(str2, 40))


#!/usr/bin/python3 
str = "this2016"  # No space in this string 
print (str.isalnum()) 
str = "this is string example....wow!!!" 
print (str.isalnum())


#!/usr/bin/python3 
str = "this";  # No space & digit in this string 
print (str.isalpha()) 
str = "this is string example....wow!!!" 
print (str.isalpha())


str = "123456";  # Only digit in this string 
print (str.isdigit()) 
str = "this is string example....wow!!!" 
print (str.isdigit())


str1 = "THIS is string example....wow!!!" 
print (str1.islower()) 
str1 = "this is string example....wow!!!" 
print (str1.islower())


#!/usr/bin/python3 
str = "this2016"   
print (str.isnumeric()) 
str = "23443434"   
print (str.isnumeric())



#!/usr/bin/python3 
str = "       "  
print (str.isspace()) 
str = "This is string example....wow!!!" 
print (str.isspace()) 



#!/usr/bin/python3 
str = "This Is String Example...Wow!!!" 
print (str.istitle()) 
str = "This is string example....wow!!!" 
print (str.istitle()) 



#!/usr/bin/python3 
str = "THIS IS STRING EXAMPLE....WOW!!!" 
print (str.isupper()) 
str = "THIS is string example....wow!!!" 
print (str.isupper())



#!/usr/bin/python3 
s = "-" 
seq = ("a", "b", "c") # This is sequence of strings. 
print (s.join( seq )) 



#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print ("Length of the string: ", len(str)) 







#!/usr/bin/python3 
str = "THIS IS STRING EXAMPLE....WOW!!!" 
print (str.lower()) 



#!/usr/bin/python3 
str = "     this is string example....wow!!!" 
print (str.lstrip()) 
str = "*****this is string example....wow!!!*****" 
print (str.lstrip('*')) 


intab = "aeiou"   
outtab = "12345" 
trantab = str.maketrans(intab, outtab) 
str = "this is string example....wow!!!" 
print (str.translate(trantab))


#!/usr/bin/python3 
str = "this is a string example....really!!!" 
print ("Max character: " + max(str)) 
str = "this is a string example....wow!!!" 
print ("Max character: " + max(str))



#!/usr/bin/python3 
str = "www.tutorialspoint.com" 
print ("Min character: " + min(str)) 
str = "TUTORIALSPOINT" 
print ("Min character: " + min(str)) 




#!/usr/bin/python3 
str = "this is string example....wow!!! this is really string" 
print (str.replace("is", "was")) 
print (str.replace("is", "was", 3))



#!/usr/bin/python3 
str1 = "this is really a string example....wow!!!" 
str2 = "is" 
print (str1.rfind(str2)) 
print (str1.rfind(str2, 0, 10)) 
print (str1.rfind(str2, 10, 0)) 
print (str1.find(str2)) 
print (str1.find(str2, 0, 10)) 
print (str1.find(str2, 10, 0))



#!/usr/bin/python3 
str1 = "this is really a string example....wow!!!" 
str2 = "is" 
print (str1.rindex(str2)) 
print (str1.rindex(str2,10))




#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print (str.rjust(50, '*'))



#!/usr/bin/python3 
str = "     this is string example....wow!!!     " 
print (str.rstrip()) 
str = "*****this is string example....wow!!!*****"    
print (str.rstrip('*'))


#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print (str.split( )) 
print (str.split('i',1)) 
print (str.split('w'))




#!/usr/bin/python3 
str = "this is \nstring example....\nwow!!!" 
print (str.splitlines( )) 





#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print (str.startswith( 'this' )) 
print (str.startswith( 'string', 8 )) 
print (str.startswith( 'this', 2, 4 ))


#!/usr/bin/python3 
str = "*****this is string example....wow!!!*****" 
print (str.strip( '*' ))




#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print (str.swapcase()) 
str = "This Is String Example....WOW!!!" 
print (str.swapcase())



#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print (str.title()) 


#!/usr/bin/python3 
from string import maketrans   # Required to call maketrans function. 
intab = "aeiou" 
outtab = "12345" 
trantab = maketrans(intab, outtab) 
str = "this is string example....wow!!!"; 
print (str.translate(trantab))




#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print ("str.upper : ",str.upper())



#!/usr/bin/python3 
str = "this is string example....wow!!!" 
print ("str.zfill : ",str.zfill(40)) 
print ("str.zfill : ",str.zfill(50)) 


#!/usr/bin/python3 
str1 = "this2016" 
print (str1.isdecimal()) 
str1 = "23443434" 
print (str1.isdecimal()) 






