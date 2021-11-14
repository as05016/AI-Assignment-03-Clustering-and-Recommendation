#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Student 1(Name and ID):
Student 2(Name and ID):

"""

import random

def initializePoints(count):
     for i in range(int(count/3)):
         points.append([random.gauss(0,10),random.gauss(100,10)])
     for i in range(int(count/3)):
         points.append([random.gauss(-30,20),random.gauss(10,10)])
     for i in range(int(count/3)):
         points.append([random.gauss(30,20),random.gauss(10,10)])

     return points



def cluster(points,K,visuals = True):
    clusters=[]
    
    #Your kmeans code will go here to cluster given points in K clsuters. If visuals = True, the code will also plot graphs to show the current state of clustering
    
    return clusters



def clusterQuality(clusters):
    score = -1
    #Your code to compute the quality of cluster will go here.
    
    return score
    

def keepClustering(points,K,N,visuals):
    clusters = []
    
    #Write you code to run clustering N times and return the formation having the best quality. 
    
    return clusters
    



K = 3
N = 10
points = initializePoints(1000)

clusters = keepClustering(points,K,N,True)

print ("The score of best Kmeans clustering is:", clusterQuality(clusters))

