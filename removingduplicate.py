
movies = [
    {
        "name":"entertainment",
        "year":2010,
        "actors":["akshay","tamnaah"]
    },
    {
        "name":"ishq",
        "year":2001,
        "actors":["ajay","aamir"]
    },
    {
        "name":"drishyam",
        "year":2017,
        "actors":["ajay","tabu"]
    },
    {
        "name":"freddy",
        "year":2020,
        "actors":["kartik aryan","kirti sanon"]
    },
    {
        "name":"bhool bhuliya",
        "year":2015,
        "actors":["akshay","vidhya balan"]
    }    
]
y=[]
for i in range(0,len(movies)):
    a=movies[i]["actors"]
    for j in range(0,len(a)):
        if(a[j]=="akshay"):
            b=movies[i]
            y.append(b)
movies.remove(y[0])
movies.remove(y[1])
print(movies)
            
        
        

            
            
            
