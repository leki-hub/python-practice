def even_numbers():
    num = 0
    while num < 10:
        yield num
        num += 2
gen = even_numbers()
try:
    while True:
        print(next(gen))
except StopIteration:
    print("Sequence ended.")
"""or""" 
for i in gen:
        print(i)
