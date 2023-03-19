# ShapeName = input("Enter the shape you want to calculate area of: ")
# Deminsion=int(input("Enter the value of Dimension "))
# area = 0
#
#
# if ShapeName == "Rectangle":
#
#     width = int(input("Enter the value of length: "))
#
# elif ShapeName == "Triangle":
#     height = int(input("Enter the value of height: "))
#
#
# def areacalculator(ShapeName,demension):
#     _input_=ShapeName
#
#     area = 0
#     pie = 3.14
#
#     if _input_ == "Square":
#
#         area = area + (demension ** 2)
#     elif _input_ == "Circle":
#
#         area = area + (2 * pie * demension)
#     elif _input_ == "Rectangle":
#
#
#         area = area + (demension * width)
#     elif _input_ == "Triangle":
#
#         area = area +(0.5 * demension * height)
#     else:
#         print ("Select a valid shape")
#     print ("Area is : "+"%.2f" % area)
#
# areacalculator(ShapeName,Deminsion)

# 2
# string = input("please enter a statement")
# ch=input("Enter the character")
# print("Duplicate characters in a given string: ");
# if ch in string:
#     print([index for index, character in enumerate(string) if character == ch])


# #3
# num=int(input("please enter a num"))
#
# list = []
# newlist=[]
#
# for i in range(1,num+1):
#      newlist = []
#     for j in range(1, i + 1):
#         newlist.append(j*i)
#     list.append(newlist)
# print(list)


# 4
statemanet=input("enter your list")
statemanet=statemanet.replace('[','').replace(']','').replace('"','').split(',')
print(" Input List",statemanet)
Dictionary={}
for i in range(len(statemanet)):
    d={statemanet[i][0]:statemanet[i]}
    Dictionary.update(d)
print("Dictionary :",Dictionary)
# ["ahmed","fatma","Ibrahim"]