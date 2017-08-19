
# import classes and functions 

from keras.models import Sequential 
from keras.layers.core import Dense, Activation
from keras.utils import np_utils
from PIL import Image
import matplotlib.pyplot as plot
import os,sys
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

 
# Training Data
pathTrainDataCar = 'TrainImages/car/'
pathTrainDataBuilding = 'TrainImages/building/'
pathTrainDataRoad = 'TrainImages/road/'
pathTestData = 'TrainImages/validation/'

pathResizedTrainDataCar = 'ResizeTrainImages/car/'
pathResizedTrainDataBuilding = 'ResizeTrainImages/building/'
pathResizedTrainDataRoad = 'ResizeTrainImages/road/'
pathResizedTestData = 'ResizeTrainImages/validation/'

# Resize the images 
row,column = 100,100

listingCar = os.listdir(pathTrainDataCar)
print(listingCar)
for file in listingCar:
	img = Image.open(pathTrainDataCar + file)
	resizeImg = img.resize((row,column))
	gray = resizeImg.convert('L')
	gray.save(pathResizedTrainDataCar + file)


listingBuilding = os.listdir(pathTrainDataBuilding)
print(listingBuilding)
for file in listingBuilding:
	img = Image.open(pathTrainDataBuilding + file)
	resizeImg = img.resize((row,column))
	gray = resizeImg.convert('L')
	gray.save(pathResizedTrainDataBuilding + file)


listingRoad = os.listdir(pathTrainDataRoad)
print(listingRoad)
for file in listingRoad:
	img = Image.open(pathTrainDataRoad + file)
	resizeImg = img.resize((row,column))
	gray = resizeImg.convert('L')
	gray.save(pathResizedTrainDataRoad + file)


listingTestData = os.listdir(pathTestData)
print(listingTestData)
for file in listingTestData:
	img = Image.open(pathTestData+file)
	resizeImage = img.resize((row,column))
	gray = resizeImage.convert('L')
	gray.save(pathResizedTestData+file)


