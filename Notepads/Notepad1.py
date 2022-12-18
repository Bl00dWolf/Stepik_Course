b = b"Lets grab a \xf0\x9f\x8d\x95!"
# Let's check the type
type(b)


# Now, let's decode/convert them into a string
s = b.decode('UTF-8')
print(s)