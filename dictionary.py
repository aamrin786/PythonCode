myDict={
    "1":"one",
    "2":"two",
    "3":"three",
}
print(myDict)
#to update the dictionary
updateDict={"4":"Four","1":"One"}
myDict.update(updateDict)
print(myDict)
print(myDict.get("1"))