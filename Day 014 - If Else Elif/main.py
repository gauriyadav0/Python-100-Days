# If-else statement
a = int(input("Enter your age: "))
print("Your age is:", a)
if(a<18):
  print("You can't drive")
else:
  print("You can drive")

# Elif statement
num = int(input("Enter the value of num: "))
if(num<0):
  print("num is negative")
elif(num==0):
  print("num is zero")
else:
  print("num is positive")