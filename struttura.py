from pyswip import Prolog
from tabulate import tabulate
import percorso as p
import funzionalita as f

prolog = Prolog()
prolog.consult("KB_1.pl") 

#mostra la lista completa delle strutture
def structList():
    
    myTrueQuery= "struttura(REPARTO,PIANO,PRIMARIO)"
    f.outputResult(myTrueQuery, True)

#utile per aggiungere una nuova struttura
def addStruct():
     
    structDepartment = ""
    
  #messaggio errore nel caso sono presenti dei numeri nel reparto inserito 
    while(structDepartment == ""):
       
        structDepartment = input("Inserisci il reparto:\n").lower()
        queryCheck = "struttura("+str(structDepartment)+",PIANO,PRIMARIO)"
            
        if(any(chr.isdigit() for chr in str(structDepartment))): 
            structDepartment=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
    
   
    #controllo presenza reparto nel database
    if(not f.outputResult(queryCheck, False)):
        
        floor = input("Inserisci il piano del reparto: ")
                
        primary = input("Inserisci il primario: ").lower()

        queryCheck = "struttura("+str(structDepartment)+","+str(floor)+","+str(primary)+")"

        prolog.assertz(queryCheck)
        
        print("Struttura inserita nel database.")
        
    else:
        print("Struttura gia' presente nel database.\n")
        
#rimuove una struttura esistente
def removeStruct():
    
    structDepartment = input("Inserisci il reparto da eliminare:\n").lower()
    queryCheck = "struttura("+str(structDepartment)+",PIANO,PRIMARIO)"
    
    #controllo presenza reparto nel database
    if(f.outputResult(queryCheck, False)):
        prolog.retractall(queryCheck)
        print("La struttura e' stata eliminata correttamente.\n")
        
        p.removePath(structDepartment)
    else:
        print("Struttura non presente nel database.\n")
        