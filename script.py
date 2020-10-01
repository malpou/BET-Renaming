from os.path import isfile, join
from os import listdir
import os

number = 690
counter = 1
mypath = "C:/Users/malth/Desktop/Files/"
outpath = "C:/Users/malth/Desktop/Output/"
nextLetter = ""

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in files:
    if ".txt" in file:
        nextLetter = "A"
        os.rename(mypath + file,
                  f"{outpath}Leg_{number}.txt")
    else:
        if "A" in nextLetter:
            nextLetter = "B"
            letter = "A"
        elif "B" in nextLetter:
            nextLetter = "C"
            letter = "B"
        else:
            letter = "C"
        os.rename(mypath + file,
                  f"{outpath}Leg_{number}_{letter}.png")
    if counter % 4 == 0:
        number = number + 1
    counter += 1
