# Databricks notebook source
import numpy as np
import pyspark as ps
import matplotlib.pyplot as plt

dataRaw = spark.read.csv (path = "dbfs:/FileStore/IrisData/iris_head_num.txt")
dataRaw = np.array(dataRaw.select("*").collect())
header = dataRaw [0, :]
data = dataRaw [1:, :4]
data = np.vstack(data.astype (np. float32))

labels = np.vstack (dataRaw [1:, 4].astype (np. int32))

labelsUn, labelsCounts = np.unique (labels, return_counts = 1)

# COMMAND ----------

nrows,ncols = np. shape(data) 
nclasses = len(labelsUn)
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses, ncols))
mini = np.zeros((nclasses, ncols)) 
sd = np.zeros((nclasses,ncols)) 
for i in labelsUn:
    indexes = np.reshape(labels==i, nrows)
    average[i-1,] = np.mean (data[indexes, :],axis=0) 
    maxi[i-1,:] = np.max(data[indexes, :], axis=0)
    mini[i-1] = np. min (data [indexes, :],axis=0) 
    sd[i-1,:] = np. std (data[indexes, :], axis=0)

# COMMAND ----------

species = np.array(['setosa', 'versicolor', 'virginica']) 
features = np.array (header [:-1].astype("U"))
x = np.arange(len(features))

fig, ax = plt.subplots() 
for i in labelsUn:
    ax.errorbar(x, average[i-1,:], sd[i-1,:], marker="o", label=species[i-1])

                             
#Aesthetics
ax. legend (loc= "upper right")
ax.set_xlabel("features", fontsize=14, fontweight='bold') 
ax.set_ylabel("mean +/- sd", fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels (features, rotation=45)
fig.tight_layout() #make sure that the axes labels fit the figure

# COMMAND ----------

#Boxplots (2)
outliers = dict(marker='+', markerfacecolor='black') 
medians = dict(linewidth=2)
boxes = np.array([dict (facecolor='r',color='r'),
                  dict (facecolor='g', color='g'),
                  dict (facecolor='b',color='b')])
                  
                  
mylegend = [plt.scatter ([0], [0], facecolor='r', edgecolor='r', label=species[0]),
            plt.scatter ([0], [0], facecolor='g', edgecolor='g', label=species[1]), 
            plt.scatter ([0], [0], facecolor='b', edgecolor='b', label=species [2])]
plt.close("all") #make sure that no figure is generated

# COMMAND ----------

x = -7
step = 5
fig, ax = plt.subplots()


for j in range(len(features)): #for each feature...
    x+= 7
    for i in labelsUn:     #for each category...
        indexes = np.reshape(labels==i,nrows)
        temp = data[indexes,j]
        ax.boxplot(temp, positions=[x],
                    widths=2,
                    patch_artist=True,
                    medianprops=medians,
                    boxprops=boxes[i-1],
                    flierprops=outliers)
        x+= step
        
ax.set_title("iris data set", fontsize=13, fontweight='bold') 
ax.set_ylabel("values", fontweight='bold') 
ax.set_xticks(np.arange(step, x, 22))
ax.set_xticklabels (features, fontweight='bold', rotation=45) 
ax. legend (handles=mylegend)
fig.tight_layout() #make sure that the axes labels fit the figure

# COMMAND ----------


