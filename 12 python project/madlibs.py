# #string concatanation (aka how to put strings together)
# #suppose we want to create a string that says "subscribe to _____________"
# youtuber= "vikas chaudhary" #some string variable

# #a few ways to do this
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj= input("Adjective: ")
verb1=input("verb1: ")
verb2= input("verb2: ")
verb3= input("Verb3: ")

famous_person = input("Famous person: ")
madlib = f"computer programming is so {adj}! it make me so excited all the time because \
i love to {verb1} stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)