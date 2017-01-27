#Test Program By Earl
print("Hello World")
a = 99 # Start with the usual number of bottles

# What do we want to say
s = "{0} bottles on the wall. {0} bottles. Take one down, now there are only {1} bottles left"
print(s.format(a, a-1))
a = 98  # Now say it with a few different numbers to start with
print(s.format(a, a-1))
a = 97
print(s.format(a, a-1))

user = input("Please tell me your first name: ")

print("Hello, {0}. You are looking quite frisky today!".format(user))

print("Good bye!")