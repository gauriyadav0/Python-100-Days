# Strings are immutable
original_sentence = "!!!John!! !!!!!!!!! John"
print(len(original_sentence))
print(original_sentence)
print(original_sentence.upper())
print(original_sentence.lower())
print(original_sentence.rstrip("!"))
print(original_sentence.replace("John", "Alice"))
print(original_sentence.split(" "))
blog_title = "introduction to Python"
print(blog_title.capitalize())

string1 = "Hello, welcome to the Console!!!"
print(len(string1))
print(len(string1.center(50)))
print(original_sentence.count("John"))

string1 = "Hello, welcome to the Console !!!"
print(string1.endswith("!!!"))

string1 = "Hello, welcome to the Console !!!"
print(string1.endswith("to", 4, 10))

string1 = "Her name is Alice. She is a software engineer."
print(string1.find("Alice"))
# print(string1.index("ishh"))

string1 = "WelcomeToTheConsole"
print(string1.isalnum())
string2 = "Welcome"
print(string2.isalpha())

string1 = "hello world"
print(string1.islower())

string1 = "We wish you a Merry Christmas\n"
print(string1.isprintable())
string1 = "         "       #using Spacebar
print(string1.isspace())
string2 = "  "       #using Tab
print(string2.isspace())

string1 = "World Health Organization"
print(string1.istitle())

string2 = "To kill a Mocking bird"
print(string2.istitle())

string1 = "Python is an Interpreted Language"
print(string1.startswith("Python"))

string1 = "Python is an Interpreted Language"
print(string1.swapcase())

string1 = "Her name is Alice. Alice is a software engineer."
print(string1.title())
