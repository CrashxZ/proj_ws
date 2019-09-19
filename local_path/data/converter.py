import os
import json
#reads data from the specifyed file
with open("localPoseStamped_2.txt", "r") as file:
    pathData = file.readlines()
#convert into json array
for point in pathData:
    point = eval(point)
    point = {
        "x": point[0],
        "y": point[1],
        "z": point[2]
    }
    #dump json array in file
    with open("coordinates2.json", "a") as file:
        json.dump(point, file)
        file.write("\n")




