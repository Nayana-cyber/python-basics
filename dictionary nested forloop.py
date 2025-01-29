


myfamily = {
    "child1 ": {
        "name" : "Emil",
        "year" : 2004
    },

    "child2" : {
        "name" : "nayana",
        "year" : 2002
    },

    "child3" : {
        "name" : "karthika",
        "year" : 2003
    }
}


for x , obj in myfamily.items():
    print(x)

    for y in obj :
        print(y + ':' , obj [y])