from PIL import Image, ImageChops
import os
import math

streamName = input('Enter stream name: ')
directory = 'images/' + streamName + '/'
counter=0
arr = [None] * len(os.listdir(directory))
for filename in os.listdir(directory):
    arr[counter] = Image.open(directory + filename)
    counter+=1

dataFile = open(streamName + '_data_file.txt', 'w')

# get average difference over time between each year
totalDiff=0
for image in range(len(arr) - 1):
    imageDiff = ImageChops.difference(arr[image], arr[image+5])
    rect = imageDiff.getbbox()
    print(imageDiff.getbbox())
    totalDiff += math.hypot(rect[0] - rect[2], rect[1] - rect[3]) # adding abs hypot distance
totalDiff /= len(arr)

dataFile.print(totalDiff)