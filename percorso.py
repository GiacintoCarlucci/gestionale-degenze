
from pyswip import Prolog
import paziente as p
import funzionalita as f

prolog = Prolog()
prolog.consult("KB_1.pl") 

#mostra la lista completa dei percorsi 
def pathList():
    
    myTrueQuery= "percorso(CODICE_REPARTO,REPARTO,POSTI_LETTO)"
    f.outputResult(myTrueQuery, True)
    
def addPath():
    
    pathID = ""
    
    #controllo numero caratteri del codice reparto
    while(not 1 <= len(str(pathID)) <= 3):
       
        pathID = input("Inserisci codice reparto:\n").lower()
            
        queryCheck = "percorso("+str(pathID)+",REPARTO,POSTI_LETTO)"
       
        #messaggio errore nel caso la lunghezza dell'ID non dovesse rientrare nel range (1-3)   
        if(not 1 <= len(str(pathID)) <= 3):
            print("Valore inserito non valido. Max 3 caratteri!\n")
         
        #messaggio errore nel caso sono presenti dei numeri nell'ID inserito   
        if(any(chr.isdigit() for chr in str(pathID))): 
            pathID=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
            
    #controllo presenza id nel database
    if(not f.outputResult(queryCheck, False)):
        structFound = False
            #controllo presenza struttura nel database
        while(not structFound):
                
            struct = input("Inserisci il reparto: ").lower()
            checkStruct = "struttura("+str(struct)+",PIANO,PRIMARIO)"
            structFound = f.outputResult(checkStruct, False)
                
            if (not structFound):
                    
                print("Valore inserito non valido, inserire un percorso presente nel database.\n") 
         
        availability = ""
        
        #controllo inserimento disponibilita
        while(availability == ""):
            
            availability = input("Inserisci la disponibilita' dei posti letto: ")
            
            if(not availability.isdigit()):
                
                print("Valore inserito non valido, inserire solo valori numerici.\n")
                availability = ""
        
        queryCheck = "percorso("+str(pathID)+","+struct+","+availability+")"
        prolog.assertz(queryCheck)
        
        print("Percorso inserito nel database.")
        
    else:
        print("Percorso gia' presente nel database.\n")
        
#rimuove un percorso in seguito alla rimozione di una struttura
def removePath(structDepartment):
    pathID=""
    queryCheck = "percorso(CODICE_REPARTO,"+str(structDepartment)+",POSTI_LETTO)"
    
    #controllo presenza reparto nel database
    if(f.outputResult(queryCheck, False)):
        
        path=list(prolog.query("percorso(CODICE_REPARTO,"+str(structDepartment)+",_)"))
       
        f.outputResult(queryCheck, True)
        
        for elem in path:
            pathID = str(path[0]).split("'")
            p.removePatientForPath(pathID[3])
            prolog.retractall(queryCheck)

def modifyAvailability(ID,operation):
    
    queryCheck = "percorso("+str(ID)+",REPARTO,POSTI_LETTO)"
    destination=list(prolog.query(queryCheck))
    #salvataggio occorrenze di REPARTI e POSTI_LETTO
    for elem in destination:
        infoDestination = extractPath(destination, operation)

        if(infoDestination[1] != 0):
            prolog.retractall(queryCheck)
            prolog.assertz("percorso("+str(ID)+","+str(infoDestination[0])+","+str(infoDestination[1])+")")
            return True
        else:
            return False
    
def extractPath(list, operation):
        listInfo=[]
        destinationID = str(list[0]).split("'")
        listInfo.append(destinationID[3])
        
        if(operation == 0):
            listInfo.append(int(destinationID[6][destinationID[6].find(' ')+1:destinationID[6].find('}')]) - 1)
            return listInfo

        elif(operation == 1):
            listInfo.append(int(destinationID[6][destinationID[6].find(' ')+1:destinationID[6].find('}')]) + 1)
            return listInfo
        
        else:
            return destinationID[7]
        