#list uses square braces [] and dictionary uses curly braces {}
capital={
    #"key":"value"
    "Nepal":"Kathmandu",
    "S.Korea":"Seoul",
    "Japna":"Tokyo",
    "China":"Bejing",
}
#nesting a dictionARY in a dictionary
travel_vlog={
    "Nepal":{"cities_visted":["mustang","pokhara","nala","banepa","lubhu"],"total_visit":6}, 
    "S.Kora":{"cities_visited":["seoul","jeju","ilsan","busan"],"total_visit":5},
    "Japan":{"cities_visited":["tokyo","hakaido","osaka"],"total_visit":4},
    "China":{"cities_visited":["bejing","shanghai","senai"],"total_visit":8},
}
#nesting a dictionary in a list
travel_vlog=[
    {
        "country":"Nepal",
        "cities_visted":["mustang","pokhara","nala","banepa","lubhu"],#list
        "total_visit":6
    }, 
   
    {
        "country":"S.Korea",
        "cities_visited":["seoul","jeju","ilsan","busan"],
        "total_visit":5
    },
    
    {
        "country":"Japan",
        "cities_visited":["tokyo","hakaido","osaka"],
        "total_visit":4
    },
    
    {
        "country":"China",
        "cities_visited":["bejing","shanghai","senai"],
        "total_visit":8
    },
    
]
