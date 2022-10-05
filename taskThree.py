vowels = ["a", "e", "i", "o", "u"]
vowelCount = 0
vowelList = ""
while True:
  try:
    userstring = list(input("Please enter a sentence: "))
    break
  except:
    print("Invalid value entered\n\n")

for i in userstring:
  if i in vowels:
    vowelCount += 1
    vowelList += i

print("There were", vowelCount, "vowels in that sentence!")
print("The vowels were in order:", vowelList)
