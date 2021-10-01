import numpy as np
from numpy.core.numeric import identity 
import pandas as pd 

pd.set_option('display.max_columns', None)
dataset = pd.read_csv('/home/chem/Documents/dataset.csv')
dataset2 = dataset 
b = 45 


def scores(dataset):
    UID = dataset['user_a'].drop_duplicates()  
    scores = []

    for i in UID:
        riskscores =[]
        contactsIndex = dataset[dataset['user_a'] == i].index
        print('user', i)
        print(' user contacts', contactsIndex)
     
    
        for j in contactsIndex:
            timeXdist = (45 * dataset['time'].iloc[[j]] * dataset['dist'].iloc[[j]])
            riskscores.append(float(timeXdist))
           

        
        equation = sum(riskscores)
        scores.append(equation)
        print('risk for each contact', riskscores)
        print('sum of risk for contacts', equation)
        print('\n')
    

    
    covidRisk = pd.DataFrame()
    covidRisk['UID'] = UID
    covidRisk['scores'] = scores
    return covidRisk


def convertor(time, dist):
    timeScore = []
    distScore = []
    
    for i in time:
        if i < 5:
            timeScore.append(0.5)
        elif i >=5 and i< 15:
            timeScore.append(1)
        elif i >= 15 and i < 60:
            timeScore.append(2)
        else:
            timeScore.append(4)

    for i in dist:
        if i <2:
            distScore.append(2)
        elif i >= 2 and i < 4:
            distScore.append(1)
        else:
            distScore.append(0.1)
    return timeScore, distScore


time, dist = convertor(dataset['contact_duration'],dataset['contact_distance'])
dataset['time'] = time
dataset['dist'] = dist

covidRisk = scores(dataset)
