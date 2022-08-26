programming_dictionary = {
    "Bug" : "An error in the program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again", 
    "Loop" : "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

#creating an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit an item in a dicitonary
programming_dictionary["Bug"] = "Test"
print(programming_dictionary)

#loop through a dictionary
# for thing in programming_dictionary:
#     #only prints the key, not the value in the key
#     print(thing)
#     #to get value in key
#     print(programming_dictionary[thing])

#cleaned up
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])