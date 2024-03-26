#Dictionaries

#The dict() class
my_values = dict()
person = {
    "name" : "Dan",
    "school" : "Zindua School",
    "hobbies" : ["BasketBall", "Swimming", "Football"],
    "age" : 50,
    "isActive" : True,
    "isPresent" : False,
    "other_values" : {
        "personalities" : None,
    }
}

person["name"] = "Walobwa"
person["age"] +=1

print(person)