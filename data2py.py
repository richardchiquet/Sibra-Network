#!/usr/bin/python3
# -*-coding:utf-8-*-

from Stop import Stop
from Network import Network
from Schedule import Schedule

data_file_name = '1_Poisy-ParcDesGlaisins.txt'
# data_file_name = '2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic


slited_content = content.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

Sibra_Networkw = Network()
for element in regular_path.split():
    if not (element in ['N', '+']):
        stop = Stop(element, [regular_date_go[element]])
        stop.addSchedule([regular_date_go[element], regular_date_back[element]])
        Sibra_Networkw.addStops([stop])

c = 0
for element in Sibra_Networkw.stops:
    if c == 0:
        element.addNextStops([Sibra_Networkw.stops[1]])
    elif c == len(Sibra_Networkw.stops) - 1:
        element.addNextStops([Sibra_Networkw.stops[c - 1]])
    else:
        element.addNextStops([Sibra_Networkw.stops[c - 1], Sibra_Networkw.stops[c + 1]])
    c += 1
"""
for element in Sibra_Networkw.stops:
    L=[]
    print(element.getName(),':' )
    for element2 in element.nextStops:
        L=L+[element2.getName()]
    print(L)
"""

data_file_name = '2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r') as f:
        content = f.read()
except OSError:
    # 'File not found' error message.
    print("File not found")


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic


slited_content = content.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

NewStop = []
for element in regular_path.split():
    if not (element in ['N','+']):
        if Sibra_Networkw.stopExist(element):
            Sibra_Networkw.getAStop(element).addSchedule([regular_date_go[element], regular_date_back[element]])
            NewStop.append(element)
        else:
            stop = Stop(element, [regular_date_go[element]])
            stop.addSchedule([regular_date_back[element], regular_date_go[element]])
            Sibra_Networkw.addStops([stop])
            NewStop.append(element)

print(Sibra_Networkw.getStopsName())
c = 0
for element in NewStop:
    if c == 0:
        Sibra_Networkw.getAStop(element).addNextStops([Sibra_Networkw.getAStop(NewStop[1])])
    elif c == len(NewStop) - 1:
        Sibra_Networkw.getAStop(element).addNextStops([Sibra_Networkw.getAStop(NewStop[c - 1])])
    else:
        Sibra_Networkw.getAStop(element).addNextStops(
            [Sibra_Networkw.getAStop(NewStop[c - 1]), Sibra_Networkw.getAStop(NewStop[c + 1])])
    c += 1

print(Sibra_Networkw.shortestResearch("Courier", "VIGNIÃˆRES"))

print(Sibra_Networkw.getStops()[3].getSchedule())

while True:
    ending = input("Where do you go?\n")

    if not (ending in Sibra_Networkw.getStopsName()):
        print("This ending is invalable")

    elif ending == "stop":
        break

    else:
        starting = input("Where are you leaving from?\n")

        if not (starting in Sibra_Networkw.getStopsName()):
            print("This starting is invalable")


        else:
            research = input("What type of reseach do you want (shortest,fastest,foremost)?")

            if research in ["shortest", "fastest", "foremost"]:

                if research == "shortest":
                    print(Sibra_Networkw.shortest(starting, ending))

                elif research in ["fastest","foremost"]:
                    date = input("When do you go (00:00) ?")

                    if research == "fastest":
                        print(Sibra_Networkw.fastest(starting,ending,date))
                    else:
                        print(Sibra_Networkw.fastest(starting,ending,date))