person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print()

# print out the name of the second child
print(person["children"][1])
print()

# print out the name of the cat
print(person["pets"]["cat"])
print()

# iterate through all children and print out each child
for k in person["children"]:
    print(k)
print()
    

# print out the pets in this format:
# type of pet: dog name of pet: Fido

for k, v in person["pets"].items():
    print(f"type of pet: {k} name of pet: {v}")
print()