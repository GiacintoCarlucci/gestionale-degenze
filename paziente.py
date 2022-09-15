from pyswip import Prolog
import percorso as p
import funzionalita as f

prolog = Prolog()
prolog.consult("KB_1.pl") 

#mostra la lista completa dei pazienti 
def patientList():
    
    myTrueQuery= "paziente(ID,IDONEO_TICKET,PERCORSO)"
    f.outputResult(myTrueQuery, True)

#mostra la lista dei pazienti idonei
def suitablePatientList():
    
    myTrueQuery= "paziente(ID,si,PERCORSO)"
    f.outputResult(myTrueQuery, True)
    
#mostra la lista dei pazienti non idonei
def notSuitablePatientList():
    
    myTrueQuery= "paziente(ID,no,PERCORSO)"
    f.outputResult(myTrueQuery, True)
    
#dato l'ID, cerca un paziente
def findPatient():
    
    patientID = ""

    #controllo numero caratteri del codice fiscale inserito
    while(patientID == "" ):
       
        patientID = input("Inserisci il codice fiscale del paziente che vuoi cercare:\n")
        
        if(not len(patientID) == 16):
            print("Valore inserito non valido. Max 16 caratteri!")
            patientID = ""    
            
    str(patientID).lower()
    myTrueQuery= "paziente("+patientID+",IDONEO_TICKET,PERCORSO)"
    f.outputResult(myTrueQuery, True)
    
#inserisce un paziente
def addPatient():
    
    patientID = ""

    #controllo numero caratteri sul codice fiscale inserito
    while(patientID == "" ):
       
        patientID = input("Inserisci il codice fiscale del nuovo paziente:\n")
        patientID = str(patientID).lower()
        queryCheck = "paziente("+patientID+",IDONEO_TICKET,PERCORSO)"
        
        if(not len(str(patientID)) == 16):
            print("Valore inserito non valido. Max 16 caratteri!")
            patientID = ""    
  
    #controllo presenza id nel database
    if(not f.outputResult(queryCheck, False)):

        patientSuitability = ""
        
        #controllo inserimento 'si' o 'no'
        while(patientSuitability != 'si' and patientSuitability != 'no'):
            
            patientSuitability = input("Inserisci se e' idoneo o meno(si/no): ").lower()
            
            if(patientSuitability != 'si' and patientSuitability != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
    
        #inserimento del percorso solo in caso di idoneit�
        if(patientSuitability == 'si'): 
            
            #controllo presenza percorso nel database
            pathFound = False
            
            while(not pathFound):
                
                patientPath = input("Inserisci l'ID del percorso: ")
                checkPath = "percorso("+str(patientPath)+",REPARTO,POSTI_LETTO)"
                pathFound = f.outputResult(checkPath, False)
                
                if (not pathFound):
                    print("Valore inserito non valido, inserire un percorso presente nel database.\n") 
                else:
                    if(p.modifyAvailability(str(patientPath), 0)):
                        queryCheck = "paziente("+patientID+","+patientSuitability+","+str(patientPath)+")"
                    else:
                        print("Disponibilita' posti letto non sufficente \n") 
                                     
        else:
            
            queryCheck = "paziente("+patientID+","+patientSuitability+", null)"
            
        prolog.assertz(queryCheck)
        
        print("Paziente inserito nel database.")
        
    else:
        print("Paziente gia' presente nel database.\n")
       
    
#modifica un paziente esistente
def modifyPatient():
    
    patientID = input("Inserisci il codice fiscale del paziente da modificare:\n")
    patientID = str(patientID).lower()
    queryCheck = "paziente("+patientID+",IDONEO_TICKET,PERCORSO)"
    
    #controllo presenza id nel database
    if(f.outputResult(queryCheck, False)):
        
        lista=list(prolog.query(queryCheck))
        oldPath = p.extractPath(lista, 2)
           
        prolog.retractall(queryCheck)
        
        patientSuitability = ""
        
        #controllo inserimento 'si' o 'no'
        while(patientSuitability != 'si' and patientSuitability != 'no'):
            
            patientSuitability = input("Inserisci se e' idoneo o meno(si/no): ").lower()
            
            if(patientSuitability != 'si' and patientSuitability != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
        #inserimento del percorso solo in caso di idoneita
        if(patientSuitability == 'si'): 
            pathFound = False
            #controllo presenza percorso nel database
            while(not pathFound):
                
                patientPath = input("Inserisci l'ID del percorso: ")
                checkPath = "percorso("+str(patientPath)+",REPARTO,POSTI_LETTO)"
                pathFound = f.outputResult(checkPath, False)
                
                if (not pathFound):
                    
                    print("Valore inserito non valido, inserire un percorso presente nel database.\n") 
                else:
                    #diminuizione della disponibilita nuovo percorso
                    if(p.modifyAvailability(str(patientPath),0)):
                        #aumento disponibilita vecchio percorso
                        queryCheck = "paziente("+patientID+","+patientSuitability+","+str(patientPath)+")"
                    else:
                        print("Disponibilita' posti letto non sufficente \n")         
            
        else:
            
            queryCheck = "paziente("+patientID+","+patientSuitability+", null)"
         
        p.modifyAvailability(str(oldPath), 1)       
        prolog.assertz(queryCheck)
        
        print("Paziente modificato correttamente.")
        
    else:
        print("Paziente non presente nel database.\n")
        
#rimuove un paziente in seguito alla rimozione di una struttura
def removePatientForPath(pathID):
    
    queryCheck = "paziente(ID,IDONEO_TICKET,"+str(pathID)+")"
    patient=list(prolog.query(queryCheck))
    
    for elem in patient:
        
        #controllo presenza reparto nel database
        if(f.outputResult(queryCheck, False)):
            prolog.retractall(queryCheck)
  
