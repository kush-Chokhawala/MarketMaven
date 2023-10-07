"""Importing the Dependencies"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

"""Data Collection & Analysis"""

# loading the data from csv file to a Pandas DataFrame
customer_data = pd.read_csv('/content/drive/MyDrive/Kush_Modi Personal/Personal Projects/Unsupervised ML/Customer Segmentation using K-Means Clustering/Mall_Customers.csv')

# first 5 rows in the dataframe
customer_data.head()

# finding the number of rows and columns
customer_data.shape

# getting some informations about the dataset
customer_data.info()

# checking for missing values
customer_data.isnull().sum()

"""Choosing the Annual Income Column & Spending Score column"""

X = customer_data.iloc[:,[3,4]].values
print(X)

"""Choosing the number of clusters

WCSS -> Within Clusters Sum of Squares
"""

# Finding WCSS value for different number of clusters

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(X)

  wcss.append(kmeans.inertia_)

#plot an elbow graph

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Graph')
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.show()

"""Optimum Number of Clusters = 5

Training the k-Means Clustering Model
"""

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)

# return a label for each data point based on their cluster
Y = kmeans.fit_predict(X)
print(Y)

"""5 Clusters - 0, 1, 2, 3, 4

Visualizing all the Clusters
"""

# plotting all the clusters and their Centroids

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c='blue', label='Cluster 5')

# plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

"""Pairplot for Feature Visualization"""

sns.pairplot(customer_data, vars=['Age', 'Annual Income (k$)', 'Spending Score (1-100)'])
plt.show()

"""Distribution of Annual Income and Spending Score"""

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(customer_data['Annual Income (k$)'], bins=20, kde=True)
plt.title('Distribution of Annual Income')

plt.subplot(1, 2, 2)
sns.histplot(customer_data['Spending Score (1-100)'], bins=20, kde=True)
plt.title('Distribution of Spending Score')

plt.show()

"""Countplot for Gender Distribution"""

plt.figure(figsize=(6, 4))
sns.countplot(data=customer_data, x='Gender')
plt.title('Gender Distribution')
plt.show()

"""Boxplot for Age Distribution by Gender"""

plt.figure(figsize=(8, 6))
sns.boxplot(data=customer_data, x='Gender', y='Age')
plt.title('Age Distribution by Gender')
plt.show()

"""Boxplot for Spending Score Distribution by Gender"""

plt.figure(figsize=(8, 6))
sns.boxplot(data=customer_data, x='Gender', y='Spending Score (1-100)')
plt.title('Spending Score Distribution by Gender')
plt.show()

