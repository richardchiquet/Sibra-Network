# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:54:31 2020

@author: chiquetr
"""

class Stop:
    
    
    def __init__(self,name,schedule=[],nextStops=[]):
        self.name = name
        self.nextStops = nextStops
        self.schedule = schedule
        
        
    def getName(self):
        return self.name
    
    def getNextStops(self):
        return self.nextStops
    
    def getSchedule(self):
        return self.schedule
    
    def addSchedule(self,scheduleToAdd):
        self.schedule = self.schedule+[scheduleToAdd]
    
    def addNextStops(self,StopsToAdd):
        self.nextStops=self.nextStops+StopsToAdd



class Network:
    
    
    
    def __init__(self,stops=[]):
        self.stops = stops
        
    
    def getStops(self):
        return self.stops
        
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
    
    def shortestResearch(self,starting,ending):
        if not(self.stopExist(starting)) or not(self.stopExist(ending)):
            return (print('wrong stop'))
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
    
            
            
            