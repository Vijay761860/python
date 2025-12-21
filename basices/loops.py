#this is a name list 
list1=["vijay", "ajay","nitin","ritik","pritike"]
list2 =[1,2,3,4,56,7,788,9,9,67,4,35,87,9,456,3,455,7,33]


# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
# [1, 2, 3, 4, 56, 7, 788, 9, 9, 67, 4, 35, 87, 9, 456, 3, 455, 7, 33]
var = 1
while var < len(list2):
    print(list2)
    var +=1


# 7
# 788
# 9
# 3
# 455
# 7
# 33
varr= 0
while varr <len(list2):
    print(list2[varr])

    varr += 1


# ['vijay', 'ajay', 'nitin', 'ritik', 'pritike']
# ['vijay', 'ajay', 'nitin', 'ritik', 'pritike']
# ['vijay', 'ajay', 'nitin', 'ritik', 'pritike']
# ['vijay', 'ajay', 'nitin', 'ritik', 'pritike']
var1 = 1
while var1 < len(list1):
    print(list1)
    var1 +=1


# vijay
# ajay
# nitin
# ritik
# pritike
varr2 =0
while varr2 <len(list1):
    print(list1[varr2])

    varr2 += 1

#number printing sucessfully
i = 1
while i <=5:
    print(i)
    i +=1
else:
    print("Number printing successfully")

# alwase runnign 
# while True:
#     num = int(input("Enter a number and 0 to exit : "))

#     if num == 0:
#         break

password = ""

while password != "admin":
    password = input("Enter password: ")
print("Access granted")


passe =""
while passe != "admin":
    passe = input("Enter a pssowd")
print("Access granted")