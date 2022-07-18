#Raw binary data immutable 

text = b'data of some strings '
print(text)

print (text[0])

print(text.split())


#converting
textPolish = "Jakiś tam polski ól z błędami"
print(textPolish)
data = textPolish.encode('utf8')

print(data)

poPolsku = data.decode('utf')

print(poPolsku == textPolish)
print (poPolsku)