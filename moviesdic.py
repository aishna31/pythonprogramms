# movies
movies = [
    {
        "name":"entertainment",
        "year":2010,
        "actors":["akshay","tamnaah","sonu"]
    },
    {
        "name":"ishq",
        "year":2001,
        "actors":["ajay","aamir","kajol"]
    },
    {
        "name":"drishyam",
        "year":2017,
        "actors":["ajay devgan","tabu","aishna vatyani"]
    },
    {
        "name":"freddy",
        "year":2020,
        "actors":["kartik aryan","kirti sanon","alia bhatt"]
    },
    {
        "name":"bhool bhuliya",
        "year":2015,
        "actors":["akshay kumar","vidhya balan","amisha patel"]
    }    
]
for i in range(0,len(movies)):
    a=movies[i]["actors"]
    for j in range(0,len(a)):
         if(a[j]=="akshay kumar"):
             print(movies[i]["name"])
         if(a[j]=="alia bhatt"):
           print(movies[i]["name"])       
