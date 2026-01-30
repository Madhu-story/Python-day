info = {
    "key" : "value",
    "name" : "Madhura",
    "age" : 35,
    "is_adult" : True,
    "cgpa" : 8.9,
    "subjects" : ["Python", "Java", "C"],
    "topics" : ("list", "tuple", "dictionary", "set")
}

info["surname"] = "Sajjan"
info["name"] = "Nagaraj"
print(info)

nul_dict = {}
nul_dict["name"] = "Madhura"
print(nul_dict)

student = {
    "name" : "Akshay Kumar",
    "score" : {
        "phys" : 98,
        "chem" : 97,
        "math" : 96
    }

}

print(student["score"]["chem"])
print(len(info))
print(student.keys())
print(list(student.values()))
pairs = list(student.items())
print(pairs[1])

print(student["name"])  # gives error if given key name is not matching to key in dictionary
print(student.get("names"))  # gives None and next lines of code will excute

print("Welcome, ")
print("We are learning")
print("Coding")

student.update({"city":"Delhi"})
new_dict = student.update({"age":18})
print(student)
