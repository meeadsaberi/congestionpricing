# Here we import two modules that are necessary for running this API.
from AMesoAPI import *
import csv

pricing_sections = []
# Your pricing sections csv file should contain the ids of all your pricing links, either in a row or in a column.
with open(r'This is the path to your pricing sections csv file', 'rb') as f:
    for line in f:
        for s in line.split(','):
            pricing_sections.append(int(s))
num = len(pricing_sections)

# Here you define your tolls. As an example, we consider a particular picing regime called the joint distance and delay toll.
# Details of this pricing regime can be found in this paper: Gu, Z., Shafiei, S., Liu, Z., Saberi, M., 2018. Optimal distance- and time-dependent area-based pricing with the Network Fundamental Diagram. Transp. Res. Part C 95, 1-28.
# The tolling period is from 8 to 10 AM, with a total of 8 small tolling intervals, each of which is 15 min.
distance_toll = [x1, x2, x3, x4, x5, x6, x7, x8]
delay_toll = [y1, y2, y3, y4, y5, y6, y7, y8]
# The simulation starts from 6 AM. Hence the first tolling interval starts after 7200 sec. Here we minus one to ensure that the tolls are in effect before the immediate route choice update.
t_1 = 7200 - 1
t_2 = 8100 - 1
t_3 = 9000 - 1
t_4 = 9900 - 1
t_5 = 10800 - 1
t_6 = 11700 - 1
t_7 = 12600 - 1
t_8 = 13500 - 1
t_9 = 14400 - 1


def MesoAPILoad(simhandler):
    return 0


def MesoAPIInit(simhandler, iterationNumber, statisticsActivated):
    return 0


def MesoAPIUnLoad(simhandler):
    return 0


def MesoAPIFinish(simhandler):
    return 0


def MesoAPINewVehicleSystem(simhandler, vehhandler):
    return 0


def MesoAPINewVehicleNetwork(simhandler, vehhandler):
    return 0


def MesoAPIFinishVehicleNetwork(simhandler, vehhandler, normalOut):
    return 0


def MesoAPIEnterVehicleSection(simhandler, vehhandler, fromSection, toSection):
    return 0


def MesoAPIExitVehicleSection(simhandler, vehhandler, section):
    return 0


def MesoAPIPostManageControl(simhandler):
    return 0

# The tolls are implemented solely under this function.
def MesoAPIPreManageRouteChoice(simhandler):
	# If you have warm up time, you need to subtract this time from t below.
    t = AMesoGetCurrentTime(simhandler)
	# The following loop simply allocates the tolls to the corresponding tolling intervals.
    if t_1 < t < t_2:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[0])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[0])
    elif t_2 < t < t_3:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[1])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[1])
    elif t_3 < t < t_4:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[2])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[2])
    elif t_4 < t < t_5:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[3])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[3])
    elif t_5 < t < t_6:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[4])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[4])
    elif t_6 < t < t_7:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[5])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[5])
    elif t_7 < t < t_8:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[6])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[6])
    elif t_8 < t < t_9:
        for n in range(num):
            AMesoSetSectionUserDefinedCost(simhandler, pricing_sections[n], distance_toll[7])
            AMesoSetSectionUserDefinedCost2(simhandler, pricing_sections[n], delay_toll[7])
    return 0