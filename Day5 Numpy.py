# Databricks notebook source
print ("Hello World")

# COMMAND ----------

import numpy as np

# COMMAND ----------

my1dArray = np.array([1,2,3])
my2dArray = np.array((([[1,2,3], [4,5,6]])), dtype = float)

charrArray1 = np.array([(1, 'a', 3.), (4,5,'zzz')], dtype="U21")
print(charArray1)

# COMMAND ----------

rows = 4
cols = 3

array1s = np.ones((rows, cols))

array5 = 5*np.ones((rows, cols)) #multiplies data by 5

array7s = np.full((rows, cols), 7) #inputs 7 as data

print(array1s)
print(array5)
print(array7s)

# COMMAND ----------

samples = 3
step = 3
start = 10
stop = 25


np.arange(start, stop, step)

np.linspace(start, stop, step)

np.eye(3)

np.random.random((2,3))

np.random.randint(0,10, (3,3))

# COMMAND ----------

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a.ndim
a.shape
a.size
a.dtype

a[a < 9]
np.diag(a)

# COMMAND ----------

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[9,8,7], [6,5,4]])

summ1 = a.sum()
summ2 = np.sum(a)

a+b
a-b
a*b
a/b
np.exp (a)
np.sqrt(a)
np.sin(a)
np.cos(a)
np.log(a)


# COMMAND ----------

# (0,3)
# (0,0)

A = np.array([0,0])
b = np.array([0,3])
c = np.array([1.5,0])

from numpy import linalg as la

AB2 = la.norm(a-b)
AC2 = la.norm(a-c)
BC2 = la.norm(b-c)

print(bc2,bc)


# COMMAND ----------

import numpy as np
#import pyspark as ps

#use spark to read the txt files as a csv
dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")
# collect all the data and store it as a np array
dataRaw = np.array(dataRaw.select("*").collect())

#sepertate data from columns
header = dataRaw[0,:]

# select all rows except the first, all columns except the 4th
data = dataRaw[1:, :4]

#convert data from string to float32
data = np.vstack(data.astype(np.float32))

#select the labels column
labels = np.vstack(dataRaw[1:, 4].astype(np.int32))

#make an array of unique labels, and the number of labels total
labelsUn, labelsCounts = np.unique(labels, return_counts = 1)

# This shows we have 3 different flowers in our dataset, with 50 samples each
display(labelsUn, labelsCounts)


# COMMAND ----------

# Find average, maximum, minimum and stand devisation of each column per category

#number of rows (observtions) and columns (attributes or features) of our data
nrows, ncols= np.shape(data) # >150, 4
# number of unique categories
nclasses = len(labelsUn) # >3
#Initialise empty dfs into which we will update our statistics 
average = np.zeros((nclasses, ncols))
maxi = np.zeros((nclasses, ncols)) 
mini= np.zeros((nclasses, ncols)) 
sd = np.zeros((nclasses,ncols))


for i in labelsUn: #> [1,2,3]
    #Select indices of where in df matches current label
    indexes = np.reshape(labels==i, nrows)
    #Push into empty arrays the caclulated mean, max, min, and standardDeviation 
    average[i-1,] = np.mean (data[indexes, :],axis=0)
    maxi[i-1] = np.max(data[indexes, :],axis=0) 
    mini[i-1] = np.min(data[indexes, :], axis=0) 
    sd[i-1] = np. std (data[indexes, :],axis=0)
    
    
print (header) 
print("averages")
print (average) 
print("maximum") 
print (maxi) 
print("minimum") 
print (mini)
print("standard deviation")
print(sd)

# COMMAND ----------

#More optimal ways are available but let's do it with nested for loops for revision

# Make empty array to store outliers
outliers2sd = np.zeros((nclasses,ncols))
for i in labelsun:
    #Find indexes again
    indexes = np.reshape(labels ==i, nrows) #Select the data that matches the class
    classData= data[indexes, :]
    #For each column in this data
    for j in range (ncols):
        #Find thresholds, high and low
        thresholdLow = average[i-1,j]-2*sd[i-1,j] 
        thresholdHigh = average[i-1,j]+2*sd[i-1,j]
        #Any data above or below
        remain = [x for x in classData[:,j] if(x > thresholdLow)]
        remain = [x for x in classData[:,j] if(x < thresholdHigh)]
        #Calculate percentage of outliers
        outliers2sd[i-1,j] = 100 * (labelsCounts[i-1] - len(remain)) / labelsCounts[i-1]
print (header)
print (outliers2sd)


# COMMAND ----------

#Export to spark.csv file
#some variables for formatting
decimals = 2
fmt="%.2f"
formatf = ".csv"
import pandas as pd

# Our data is in all sorts of shapes now after collecting it
#Well put it together, format it, and export it
species = np.array(['setosa', 'versicolor', 'virginica'])
# For each of the flowers in our df
for i in range(len(labelsUn)):
    #Stack the statistics generated
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]] ).T
    #Round the decimals to the nearest 2 places
    temp = np.around (temp, decimals)
    #Cast numbers to string and format
    temp_str = np.char.mod (fmt, temp)
    #Take header row and transpose it to be a column
    rows = np.array(header [:-1].astype("U")) [:, np.newaxis]
    
    #Put header column next to data 
    rowsf= np.hstack ((rows, temp_str))
    #make beauty header row for the csv
    headerf = [species[i], 'mean', 'min', 'max', 'std', 'outliers2sd%']
    #Cast to a pandas dataframe, to then be cast to spark dataFrame 
    pdDf = pd.DataFrame (rowsf, columns = [headerf])
    
    #Cast to spark dataframe
    sparkDf = spark.createDataFrame(pdDf)
    #Try to write out 4 csvs
    try:
        sparkDf.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/tables/irisTest/" + str(species[i]))
    except:
        #Unless file already exists
        print("File Already Exists")
        
    #Read back file to make sure everything works
    display (spark.read.csv("dbfs:/FileStore/tables/irisTest/" + str(species[i])))

