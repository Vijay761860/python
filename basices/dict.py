
#this is a dictrory and method
dict1= {
    "name": "vijay",
    "age": 21,
    "fee": 15000,
    "yesrs":{
        "first_yesr": "coding",
        "secoud_year": "placement"
    },
    "subject":["java","c","python","rust","networking","Math", "Science", "English"]
}


#new dict creating for updating 
dict2 ={
    "name": "ritu",
    "age": 20,
    "fee": 1500,
    "streame": "mba",
    "yesrs":{
        "first_yesr": "medical",
        "secoud_year": "placement"
    },

}
dict1["name"]=["ajay"] #overwirting a value
dict1["name"]="deepak" #overwriting value
print(dict1.keys()) #all keys print
print()

print(dict1.values()) #print all values
print(type(dict1.values()))#print all values
print(len(dict1.values())) # lenght print
print(list(dict1.values())) #conver a list usign list method 
print()


print(dict1.items()) # al items as a tuple
print()

print(dict1.get("name"))

print(dict1)


#updating a dict1 to dict2
newdic = dict.update(dict2)
print(newdic)

