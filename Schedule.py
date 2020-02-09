class Schedule:

    def __init__(self,Schedule="00:00"):

        self.schedule=schedule


    def getSchedule(self):
        return self.schedule

    def dateconvert(self):
        ConvertedS=0
        if len(self.schedule) == 4:
            ConvertedS=self.schedule[0]*60+self.schedule[2]*10+self.schedule[3]
        if len(self.schedule) == 5 :
            ConvertedS=self.schedule[0]*600+self.schedule[1]*60+self.schedule[3]*10+self.schedule[4]
        else:
            return false
