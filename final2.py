from os import error
import re
import random
import matplotlib.pyplot as plt
import numpy as np
from plotly.graph_objs import layout
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib
import seaborn
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter  
import ffmpeg
import matplotlib.animation as animation

def virus_plot(np,nom,nov,nob,d):
    # number_of_people = int(input('please enter the number of people smaller than 10000>>>'))
    # number_of_only_masked = int(input('please enter the the number of only maked but not vaccinated herer >>>'))
    # number_of_only_vaccinated = int(input('please enter the the number of only Vaccinated but not masked herer >>>'))
    # number_of_both = int(input('please enter the the number of both Vaccinated and masked herer >>>'))
    # days = int(input('please enter the number of days of the simulation>>>'))
    
    number_of_people = int(np) #record input np as number_of_people veriable
    number_of_only_masked = int(nom)#record input nom as number_of_only_masked veriable
    number_of_only_vaccinated = int(nov)#record input nov as number_of_only_vaccinated veriable
    number_of_both = int(nob)#record input nob as number_of_both veriable
    days = int(d)#record input d as days veriable
    number_of_unprotected = int(number_of_people)-int(number_of_only_masked) - int(number_of_only_vaccinated) - int(number_of_both)#calculated the number of people who is unprotected
    day = []#defind a day list
    people_inffected = []#defind a people_inffected list
    unprotected_inffected = []#defind a unprotected_inffected list
    only_masked_inffected = []#defind a only_masked_inffected list
    only_vaccinated_inffected = []#defind a day list
    masked_and_vaccinated_inffected = []#defind a only_vaccinated_inffected list
    num_people_meet=20 # assumption, every person will meet 20 people every day with close contact

    f = open('data/name.txt') #open txt file where stores 10000 names

    list_of_name = [] # prepare the list_of_name to store the names
    for line in f:#change the names into one word
        list_of_name.append(line.strip().replace(' ','_'))
    list_to_use = list_of_name[:number_of_people]
    '''
    Assign names to each category of people, also it counts the people for us
    '''
    list_of_only_masked = list_to_use[0:number_of_only_masked] #
    list_of_only_vaccinated = list_to_use[number_of_only_masked:number_of_only_masked+number_of_only_vaccinated]
    list_of_both = list_to_use[number_of_only_masked+number_of_only_vaccinated : number_of_only_masked+number_of_only_vaccinated+number_of_both]
    list_of_unprotected = list_to_use[number_of_only_masked+number_of_only_vaccinated+number_of_both:number_of_people+1]

    class Virus():
        '''defube the status of each person'''
        def __init__(self, name = '', masked = False, vaccinated = False, inffected = False):
            self.name = name
            self.masked = masked
            self.vaccinated = vaccinated
            self.inffected = inffected
        '''show the status of each person by print'''
        def __str__(self):
            return f'name:{self.name}, mask:{self.masked}, vaccinated:{self.vaccinated}, inffected:{self.inffected}'

    l = [] # make a list l to hold of all people
    '''put all people into the list with assigned status and names, i is the names for each of the name list'''
    for i in list_of_only_masked:
        i = Virus(i,True,False,False)
        l.append(i)
        # print(i)
    for i in list_of_only_vaccinated:
        i = Virus(i,False,True,False)
        l.append(i)
        # print(i)
    for i in list_of_both:
        i = Virus(i,True,True,False)
        l.append(i)
        # print(i)
    for i in list_of_unprotected:
        i = Virus(i,False,False,False)
        l.append(i)
        # print(i)

    #put in 1 person who is affected and unprotected
    patient = Virus('original_inffection', False, False,True)
    l.append(patient)
    # print(patient.inffected)

    # shuffle the list to decide on go out sequence
    random.shuffle(l)

    # Start the simulation
    result = ''
    '''loop of every day'''
    for num1 in range(days):
        '''loop of every person in each day'''
        for i in l:
            '''loop of meeting 20 people every day, for every person met'''
            for num2 in range(num_people_meet):
                '''randomly select a person to meet'''
                person_met = random.choice(l) # need modification of not meeting one self.
                '''according to each person met and the person who goes out, apply different inffection rate to calculate for the probability of inffection and apply it to the oop characterastics'''
                if i.inffected == True and person_met.vaccinated == True:
                    prob = random.random()
                    if i.masked == True and person_met.masked == True:
                        if prob < 0.015*0.0002: #both masked inffection rate*vaccine break through rate
                            person_met.inffected = True
                    elif i.masked == True and person_met.masked == False:
                        if prob < 0.05*0.0002: #patient masked inffection rate*vaccine break through rate
                            person_met.inffected = True 
                    elif i.masked == False and person_met.masked == True:
                        if prob < 0.3*0.0002: #only healthy person masked inffection rate*vaccine break through rate
                            person_met.inffected = True
                    elif i.masked == False and person_met.masked == False:
                        if prob < 0.9*0.0002: #both not masked inffection rate*vaccine break through rate
                            person_met.inffected = True                   
                elif i.inffected == True and person_met.vaccinated == False:
                    prob = random.random()
                    if i.masked == True and person_met.masked == True:
                        if prob < 0.015: #both masked inffection rate
                            person_met.inffected = True
                    elif i.masked == True and person_met.masked == False:
                        if prob < 0.05: #patient masked inffection rate
                            person_met.inffected = True 
                    elif i.masked == False and person_met.masked == True:
                        if prob < 0.3: #only healthy person masked inffection rate
                            person_met.inffected = True
                    elif i.masked == False and person_met.masked == False:
                        if prob < 0.9: #both not masked inffection rate
                            person_met.inffected = True
                elif person_met.inffected == True and i.vaccinated == True:
                    prob = random.random()
                    if i.masked == True and person_met.masked == True:
                        if prob < 0.015*0.0002: #both masked inffection rate*vaccine break through rate
                            i.inffected = True
                    elif i.masked == True and person_met.masked == False:
                        if prob < 0.3*0.0002: #patient masked inffection rate*vaccine break through rate
                            i.inffected = True 
                    elif i.masked == False and person_met.masked == True:
                        if prob < 0.05*0.0002: #only healthy person masked inffection rate*vaccine break through rate
                            i.inffected = True
                    elif i.masked == False and person_met.masked == False:
                        if prob < 0.9*0.0002: #both not masked inffection rate*vaccine break through rate
                            i.inffected = True                   
                elif person_met.inffected == True and person_met.vaccinated == False:
                    prob = random.random()
                    if i.masked == True and person_met.masked == True:
                        if prob < 0.015: #both masked inffection rate
                            i.inffected = True
                    elif i.masked == True and person_met.masked == False:
                        if prob < 0.3: #patient masked inffection rate
                            i.inffected = True 
                    elif i.masked == False and person_met.masked == True:
                        if prob < 0.05: #only healthy person masked inffection rate
                            i.inffected = True
                    elif i.masked == False and person_met.masked == False:
                        if prob < 0.9: #both not masked inffection rate
                            i.inffected = True
        
        count1 = 0 #count of total inffection
        count2 = 0 #count of unprotected peopple inffection
        count3 = 0 #count of people wear mask only got inffected
        count4 = 0 #cont of people vaccinated only got inffected
        count5 = 0 #count of poeple vaccinated and masked got inffected
        '''start the counting process'''
        for i in l:
            if i.inffected == True:
                count1 = count1 + 1
        for i in l:
            if i.inffected == True and i.masked == False and i.vaccinated == False:
                count2 = count2 + 1
        for i in l:
            if i.inffected == True and i.masked == True and i.vaccinated == False:
                count3 = count3 + 1   
        for i in l:
            if i.inffected == True and i.masked == False and i.vaccinated == True:
                count4 = count4 + 1  
        for i in l:
            if i.inffected == True and i.masked == True and i.vaccinated == True:
                count5 = count5 + 1
        '''make lists for data frame in order to graph the gif'''
        day.append(num1+1)
        people_inffected.append(count1)
        unprotected_inffected.append(count2-1)
        only_masked_inffected.append(count3)
        only_vaccinated_inffected.append(count4)
        masked_and_vaccinated_inffected.append(count5)

    '''make the dictionary'''
    data = {'Day': day,
            'Total_Inffection':people_inffected,
            'Unprotected_people_inffection':unprotected_inffected,
            'Only_Masked_people_inffection':only_masked_inffected,
            'Only_Vaccinated_people_inffection':only_vaccinated_inffected,
            'Both_Masked_and_Vaccinated_People_inffection':masked_and_vaccinated_inffected}
    
    '''define into a data frame'''
    df = pd.DataFrame(data)
    
    '''define the plot'''
    fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
    axes.set_ylim(0, number_of_people)
    axes.set_xlim(0, days)
    plt.style.use("ggplot")
    '''define list for x and y axis'''
    x,y1,y2,y3,y4,y5 = [], [], [], [], [], []
    '''define the animation, each line and the color'''
    def animate(i):
        x.append(data['Day'][i])
        y1.append((data['Total_Inffection'][i]))
        y2.append((data['Unprotected_people_inffection'][i]))
        y3.append((data['Only_Masked_people_inffection'][i]))
        y4.append((data['Only_Vaccinated_people_inffection'][i]))
        y5.append((data['Both_Masked_and_Vaccinated_People_inffection'][i]))
        axes.plot(x,y1, color="red")
        axes.plot(x,y2, color="gray")
        axes.plot(x,y3, color="blue")
        axes.plot(x,y4, color="yellow")
        axes.plot(x,y5, color="green")
    
    '''define the animation detain and format'''
    ani = FuncAnimation(fig=fig, func=animate)
    writergif = PillowWriter(fps=30)
    
    '''ignore the uninportant error'''
    try:
        '''save the animation to gif'''
        ani.save("templates/movie.gif",writer=writergif)
    except Exception:
        pass
    
    
    
virus_plot(100,10,10,80,300)