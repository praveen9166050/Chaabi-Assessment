# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the lists.

def commonAndNotCommon(Mainstream, mustWatch):
    MainstreamSet = set(Mainstream)
    mustWatchSet = set(mustWatch)
    common = MainstreamSet.intersection(mustWatchSet)
    notCommon = MainstreamSet.symmetric_difference(mustWatchSet)
    return list(common), list(notCommon)

Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
mustWatch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common, notCommon = commonAndNotCommon(Mainstream, mustWatch)
print(common)
print(notCommon)