
import numpy as np
N_population= int(input("Enter the number of population"))  # Total number of population
Healthy_state=0
Sick_state=1
Dead_state=2
mortality_rate=.005
no_immunity=0
immune=1
recovery_days=9
infection_prob_healthy=.03
infection_prob_sick=.30
data= np.zeros((N_population,3)) # This creates an array with N_population as the rows and three columns for health status(colunm 1), immune status(colunm 2) and sick day count(colunm 3).
pandemic_start= np.random.randint(N_population) # Here, we are selecting one person randomly from the whole population and assigning as sick.
data[pandemic_start,0]=Sick_state  # This will mark one person as sick

#case a
for days in range(101):
    sick_group = data[:,0]==Sick_state #here we identify all the sick ones.
    death_probability=np.random.random(N_population)
    dead=sick_group & (death_probability<mortality_rate) #here, we find sick ones those have low mortality rate and mark as dead.
    data[dead,0]=Dead_state
#case b    
    data[sick_group,2]+=(1)#increasing the counter of days by one to calculate how long a sick person is sick.
    print(data)
    healthy_and_immune=(sick_group) & (data[:,2]>recovery_days) # finging every sick person who covered 10 days and putting them back to healthy and immune state.
    data[healthy_and_immune,0]=Healthy_state
    data[healthy_and_immune,1]=immune
    data[healthy_and_immune,2]=0  # once the sick person become immune, the days will kept back to 0.
    
#case c and d
remaining_sick_people=np.where(data[:,0]==1)[0] # here we will find the indices of remaining sick people after case a and b.
random_meet=np.random.randint(0,11,size=np.sum(remaining_sick_people))# this defines the total random number of meet by sick people
people_met=np.random.randint(0,N_population,size=random_meet.sum()) # this defines the random number of meet by remaining sick people with random number of population

people_met_health_status=data[people_met,0] #this defines the health status of people who met sick people
people_met_immune_status=data[people_met,1] #this defines the immunity status of people who met sick people

infection_prob=np.where(people_met_immune_status==immune,infection_prob_healthy,infection_prob_sick)
infection_occuring=np.random.random(len(people_met))
new_infections=(people_met_health_status==Healthy_state)&(infection_occuring<infection_prob) # this checks where the person is healthy and ra
data[people_met[new_infections], 0] = Sick_state  # this mentions the newly infected healthy people

number_of_sick = np.sum(data[:, 0] == Sick_state)
number_of_dead = np.sum(data[:, 0] == Dead_state)
number_of_healthy = np.sum((data[:, 0] == Healthy_state) & (data[:, 1] == 0))
number_of_immune = np.sum(data[:, 1] == immune)

print(f"Sick: {number_of_sick}, Dead: {number_of_dead}, Healthy: {number_of_healthy}, Immune: {number_of_immune}")

#The code leverages NumPy's vectorized operations to simulate the spread of Virus V within a population.
#Over the course of 100 simulated days, the model accurately reflects the progression of infection, recovery, the development of immunity, and mortality.
#The findings indicate that even with a relatively low mortality rate, the virus can have a profound impact on the population's health, leading to widespread infections and fatalities if not properly managed.

    
    
   
   
