import re

x = 'My Email address is topebali97@gmail.com. Email me ty32@yahoo.com'
y = re.findall(r'(\S+@\S+)',x)
print (y)

#extracts only gmail
z = 'My Email address is topebali97@gmail.com. Email me ty32@yahoo.com'
b = re.findall(r'(\S+@gmail\S+)',z)
print (b)

#extracts only yahoomail
z = 'My Email address is topebali97@gmail.com. Email me ty32@yahoo.com'
b = re.findall(r'(\S+@yahoo\S+)',z)
print (b)

