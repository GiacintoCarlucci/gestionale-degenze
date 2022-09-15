import funzionalita as f
import paziente as p
     
#dizionario per definire i comandi disponibili
switcher = {
    "1": f.pazienti,
    "2": f.idonei,
    "3": f.non_idonei,
    "4": f.cerca_paziente,
    "5": f.aggiungi_paziente,
    "6": f.modifica_paziente,
    "7": f.percorsi,
    "8": f.aggiungi_percorso,
    "9": f.strutture,
    "10": f.aggiungi_struttura,
    "11": f.rimuovi_struttura,
    "12": f.probabilita_idoneita,
    "13": f.percentuale_sconto,
    "14": f.bonta_classificatore,
    "-1": f.mainMenu
    }

#funzione per accedere al dizionario
def switch(command):
    return switcher.get(command, f.default)()

#funzione iniziale main
if __name__ == '__main__':
    f.firstMessage()
    f.sodHelp()
    command = "1"
    
    while (command != "0"):
        command = input("Comando inserito -> ")
        
        if(command != "0"):
            switch(command)
    
    f.esci()
        