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


