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

    
    if(visuals == True):
        Iteration = 0
        print(f'Iteration {Iteration}')

        x_vals = list()
        y_vals = list()

        for j in points:
            x_vals.append(j[0])
            y_vals.append(j[1])

        plt.scatter(x_vals, y_vals, alpha = 0.5, edgecolor = 'w')

        for i in range(K):
            plt.scatter(centroids[i][0],centroids[i][1],marker =",",edgecolor='k',color='black')

        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.show()

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


        
        if(visuals == True):
            Iteration += 1
            print(f'Iteration {Iteration}')
            
            for i in range(K):
                x_vals = list()
                y_vals = list()

                for j in centroid_dict[i]:
                    x_vals.append(j[0])
                    y_vals.append(j[1])

                plt.scatter(x_vals, y_vals, alpha = 0.5, edgecolor = 'w')
                plt.scatter(centroids[i][0],centroids[i][1],marker =",",edgecolor='k',color='black')

            plt.xlabel('X axis')
            plt.ylabel('Y axis')
            plt.show()                

        if(changed_K == 0):
            break

        centroid_dict = dict()
        for i in range(K):
            centroid_dict[i] = list()

    clusters.append(centroids)
    clusters.append(centroid_dict)

    return clusters



def clusterQuality(clusters):
    
    centroids = clusters[0]
    centroid_dict = clusters[1]

    sum_sq_err = 0

    for i in range(K):
        c = centroids[i]
        
        for p in centroid_dict[i]:
            sum_sq_err += euclidean_distance(c, p)

    score = sum_sq_err
    
    return score
    

def keepClustering(points,K,N,visuals):
    clusters = []
    clusters_list = []
    scores_list = []
    
    for i in range(N):
        print(f'Running K-means for iteration number {i+1}')
        cluster_generated = cluster(points, K, visuals = visuals)
        clusters_list.append(cluster_generated)
        score = clusterQuality(cluster_generated)
        scores_list.append(score)
    
    min_score_index = scores_list.index(min(scores_list))
    clusters = clusters_list[min_score_index]

    centroids = clusters[0]
    centroid_dict = clusters[1]            
    
    return clusters
    

def newGaussClusters(K, count):
    points = []
    mean = 10
    variance = 20

    for i in range(count):
        points.append([random.gauss(mean, variance), random.gauss(mean, variance)])

    clusters = cluster(points, K, visuals=True)


K = 3
N = 10
points = initializePoints(1000)

clusters = keepClustering(points,K,N,False)

print ("The score of best Kmeans clustering is:", clusterQuality(clusters))

#newGaussClusters(K, 1000)