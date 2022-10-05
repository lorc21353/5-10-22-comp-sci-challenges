length = 10
def whileprint():
  global length 
  i = 0
  while i < length:
    i += 1
    print(i)

def forprint():
  global length
  for i in range(length):
    i += 1
    print(i)

try:
  tempchoice = int(input("enter 1 for 1-10 with a while loop or 2 for 1-10 with a for loop: "))
  print("\n\n")
  if tempchoice == 1:
    whileprint()
  elif tempchoice == 2:
    forprint()

except:
  print("invalid value entered")
