##Writer a program to read one subject mark and print pass or fail ie use single return

def result(a):
 if a>40:
  return f"{a}"," Pass"
 else:
  return "fail"
a=int(input("Enter one subject marks : "))
print( "Your perfrmance is", result(a))
