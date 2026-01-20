# age ={
#         "name":"adarsh",
#         "age":29, 
#         "add":"indore",
#         "gender":[2,3,4,5,6,[9,7,[33,44,55,66,{"name":"aishna","age":[3,4,5,3]}],6]],
#         "ages":[1,2,3,4,5,[3,4,5,66]]
#     }
# print(age['gender'][5][2][4]["age"][2])

data = [
    {
        "name":"adarsh",
        "age":19
    },
    {
        "name":"aishna",
        "age":23
    },
    {
        "name":"ankit",
        "age":26
    }
]
for i in range(0,len(data)):
    if(data[i]["age"]>20):
        print(data[i]["name"])