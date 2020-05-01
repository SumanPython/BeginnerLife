fruits = {"bananas" : 12,
          "mangoes" : 1,
          "pineapple" : 3}
print(fruits)
print(fruits["pineapple"])
print(fruits["bananas"])
print(fruits.get("bananas"))
contacts = {"Suman" : [36, "122345", "shilpa@gmail.com"],
            "Chandana" : [34, "1234567", "chandana@hotmail.com"],
            "Shilpa" : [35, "1123453", "shilps@gmail.com"]
            }
print(contacts["Shilpa"])
contacts1 = {"suman" : {"Name" : "Suman Palisetty",
                        "age": 36,
                        "phone" : "123344552",
                        "email" : "spalisetty@gmail.com"},
             "shilpa" : {"Name" : "Shilpa Balla",
                                   "age" : 35,
                         "phone" : "123345643",
                         "email" : "1342123322"}}
print(contacts1)
print(contacts1["suman"])
print(50 * "%")
print(contacts1.items())
print(list(contacts1.items()))
print(contacts1.keys())
print(list(contacts1.keys()))
print(contacts1.values())
print(list(contacts1.values()))
print(contacts)
print(50 * "%")
print(contacts.pop("Suman"))
print(50 * "$")
print(contacts)
print(50 * "#")
contacts.update({"Suman" : '[37, "1356647456", "spalisetty@gmail.com"]'})
print(contacts)
contacts.popitem()
print(contacts)
print(50 * ".")
print(sorted(list(contacts1.values())))



