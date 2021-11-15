#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Altaf Shaikh - as05016:
Maheen Anees - ma05156:

"""

import random
import math
import matplotlib.pyplot as plt

def initializePoints(count):
     points = []
     for i in range(int(count/3)):
         points.append([random.gauss(0,10),random.gauss(100,10)])
     for i in range(int(count/3)):
         points.append([random.gauss(-30,20),random.gauss(10,10)])
     for i in range(int(count/3)):
         points.append([random.gauss(30,20),random.gauss(10,10)])

     return points


def euclidean_distance(P1: tuple, P2: tuple):
     return math.sqrt(sum([(a - b) ** 2 for a, b in zip(P1, P2)]))


def cluster(points,K,visuals = True):
    clusters=[]

    #Your kmeans code will go here to cluster given points in K clsuters. If visuals = True, the code will also plot graphs to show the current state of clustering

    centroids = []
    centroid_dict = dict()
    for i in range(K):
        point = tuple(points[random.randint(0, len(points) - 1)])
        centroids.append(point)
        centroid_dict[i] = list()

    while True:

        for p in range(len(points)):
            distances = list()

            for c in range(len(centroids)):
                d = euclidean_distance(tuple(points[p]), centroids[c])
                distances.append(d)

            min_index = distances.index(min(distances))
            centroid_dict[min_index].append(tuple(points[p]))

        k_means = []

        for i in range(K):
            x_sum = 0
            y_sum = 0

            for j in centroid_dict[i]:
                x_sum += j[0]
                y_sum += j[1]
            
            if(len(centroid_dict[i]) != 0):
                x_mean = x_sum / len(centroid_dict[i])
                y_mean = y_sum / len(centroid_dict[i])
            else:
                x_mean = 0
                y_mean = 0

            k_means.append((x_mean, y_mean))


        changed_K = 0
        for i in range(K):
            cent_prev = centroids[i]
            cent_next = k_means[i]
            
            d = euclidean_distance(cent_prev, cent_next)

            if(round(d) > 1):
                centroids[i] = k_means[i]
                changed_K += 1
                
        if(changed_K == 0):
            break

        centroid_dict = dict()
        for i in range(K):
            centroid_dict[i] = list()


    if(visuals == True):

        for i in range(K):
            x_vals = list()
            y_vals = list()

            for j in centroid_dict[i]:
                x_vals.append(j[0])
                y_vals.append(j[1])

            plt.scatter(x_vals, y_vals, alpha = 0.7, edgecolor = 'w')
            plt.scatter(centroids[i][0],centroids[i][1],marker =",",edgecolor='k',color='r')

        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.show()

    return clusters



def clusterQuality(clusters):
    score = -1
    #Your code to compute the quality of cluster will go here.
    
    return score
    

def keepClustering(points,K,N,visuals):
    clusters = []
    
    cluster(points, K)
    #Write you code to run clustering N times and return the formation having the best quality. 
    
    return clusters
    



K = 3
N = 10
points = initializePoints(1000)

clusters = keepClustering(points,K,N,True)

print ("The score of best Kmeans clustering is:", clusterQuality(clusters))

