# import re
# """1 search functio """
# # match any three-digit number
# pattern = r"\d{3}"
# text = "The zip code of New York 2 is 130  0 e0e01"

# match = re.search(pattern, text)
# print(match.group)  # output: 100
# """2 findall function"""
# import re

# # find all email addresses in a string
# pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{1,}\b"
# text = "Contact us at info@example.com or support@example.org or supportk-@example.org"

# matches = re.findall(pattern, text)
# print(matches)  # output: ['info@example.com', 'support@example.org' or supportk-@example.org]


# import re

# # This method splits the string at every occurrence of the pattern and returns a list of substrings
# pattern = r"Python"
# text = "I love Python programming"

# new_text = re.sub(pattern, "Java", text)
# print(new_text)  # output: "I love Java programming"

# import re

# pattern = r"[,\s]+"
# text = "apple,banana, cherry  orange"

# words = re.split(pattern, text)
# print(words)  # output: ['apple', 'banana', 'cherry', 'orange']


import re

# # # This method compiles the pattern into a regular expression object that can be reused multiple times.
pattern = r"\d{2}"
text1 = "There are 10 cats and r3070 dogs and 300 hares"
text2 = "The price is $15.99"

regex =re.compile(pattern)
matches1 = regex.findall(text1)
matches2 = regex.findall(text2)
print(matches1)  # output: ['10', '20']
print(matches2)  # output: ['10', '99']
import re

pattern = r"^hello"
text = "hello, world!\nhello, everyone!"

matches = re.findall(pattern, text, flags=re.MULTILINE)
print(matches)
import re

pattern = r"hello"
text = "Hello, kello world!"

satch = re.search(pattern, text, flags=re.IGNORECASE)
if satch:
  print(" dd" ,satch)
else:
  print("not available")
 #Example
import re
s=input("Enter pattern to check: ")
m=re.match(s, "abcabdefg")
if m:
   print("Match is available at the beginning of the String")
   print("Start Index:", m.start(), "and End Index:", m.end())
else:
   print("Match is not available at the beginning of the String")

import re
matcher=re.finditer("a{2,3}","abaabaaaba")
for match in matcher:
   print(match.start(),"......",match.group())

import re
matcher=re.finditer("a+","abaabaaab")
for match in matcher:
   print(match.start(),"......",match.group())