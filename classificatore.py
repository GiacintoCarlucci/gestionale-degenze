from sklearn.model_selection import train_test_split
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from numpy import mean
from tabulate import tabulate
from pandas import read_csv
from sklearn import svm
from numpy import absolute
from numpy import sqrt
import pandas as pd
import numpy as np


sconto = read_csv('idoneitaticket.csv')
X = np.array(sconto.drop(columns=['idoneitaticket']))
y = np.array(sconto['idoneitaticket'])

cv = LeaveOneOut()

model = LinearRegression()
scores = cross_val_score(model,X,y,scoring='neg_mean_squared_error',cv=cv,n_jobs=-1)
sqrt(mean(absolute(scores)))

def classifier():
    for train_index, test_index in cv.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    
    
    cod = 0
    reddito = 0
    protect = -1
    #result = True
    while (cod < 1 or cod > 11):
        
        table = [["CODICE_URGENZA","FASCIA"],
                ["bianco","1"],
                ["verde","2"],
                ["azzurro","3"],
                ["giallo","4"],
                ["rosso","5"],
                ["nero","6"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        
        intInserted = False
        while (not intInserted):
            cod = input("Inserisci il codice urgenza del paziente, seguendo la tabella sopra riportata: \n")
        
            intInserted = controlInput(cod)
        cod=int(cod)
        if(cod < 1 or cod > 11):
            print("Codice inserito non valido. Inserire un valore compreso tra 1 e 6")
            
    while (reddito < 1 or reddito > 3):
        
        table = [["REDDITO","FASCIA"],
                ["13.000 < REDDITO <= 26.000","1"],
                ["26.000 < REDDITO <= 40.000","2"],
                ["REDDITO > 40.000","3"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        
        
        intInserted = False
        while(not intInserted):
            
            reddito = input("Inserisci il reddito del paziente, seguendo questa tabella: ")
        
            intInserted = controlInput(reddito)
        reddito=int(reddito)
        
        if(reddito < 1 or reddito > 3):
            print("Reddito inserito non valido. Inserire un valore >= di 13.000")
            
    while (protect != 0 and protect != 1 ):
        protectAnswer = input("Il paziente e' in fascia protetta(fp) o no(n)?: ").lower()
        if(protectAnswer=='fp'):
            protect=1
        elif(protectAnswer=='n'):
            protect=0
        else:
            protect=-1
            print("Il valore che hai inserito non e' corretto. Inserisci 'fp' se il paziente e' in fascia protetta e 'n' altrimenti")
            
    idoneitaTicket = model.predict([[cod, reddito, protect]])
    for elem in idoneitaTicket:

        print(" In base a quanto appreso lo sconto sulla prestazione medica e' del: %0.2f" %elem + "%\n")


def bonta():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=0)
    
    model.fit(X_train, y_train)
    
    p_test = model.predict(X_test)
    p_test = p_test.astype(int)
    
    print(y_test)
    print(p_test)
    
    r2 = r2_score(y_test, p_test)
    
    print("R2 Score - Bontà Adattamento: %0.3f" %r2)

def controlInput(user_input):

    try:
        int(user_input)
        it_is = True
        
    except ValueError:
        it_is = False
        print("Inserire solo valori numerici.\n")
        
    return it_is



