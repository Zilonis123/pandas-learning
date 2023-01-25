import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"]) # if no index provided pd will display it 0,1,2 ...

# print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
analyzed = pd.Series(calories, index=["day1", "day2"]) # if dict provided it will use the key values instead of 0,1,2...
# if the length of index is less than "calories" then it will only display the lenght of the index
print(analyzed)