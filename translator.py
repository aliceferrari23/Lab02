import dictionary as d
class Translator:

    def __init__(self):
        self.dizionario = d.Dictionary()

    def printMenu(self):
        print("------------------------------")
        print(" Translator Alien-Italian")
        print("------------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("------------------------------")

    def loadDictionary(self, dict):
        with open(dict, 'r') as f:
            for riga in f:
                parti = riga.strip().split()
                if len(parti) >= 2:
                    self.dizionario.addWord(parti[0], parti[1:])

    def handleAdd(self, entry):
        parti = entry.split()
        if len(parti) >= 2:
            parola_aliena = parti[0]
            traduzioni_multiple = parti[1:]
            self.dizionario.addWord(parola_aliena, traduzioni_multiple)
            return self.dizionario.translate(parola_aliena)
        return None

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)

    def stampaDizionario(self):
        self.dizionario.stampaTutto()