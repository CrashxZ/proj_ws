import os
import json

with open("localPoseStamped_2.txt", "r") as file:
    pathData = file.readlines()
    
for point in pathData:
    point = eval(point)
    point = {
        "x": point[0],
        "y": point[1],
        "z": point[2]
    }
    with open("coordinates2.json", "a") as file:
        json.dump(point, file)
        file.write("\n")




