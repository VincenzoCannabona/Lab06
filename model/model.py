from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:        #->... annotazione per specificare i valori di ritorno della funzione che ci aspettiamo (non  cambia il comportamento del programma)
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        cnx=get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM automobile")
        lista_automobili=[]
        for row in cursor:
            lista_automobili.append(row)

        cnx.close()
        return lista_automobili if lista_automobili else None   #in py una lista è considerata false se vuota


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM automobile WHERE modello=%s", (modello,))
        lista_automobili_modello=[]
        for row in cursor:
            lista_automobili_modello.append(row)

        cnx.close()
        return lista_automobili_modello if lista_automobili_modello else None
