sap= " 12456ABDE"
""" Create a program that will add int values and concartanates alphabets contained in the above variable"""
def add_conc(sap):
      result= 0
      alphabet= " "
      for item in sap:
        if item.isdigit():
            result +=int(item)
        else:
            alphabet+= item
            
      return(result, alphabet)
print(add_conc(sap))
"""The above without a function can be as belw, but print is possible and not return unless we want to use a function"""
sap= "12456ABDE"

result= 0 #initialization
alphabet= " " #An empty string, 
for item in sap:
        if item.isdigit():
            result +=int(item)
        else:
            alphabet+= item
            
print([result,alphabet])