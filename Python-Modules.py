import datetime as dt
print(dt.datetime.now())  # print time now with all details
print(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day)  # print year and month and day
print(dt.datetime.max, dt.datetime.min)  # print the maximum calendar and minimum one
print(dt.datetime.now().time())  # print time hours second minutes and millisecond
print(dt.datetime(year=2002, month=12, day=12))  # print specific date
print(dt.datetime(year=2002, month=12, day=12).strftime("%d/%B/%A/%a and etc"))  # return string format from the time
# here all time formats you can choose https://strftime.org/
#-----------------------------------------------------------------------------------------------------------------------
from pytube import YouTube
link = str(input("Your link : "))  # to put your link
video = YouTube(link)  # putting your link in yotube
print(f"Your video name is {video.title}")  # to return title name
stream = video.streams.filter(progressive=True).get_highest_resolution()  # to get the highest resolution with "sound" ,
# if you want just Hd without sound make progressive false
stream.download("mp4")  # to download video into path called MP4 "you can change the name"
print("Video Downloading :)")  # gonna be printed after the video downloaded into the directory
#-----------------------------------------------------------------------------------------------------------------------
# spam chat programme ;)
import pyautogui as pa
import pyperclip as pc
import time
time.sleep(2)
while True:
    #if the text is arabic use this method or any language
    pc.copy("your text if it's another language")
    pa.hotkey("ctrl", "v")
    pa.press("enter")
    #if it's english use this method
    pa.typewrite("your text")
    pa.press("enter")
#-----------------------------------------------------------------------------------------------------------------------
import numpy as np
#numpy is the greatest module for data scientist for matrices operatios
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
np_list1 = np.array(list1)
np_list2 = np.array(list2)
print(np_list1) # now you created Numpy list !
# by this way you can add 2 arrays as matrices , or multiply or etc , remember FLASE = 0 , TRUE = 1
#now let's make 2d array :
list3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
np_list3 = np.array(list3)
print(np_list3) # now you have 2d Array
print(np_list3.shape) #will print the dimensions of it "3x3"
print(np_list3[:,0])#to access all rows and choose specific columns "[:,0] = all rows and will return first column]
# ":" here means all rows or all columns
#here's impressive statistican built-in Functions !!
print(np.mean(np_list3)) # will return the mean
print(np.median(np_list3)) # will return the median
print(np.std(np_list3)) # will return the standard deviation
print(np.corrcoef(np_list3[:,0],np_list3[:,1])) # will return the correlation between the first and second columns
# here's some comparison tools
# np.logical_or("list1","list2") , np.logical_and("list1","list2") , np.logical_xor("list1","list2") , np.logical_not("list1","list2")
# you can use for loop to print items in the array
np_array_doubled = np.array([np_list1,np_list2])
for item in np_array_doubled : print(item) #in one line
for item in np.nditer(np_array_doubled) : print(item) #now will print first list items then second one
# -----------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot.
# let's make your first plot!
list1 = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961,2002]  # let this your first x-axis
list2 = [2.53, 2.57, 2.62, 2.67, 2.71, 2.76, 2.81, 2.86, 2.92, 2.97, 3.03, 3.08,3,10]  # let this your first y-axis
plt.plot(list1, list2)  # First place for x and second for y, now will put your axis into the plot to draw it
plt.show()
plt.clf()  # clf() function in pyplot module of matplotlib library is used to clear the current figure
plt.xlabel('x-axis')  # to put name for x
plt.ylabel('y-axis')  # to put name for y
plt.title("FIRST PLOT")  # to put title for the plot
plt.show()
plt.yticks([0, 2, 4, 6, 8, 10],
           ["0", "2B", "4B", "6B", "8B", "10B"])  # here you changed from 0 1 2 3 to 0 2 4 6 way in y axis
