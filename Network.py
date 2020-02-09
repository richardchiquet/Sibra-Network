# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:54:31 2020

@author: chiquetr
"""
from Stop import Stop

class Network:
    
    
    
    def __init__(self,stops=[]):
        self.stops = stops
        
    
    def getStops(self):
        return self.stops

    def getStopsName(self):
        L=[]
        for element in self.getStops():
            L.append(element.getName())
        return L
        
    def addStops(self,stopsToAdd):
        self.stops=self.stops+stopsToAdd
        
    def stopExist(self,stop):
        for element in self.stops:
            if stop == element.getName():
                return True
        return False
    
    def getAStop(self,stop):
        for element in self.stops:
            if stop == element.getName():
                return element
        return False
    
    def getStopsName(self):
        L=[]
        for element in self.stops:
            L.append(element.getName())
        return L
    
    def shortest(self,starting,ending):
        CurrentPath = [starting]
        CurrentNode = starting
        NodeNotVisited =[]
        StopsExaminated=[]
        
        while True :
            if ending in CurrentPath:
                CurrentPath+[ending]
                break
            for element in self.getAStop(CurrentNode).getNextStops():
                if not element.getName() in StopsExaminated:
                    NodeNotVisited.append([element.getName(),CurrentPath+[element.getName()]])
            StopsExaminated+[CurrentNode]
            x = NodeNotVisited.pop(0)
            CurrentNode = x[0]
            CurrentPath = x[1]
            
        return CurrentPath
    
    def fastest(self,starting,ending,schedule):
        CurrentPath = [starting]
        CurrentNode = starting
        NodeNotVisited =[]
        StopsExaminated=[]
        stop = False
        while stop:
        pass

    def formost(self,starting,ending,schedule):
        pass