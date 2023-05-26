# Q2. Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.

def function(typesString, files):
    types = dict(map(lambda x: x.split(','), typesString.split(';')))
    res = {}
    for file in files:
        ext = file.split('.')[-1]
        if (ext in types):
            type = types[ext]
        else:
            type = "unknown"
        res[file] = type
    return res

typesString = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
files = ["abc.jpg", "xyz.xls", "text.csv", "123"]

print(function(typesString, files))