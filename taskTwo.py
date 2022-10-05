while True:
  try:
    usernum = int(input("Enter a number to count to: "))
    if usernum <= 0 :
      raise("number too low error")
    break

  except:
    print("Invalid value entered")

for i in range(usernum+1):
  if i % 2 != 0:
    print(i)
