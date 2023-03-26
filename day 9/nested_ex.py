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
#funtion that add the new counter to travel vlog
def add_new_country(country_visited,cities,visit):
    new_country={}
    new_country["country"]=country_visited
    new_country["cities_visied"]=cities
    new_country["total_visit"]=visit
    travel_vlog.append(new_country)
    
    
#adding a new country
add_new_country("Taiwan",["taipei","taichung","tainan"],2)
print(travel_vlog)