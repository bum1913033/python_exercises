# create given list of dictionaries
given = [{"name":"Stephan", "age":21},
         {"name":"Selina", "age":20},
         {"name":"Linard", "age":27},
         {"name":"Kian", "age":33}]

# create empty list variables to represent the ranges
range1 = []
range2 = []
range3 = []

# iterate over each element (dict) in given list
for element in given:
    # if dictionary["age"] is in this range add to new list variable (range1, range2, range3)
    if element["age"] >= 20 and element["age"] < 25:
        range1.append(element["name"])
    elif element["age"] >= 25 and element["age"] < 30:
        range2.append(element["name"])
    elif element["age"] >= 30 and element["age"] <=35:
        range3.append(element["name"])

# print range and result
print("20 - 25", range1)
print("25 - 30", range2)
print("30 - 35", range3)
        
