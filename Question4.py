# Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.

def switchKeysAndValues(dict):
    return {key: value for (value, key) in dict.items()}

dict = {
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}

print(switchKeysAndValues(dict))