# COMMAND ----------

import matplotlib.pyplot as plt
import numpy as np

# COMMAND ----------

#28/02
y=np.linspace(-1,1,5)
x=np.arange(5)

number_rows = 3
number_columns = 2

fig2 = plt.figure()
ax2 = fig2.subplots(number_rows, number_columns)
ax2[2,1].plot(x,y)
ax2[0,1].plot(x,y)

# COMMAND ----------

y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)

fig, ax = plt.subplots(2,2) 
ax [0,0].plot(x,y1) 
ax[0,1].scatter(x,y2) 
ax[1,0].bar(x,y1) 
ax[1,1].barh(x,y1)

# COMMAND ----------

x = np.arange(0, 4*np.pi, 0.05) 
ycos = np.cos(x)
ysin = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, ycos, 'b-', label="cos(x)") 
ax.plot(x, ysin, 'r--', label="sin(x)")

ax.set_title("Trigonometric functions") 
ax.set_xlabel("e to 4pi") 
ax.set_ylabel("cos(x) and sin(x)") 
ax.legend()

# COMMAND ----------

fig, ax = plt.subplots(1,2)

ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', xmin=0.25, xmax=0.75, color='orchid') 
ax[0].axhline (0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))
               
               
ax[1].axvline(0.3, color='red')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=10)
ax[1].axvline(0.6, linestyle=':', ymin=0.25, ymax=0.75, color='orchid') 
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1, 0.2, 0.5, 0.3))

# Set x-axix and y-axis limits 
ax[0].set_ylim([0.1, 0.9]) 
ax[1].set_xlim([0.1, 0.9])

# Set title to figure and subplots
fig.suptitle("Horizontal and vertical lines", fontsize=14) 
ax[0].set_title('Horizontal lines', fontstyle='italic') 
ax[1].set_title('Vertical lines', color='green', fontname='Arial')

# COMMAND ----------

x = np.array([2,4,6,7,4,2,5,7,8,9,4,2,1]) 
y= np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])

fig, ax = plt.subplots(1,3) 
ax[0].scatter (x,y) 
ax[0].set_title('default')

ax[1].scatter (x, y, 50, marker='+') 
ax[1].set_title('size = 50, style = +')


crosses=ax[2]. scatter (x, y, 200, marker='+', linewidth=3)
bullets=ax[2]. scatter (x, y, 50, marker='o', color='black')
bullets.set_edgecolors ('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------


#3D
z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
fig = plt.figure()
ax = np.array([fig.add_subplot(1, 3, 1, projection='3d'), 
               fig.add_subplot(1, 3, 2, projection='3d'), 
               fig.add_subplot(1, 3, 3, projection='3d')])

ax[0].scatter(x,y,z)
ax[0].set_title('default')

ax[1].scatter(x, y, z, s=50, marker='+') 
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, z, s=200, marker='+', linewidth=3) 
bullets = ax[2]. scatter(x, y, z, s=50, marker='o', color='black') 
bullets.set_edgecolors ('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

# Data
people = ["Student A", "Student B"]
studentA= np.array([90,50,80,40])
studentB= np.array([75,45,60,95])
x = np.arange (len (studentA))

# Figure
fig, ax = plt.subplots (1,2)

# Plots
ax[0].bar(x, studentA, width=0.3)
ax[1].bar(x, studentB, width=0.3)

# Aesthetics
for i in range (len (ax)):
    ax[i].set_ylim([0, 100])
    ax[i].set_title (people [i])
    ax[i].set_xlabel("exercises")
    ax[i].set_ylabel("mark (%)")
    ax[i].set_xticks ([0,1,2,3])
    ax[i].set_xticklabels(["ex1","ex2","ex3","ex4"])

# Extra: fixes the subplots separation
fig. tight_layout()

fig, ax = plt.subplots()
width = 0.3
slbars= ax.bar(x - width/2, studentA, width, label='Student A')
s2bars = ax.bar(x + width/2, studentB, width, label='Student B')

# COMMAND ----------

import matplotlib.pyplot as plt
import numpy as np

# Data
people = ["Student A", "Student B"]
studentA= np.array([99,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange (len (studentA))

fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/3.5, studentA, width, label='Student A')
s2bars = ax.bar(x + width/3.5, studentB, width, label='Student B')

ax.set_xlabel("Students")
ax.set_ylabel("Mark %")
ax.set_title('Student excersises')

ax.set_xticks ([0,1,2,3])
ax.set_xticklabels(["ex1","ex2","ex3","ex4"])

for i in range (len (studentA)):
    s1bars [1].set_linewidth (3.5)
    s2bars [1].set_linewidth (3.5)
    if studentA[1] < 50:
        slbars[i].set_edgecolor('red')
    if studentB[1] < 50:
        s2bars[i].set_edgecolor('red')

ax.legend()

# COMMAND ----------


