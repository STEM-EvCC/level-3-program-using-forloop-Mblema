mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

#Count the total number of missions.
number_of_mission = len(mission_names)


#Count the number of successful missions.
successfull_missions = 0
for x in mission_success:
    if x == True:
        successfull_missions += x  

#Calculate percentage of successful missions
success_percentage= (successfull_missions / number_of_mission)* 100

#Identify new list to store the missions launched before the year 2000.
mission_before_2000 = []
#For loop to identify mission before 2000 and joining the it  so we can print the names of the mission and not the year
for x in range(len(mission_years)):
    if mission_years[x] < 2000:
        mission_before_2000.append(mission_names[x])
    

print("Total number of missions: ", number_of_mission)
print("Number of successful missions: ", successfull_missions)
print("Success rate: ", str(round(success_percentage, 2 )) + "%")


#Printing missions launched before the year 2000.
print("Missions launched before the year 2000: ")
for mission in mission_before_2000:
        print( "-", mission)