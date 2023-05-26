# Q3. Given a list of dicts, write a program to sort the list according to a key given in input.

def sortListOfDicts(list, key):
    list.sort(key = lambda x: x[key])
    return list

list = [
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
]

print(sortListOfDicts(list, "fruit"))