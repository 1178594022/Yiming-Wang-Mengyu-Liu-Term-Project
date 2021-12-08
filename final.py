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


def virus(np,nom,nov,nob,d):
    # number_of_people = int(input('please enter the number of people smaller than 10000>>>'))
    # number_of_only_masked = int(input('please enter the the number of only maked but not vaccinated herer >>>'))
    # number_of_only_vaccinated = int(input('please enter the the number of only Vaccinated but not masked herer >>>'))
    # number_of_both = int(input('please enter the the number of both Vaccinated and masked herer >>>'))
    # days = int(input('please enter the number of days of the simulation>>>'))
    number_of_people = int(np)
    number_of_only_masked = int(nom)
    number_of_only_vaccinated = int(nov)
    number_of_both = int(nob)
    days = int(d)
    number_of_unprotected = int(number_of_people)-int(number_of_only_masked) - int(number_of_only_vaccinated) - int(number_of_both)
    day = []
    people_inffected = []
    unprotected_inffected = []
    only_masked_inffected = []
    only_vaccinated_inffected = []
    masked_and_vaccinated_inffected = []
    num_people_meet=20
    # try:
    #     number_of_only_masked+number_of_only_vaccinated+number_of_both<number_of_people
    # except:
    #     raise Exception('There has been an error in the system')

    f = open('data/name.txt')

    list_of_name = []
    for line in f:
        list_of_name.append(line.strip().replace(' ','_'))
    list_to_use = list_of_name[:number_of_people]

    list_of_only_masked = list_to_use[0:number_of_only_masked]
    list_of_only_vaccinated = list_to_use[number_of_only_masked:number_of_only_masked+number_of_only_vaccinated]
    list_of_both = list_to_use[number_of_only_masked+number_of_only_vaccinated : number_of_only_masked+number_of_only_vaccinated+number_of_both]
    list_of_unprotected = list_to_use[number_of_only_masked+number_of_only_vaccinated+number_of_both:number_of_people+1]

    class Virus():
        def __init__(self, name = '', masked = False, vaccinated = False, inffected = False):
            self.name = name
            self.masked = masked
            self.vaccinated = vaccinated
            self.inffected = inffected
        def __str__(self):
            return f'name:{self.name}, mask:{self.masked}, vaccinated:{self.vaccinated}, inffected:{self.inffected}'

    l = []
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
    for num1 in range(days):
        for i in l:
            for num2 in range(num_people_meet):
                person_met = random.choice(l) # need modification of not meeting one self.
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
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
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
        result += f'-----------------------------------------Day {num1 + 1}-----------------------------------------\n'
        result += f'{count1} number of people inffected out of {number_of_people} people\n'
        result += f'{count2-1} people out of the {number_of_unprotected} unprotected people are inffected\n'
        result += f'{count3} people out of the {number_of_only_masked} masked but not vaccinated people are inffected\n'
        result += f'{count4} people out of the {number_of_only_vaccinated} vaccinated but not masked people are inffected\n'
        result += f'{count5} people out of the {number_of_both} both masked and vaccinated people are inffected\n'
        result += f'\n'
        day.append(num1+1)
        people_inffected.append(count1)
        unprotected_inffected.append(count2-1)
        only_masked_inffected.append(count3)
        only_vaccinated_inffected.append(count4)
        masked_and_vaccinated_inffected.append(count5)
    return result

    # plt.plot(day, people_inffected, label = "Total Inffection")
    # plt.plot(day, unprotected_inffected, label = "Unprotected People Inffected")
    # plt.plot(day, only_masked_inffected, label = "Only Masked People Inffected")
    # plt.plot(day, only_vaccinated_inffected, label = "Only Vaccinated People Inffected")
    # plt.plot(day, masked_and_vaccinated_inffected, label = "Both Vaccinated and Masked People Inffected")
    # plt.legend()
    # plt.show()
'''
    data = {'Day': day,
            'Total_Inffection':people_inffected,
            'Unprotected_people_inffection':unprotected_inffected,
            'Only_Masked_people_inffection':only_masked_inffected,
            'Only_Vaccinated_people_inffection':only_vaccinated_inffected,
            'Both_Masked_and_Vaccinated_People_inffection':masked_and_vaccinated_inffected}
    df = pd.DataFrame(data)
    print(pd)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=day,y=people_inffected,mode ='lines', name = 'Total Inffection'))
    fig.add_trace(go.Scatter(x=day,y=unprotected_inffected,mode ='lines', name = 'Unprotected people inffection'))
    fig.add_trace(go.Scatter(x=day,y=only_masked_inffected,mode ='lines', name = 'Only Masked people inffection'))
    fig.add_trace(go.Scatter(x=day,y=only_vaccinated_inffected,mode ='lines', name = 'Only Vaccinated people inffection'))
    fig.add_trace(go.Scatter(x=day,y=masked_and_vaccinated_inffected,mode ='lines', name = 'Both Masked and Vaccinated People inffection'))
    fig.show()
'''
    # import dash
    # import dash_core_components as dcc
    # import dash_html_components as html

    # app = dash.Dash()
    # app.layout = html.Div([
    #     dcc.Graph(figure=fig)
    # ])

    # app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

print(virus(1000,123,123,123,123))