# and put name for each one of it
plt.show()
plt.xscale('log')  # now you changed the format of x from number into log scale
plt.show()  # here will print your and show your plot!
# let's try another way of plots!
plt.scatter(x=list1, y= list2, s=5, alpha=0.5, c="black")
# it will display as dots "scatter plot" ! , and s tends to size of dots
# and c tends to the color , and you can make dictionary have colors and put it into the c
# and to change opacity we use alpha = "from 0 to 1"
plt.gird(True) # to enable grids in the plot
plt.text(x=2002, y=3.10) # you will put x dimension and then y dimension and then the name of this place
plt.show()  # here will print your and show your plot!
# let's try another way of plots!
plt.hist(x=list1, bins=10)  # it will display histogram shape , just put your data and Python will set the number of bin
# to 10 by default for you , Bins in general here to divide your data
plt.show()  # here will print your and show your plot!
#-----------------------------------------------------------------------------------------------------------------------
# PANDAS! why should you know about pandas ? so Pandas is an open source library, providing high-performance,
# easy-to-use data structures and data analysis tools for Python it's High level manipulating data tool , for sad numpy
# can't accept varies
# in data types , so pandas come to fix it! , it's like data frame in R anyway
# You can use dictionary to connect it as data frame in pandas , as Key is the column label and values is data column
# by column
# Let's see example for Pandas
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] # list about countries names
dr =  [True, False, False, False, True, True, True] # for driving license
cpc = [809, 731, 588, 18, 200, 70, 45] # car for cap
my_dict = {'Country':names,'drives_right': dr, 'cars_per_cap': cpc} # dictionary to put our data
#REMEMBER! key is the column label and it's values is the rows
cars = pd.DataFrame(my_dict) # creating data frame
print(cars) # executed example for pandas data frame!
# if you want to change the indexes from 0 1 2 ... to something else , do this trick!
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index=row_labels
print(cars) # WOW IT HAS CHANGED !
# now let's try to import csv to pandas , to import with pandas we use the method pd.read_csv()
database = pd.read_csv('FILE.xlsx')
cars = pd.DataFrame(database,index_col=0,chunk=0) # to remove indexes in first columns from excel
# and chunk for number of rows you will extract from excel
print(cars) # and here you have done it!
#The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame
#you can access this data by using normal slice, for columns : "cars["Column"], for rows : cars[0:1]
#IN DATA FRAME : by using pandas method 1 "loc" "it's using string" we can use cars.loc["row name"] or cars.loc[:,["column1,column2]]
#IN DATA FRAME : by using pandas methos 2 "iloc""it's using integer" we can use cars.iloc[row number] or cars.iloc[["the number of row"],["the number of column]]
#you can use Numpy operator logical in pandas too
#to make filter comparison also you can do this syntax : cars[car>18]
#this way to add column : cars["Name of the column"] = the items you want to add in the column
#Using for loop with pandas example : for label,row in cars.iterrows() : print(label,row) : iter row = iterate the rows
# for lab, row in car.iterrows() :
#     car.loc[number of row, "name of column"] = the method you will apply to make it equal to
#     "THIS WAY USED TO ADD NEW COLUMN TO THE DATA FRAME WITH "iterrow"
# and you can change format of data from CSV to EXCEL with pandas with this code :
import pandas as pd
from openpyxl.workbook import Workbook
read_file = pd.read_csv(r'The file path file.csv')
read_file.to_excel(r'where to put your file.xlsx', index=None, header=True)
#-----------------------------------------------------------------------------------------------------------------------
#SOME STATISTICIAN TRICKS
#With numpy we can generate a random number of possible answer "probability"
#seed(): sets the random seed, so that your results are reproducible between simulations.
#As an argument, it takes an integer of your choosing. If you call the function, no output will be generated
#rand(): if you don't specify any arguments, it generates a random float between zero and one.
#randint() : return random int
#EXAMPLE FOR DICE CODE : import numpy as np;np.random.seed(123);print(np.random.randint(1,7))
#-----------------------------------------------------------------------------------------------------------------------
#Pillow for image manipulation
from PIL import Image as pi
# To open image
myImage = pi.open("Your image path")
# To show it
myImage.show()
# To crop photo you should init your positions
myBox = ("left","upper","right","lower")
MyNewImage = myImage.crop(box=myBox)
# To change mode of photo "filters"
print(myImage.convert("L")) # to make it grey
# To continue accessing in picture manipulation see this link : https://pillow.readthedocs.io/en/stable/
#-----------------------------------------------------------------------------------------------------------------------
#Pyplint for rating your code style
# First you have to download it by using python terminal, so first write : py -m pip install pylint
# to use it does the next syntax, and it will rate your code and if there's something bad it will notice it and will tell u
# The Syntax in terminal is : py -m pylint file.py
# will give you error codes like name and the formality of the code till you gain 10/10 rating
#-----------------------------------------------------------------------------------------------------------------------
# here will discuss SQL with python "DATA BASE"
# to import sql in python will use the next syntax
import sqlite3
db = sqlite3.connect("Example.db")  # to create database and connect to it
db.execute("CREATE TABLE if not exists 'person' (name text,age integer,user_id integer)")  # create the table and fields
Cursor = db.cursor() # to create cursor
#Cursor : will handle all operations with sql
#you can create table as use as execute data
#INSERTING DATA INTO DATABASE :
Cursor.execute("INSERT INTO 'person' (name,age,user_id) VALUES ('mahmoud',20,1)")
#UPDATE DATA INTO DATABASE :
Cursor.execute("UPDATE person set name = 'name1' where name = 'name2' ")
#DELETE DATA FROM DATABASE
Cursor.execute("DELETE from person where name = 'your name'")
#RETURN DATA FROM DATABASE
Cursor.fetchone() #will return single row of the database "like next in iterable" till return none
Cursor.fetchall() #will return all rows of the database as list of tuples
Cursor.fetchmany("specific number of rows you want") #will return specific number of rows from the database
#COMMIT THE ORDER AND CLOSE IT
db.commit() #to do the order and save it into the database
db.close() # to close the DataBase
