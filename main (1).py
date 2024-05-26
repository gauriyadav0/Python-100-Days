# Iterating over a string
name = 'Yash'
for i in name:
  print(i)
  if(i == "a"):
    print(i, "is a vowel")

# Iterating over a list
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

# Range():
for k in range(12):
  print(k+1)

for k in range(1, 12):
  print(k)

for k in range(1, 12, 3):
  print(k)