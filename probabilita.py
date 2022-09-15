from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
                                                                    
# Costruizione Rete Bayesiana Percentuale Degenza

#conoscenza dell'eta
eta = BbnNode(Variable(0, 'eta', ['anziano', 'adulto', 'giovane']), [0.70, 0.25, 0.05])

#conoscenza modalità di arrivo
modalitaArrivo = BbnNode(Variable(1, 'modalitaArrivo', ['accompagnato', 'autonomo']), [0.85, 0.15])

#nodo di conoscenza delle informazioni sul paziente (0-1)
infoPaziente = BbnNode(Variable(2, 'infoPaziente', ['prioritario', 'ordinario']),
                          [0.98, 0.02, 0.75, 0.25, 0.6, 0.4, 0.51, 0.49, 0.15, 0.85, 0.05, 0.95])

#dolore percepito dal paziente
dolore = BbnNode(Variable(3, 'dolore', ['intenso', 'lieve']), [0.85, 0.15])

#presenza di disabilità
disabilita = BbnNode(Variable(4, 'disabilita', ['si', 'no']), [0.71, 0.29])

#cartella clinica del paziente (3-4)
cartellaClinica = BbnNode(Variable(5, 'cartellaClinica', ['grave', 'moderata']), [0.99, 0.01, 0.72, 0.28,
                                                                         0.32, 0.68, 0.02, 0.98])

#urgenza complessiva delpaziente (2-5)
urgenza = BbnNode(Variable(6, 'urgenza', ['prioritaria', 'ordinaria']), [0.93, 0.07, 0.83, 0.17,
                                                                        0.52, 0.48, 0.12, 0.88])
#presenza di prescrizione medica
prescrizione = BbnNode(Variable(7, 'prescrizione', ['si', 'no']), [0.95, 0.05])

#presenza di patologie pregresse
patologiePregresse = BbnNode(Variable(8, 'patologiePregresse', ['si', 'no']), [0.85, 0.15])

#nodo di definizione visita paziente (7-8)
visitaMedica = BbnNode(Variable(9, 'visitaMedica', ['degenza', 'giornaliera']), [0.92, 0.08, 0.77, 0.23,
                                                                0.39, 0.61, 0.16, 0.84])

#previsione finale della % di degenza paziente (6-9)
previsioneDegenza = BbnNode(Variable(10, 'previsioneDegenza', ['alta', 'bassa']), [0.95, 0.05, 0.68, 0.32, 
                                                                                             0.51, 0.49, 0.06, 0.94])

bbn = Bbn() \
    .add_node(eta) \
    .add_node(modalitaArrivo) \
    .add_node(infoPaziente) \
    .add_node(dolore) \
    .add_node(disabilita) \
    .add_node(cartellaClinica) \
    .add_node(urgenza) \
    .add_node(prescrizione) \
    .add_node(patologiePregresse) \
    .add_node(previsioneDegenza) \
    .add_edge(Edge(eta, infoPaziente, EdgeType.DIRECTED)) \
    .add_edge(Edge(modalitaArrivo, infoPaziente, EdgeType.DIRECTED)) \
    .add_edge(Edge(dolore, cartellaClinica, EdgeType.DIRECTED)) \
    .add_edge(Edge(disabilita, cartellaClinica, EdgeType.DIRECTED)) \
    .add_edge(Edge(infoPaziente, urgenza, EdgeType.DIRECTED)) \
    .add_edge(Edge(cartellaClinica, urgenza, EdgeType.DIRECTED)) \
    .add_edge(Edge(prescrizione, visitaMedica, EdgeType.DIRECTED)) \
    .add_edge(Edge(patologiePregresse, visitaMedica, EdgeType.DIRECTED)) \
    .add_edge(Edge(visitaMedica, previsioneDegenza, EdgeType.DIRECTED)) \
    .add_edge(Edge(urgenza, previsioneDegenza, EdgeType.DIRECTED))

# Conversione da bbn ad albero
treeCopy = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#domande da porre all'utente
def questionsForPrediction():
    tree = treeCopy.__copy__()

    while True:
        value = input(
            "Indicare le modalità di arrivo in ospedale del paziente:\n"
            "Risposte possibili: (autonomo) (accompagnato) (non so)\n").lower()
        if value in ["autonomo", "accompagnato"]:
            insertDefinedValue(tree, "modalitaArrivo", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(0)

    while True:
        value = input(
            "Indicare eta paziente:\n"
            "Risposte possibili: (giovane) (adulto) (anziano) (non so)\n").lower()
        if value in ["giovane", "adulto", "anziano"]:
            insertDefinedValue(tree, "eta", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(1)

    while True:
        value = input("Il paziente ha patologie pregresse?:\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "patologiePregresse", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(2)

    while True:
        value = input("come valuta il paziente il suo dolore?\n"
                      "Risposte possibili: (intenso) (lieve) (non so)\n").lower()
        if value in ["intenso", "lieve"]:
            insertDefinedValue(tree, "dolore", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(3)
            
    while True:
        value = input("Il paziente presenta disabilita?\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "disabilita", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(4)

    while True:
        value = input("Il paziente e' in possesso di una prescrizione medica?\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "prescrizione", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(5)
            
    print("analizzando le tue risposte...")
    outputPrediction(tree)



#stampa la probabilita' di poter entrare in reparto
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'previsioneDegenza':
            max, min = posteriors.items()
            print(f'[{node} : {max[1]*100:.0f}%]')
            if max[1] < 0.3:
                print("La degenza non e' prevista.\n")
            elif max[1] < 0.45:
                print("Probabilta' bassa, non c'e' urgenza. Si Consiglia al paziente di Consultare il Primario del Reparto\n")
            elif max[1] < 0.6:
                print("Probabilita' media, il paziente deve attendere, il Primario del Reparto e' stato informato\n")
            elif max[1] < 0.8:
                print("Probabilita' alta, il paziente deve essere steso sul lettino e trasportato nel reparto adeguato, il primario avra' la parola finale\n")
            else:
                print("Ricovero Immediato\n")


def infoMessage(number):
    if number == 0:
        print("In questa sezione devi indica come il paziente è arrivato in Ospedale.\n")
    elif number == 1:
        print("In questa sezione devi indicare l'eta' del paziente o cercarla nella sua cartella clinica.\n")
    elif number == 2:
        print("In questa sezione devi indicare se il paziente ha patologie pregresse chiedendo o cercando nella sua cartella clinica\n")
    elif number == 3:
        print("In questa sezione devi indicare chiedendo al paziente quanto valuta il suo dolore se cosciente, altrimenti se incosciente usa il valore 'intenso'.\n")
    elif number == 4:
        print("In questa sezione devi indicare se il paziente presenta delle disabilita\n")
    elif number == 5:
        print("In questa sezione devi indicare se il paziente arrivato in ospedale abbia una prescrizione medica.\n")


