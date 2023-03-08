""" Wow, this is self practice"""
Mixedigalph= "12345WETGS"
result= 0
alphab= " "
for s in Mixedigalph:
    if s.isdigit():
       result+=int(s)

    else:
        alphab +=s
print((result,alphab))
