import paziente as pa
import percorso as pe
import struttura as s
import classificatore as c
import probabilita as p
from tabulate import tabulate
from pyswip import Prolog

prolog = Prolog()
prolog.consult("KB_1.pl") 

#funzioni dei vari comandi disponibili
def pazienti():
    print("\n-------------------------------LISTA PAZIENTI-------------------------------\n\n")
    pa.patientList()
    sodHelp()

def idonei():
    print("\n-------------------------------LISTA PAZIENTI IDONEI-------------------------------\n\n")
    pa.suitablePatientList()
    sodHelp()


def non_idonei():
    print("\n-------------------------------LISTA PAZIENTI NON IDONEI-------------------------------\n\n")
    pa.notSuitablePatientList()
    sodHelp()

def cerca_paziente():
    print("\n-------------------------------RICERCA PAZIENTE-------------------------------\n\n")
    pa.findPatient()
    sodHelp()

def aggiungi_paziente():
    print("\n-------------------------------AGGIUNTA PAZIENTI-------------------------------\n\n")
    pa.addPatient()
    sodHelp()

def modifica_paziente():
    print("\n-------------------------------MODIFICA PAZIENTI-------------------------------\n\n")
    pa.modifyPatient()
    sodHelp()

def percorsi():
    print("\n-------------------------------LISTA PERCORSI-------------------------------\n\n")
    pe.pathList()
    sodHelp()

def aggiungi_percorso():
    print("\n-------------------------------AGGIUNTA PERCORSO-------------------------------\n\n")
    pe.addPath()
    sodHelp()

def strutture():
    print("\n-------------------------------LISTA STRUTTURE-------------------------------\n\n")
    s.structList()
    sodHelp()


def aggiungi_struttura():
    print("\n-------------------------------AGGIUNTA STRUTTURA-------------------------------\n\n")
    s.addStruct()
    sodHelp()

def rimuovi_struttura():
    print("\n-------------------------------RIMOZIONE STRUTTURA-------------------------------\n\n")
    s.removeStruct()
    sodHelp()

def probabilita_idoneita():
    print("\n-------------------------------PROBABILITA' SCONTO TICKET-------------------------------\n\n")
    p.questionsForPrediction()
    sodHelp()

def percentuale_sconto():
    print("\n-------------------------------CALCOLO SCONTO TICKET-------------------------------\n\n")
    c.classifier()
    sodHelp()

def bonta_classificatore():
    print("\n-------------------------------BONTA' ADATTAMENTO-------------------------------\n\n")
    c.bonta()
    sodHelp()

def esci():
    print("\nS.O.D. Programma Terminato ")

def sodHelp():
    print("\nPer visualizzare la lista dei comandi digita: -1 ")

def default():
    print("\nValore non valido. Inserire un numero corretto.")

#messaggio di benvenuto  
def firstMessage():
    print("Benvenuto nel portale S.O.D. Sistema Operativo Degenze\n")
    
#menu per visualizzare i comandi disponibili
def mainMenu():
    table = [["COMANDO","DESCRIZIONE COMANDO"],
            ["",""],
            ["    ","PAZIENTI"],
            ["1","Mostra la lista di tutti i pazienti (idonei all'esenzione ticket e non)"],
            ["2","Mostra la lista di tutti i pazienti esenti dal ticket"],
            ["3","Mostra la lista di tutti i pazienti non esenti dal ticket"],
            ["4","Mostra le informazioni del paziente selezionato"],
            ["5","Aggiunge un nuovo paziente"],
            ["6","Modifica un paziente esistente"],
            ["",""],
            ["    ","POSTI LETTO"],
            ["7","Mostra la lista dei reparti con codice del reparto e disponibilita' dei posti letto"],
            ["8","Aggiunge un nuovo reparto"],
            ["",""],
            ["    ","STRUTTURE"],
            ["9","Mostra i reparti nell'ospedale"],
            ["10","Aggiunge una nuova struttura"],
            ["11","Rimuove una struttura"],
            ["",""],
            ["    ","FUNZIONALITA'"],
            ["12","Mostra la probabilita' di sconto del ticket"],
            ["13","Mostra lo sconto che spetta al paziente"],
            ["14","Calcola la bonta' di adattamento del modello"],
            ["0","Terminare l'esecuzione del programma"]]
    
    print(tabulate(table, tablefmt="pretty", numalign="center"))
    
    print("\nDigita il numero del comando.              \n")

#restituisce risultati query    
def outputResult(myTrueQuery, printable):
    
    myList = list(prolog.query(myTrueQuery))
    
    if not myList:
        if printable:
            print("Nessun risultato trovato.\n") 
        return False
    
    else:
        if printable:
            print(tabulate(myList, headers='keys', tablefmt="pretty", numalign="center"))
        return True