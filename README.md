[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9aHTYUBc)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15110423)
# STEM103_Level3_1-ForLoop
## Assignment 
In this assignment we are to make use of for loop in our code. 
We were provided with three lists; mission_names, mission_years and mission_success. 
we are to use these provided list to;
1. Counts the total number of space missions.
 - Here I used len() function to find the length of the list and that was was the total number of space missions
2. Counts the number of successful missions.
 - Here I use the loop to go through the mission_success list and to print the count number of True that are in the list.
3. Calculates the success rate of the missions.
 - This is a math problem so I just too the total number of part 2 and divided by the part 1 and multiplied by 100 to get the percentage. They I have to round the result in two decimal place so I used the Round() function.

4. Lists all the missions that were launched before the year 2000.
 - This was tricky because we have to use two list to tackle the problem. I had to use the intiate a new list where I will store my new values they use the mission_years list together with if to give the condition of printing items that are before the year 2000. I then had to join the results with the other list mission_names which is what we have to show on the terminal and finally used another for loop to print the new list (mission_before_2000).


## Sources used

https://www.w3schools.com/python/python_for_loops.asp
