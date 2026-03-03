class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, aliena, nuova_traduzione):
        parola = aliena.lower()

        if parola not in self.dizionario:
            self.dizionario[parola] = []

        for t in nuova_traduzione:
            t_low = t.lower()
            if t_low not in self.dizionario[aliena]:
                self.dizionario[aliena].append(t_low)

    def translate(self, aliena):
        parola = aliena.lower()
        if parola in self.dizionario:
            traduzione = self.dizionario[parola][0:]
            return [parola] + traduzione
        return None

    def translateWordWildCard(self, query):
        import re
        pattern = query.lower().replace("?", ".")
        risultati = []

        for aliena, traduzioni in self.dizionario.items():
            if re.fullmatch(pattern, aliena):
                risultati.append((aliena, traduzioni))
        return risultati


    def stampaTutto(self):
        if not self.dizionario:
            print("Il dizionario è vuoto.")
            return

        for aliena, traduzioni in self.dizionario.items():
            # Creiamo una lista di parole con gli apici: ["'trad1'", "'trad2'"]
            trads_con_apici = [f"'{t}'" for t in traduzioni]
            # Uniamo tutto con una virgola e uno spazio
            stringa_traduzioni = ", ".join(trads_con_apici)
            print(f"'{aliena}', {stringa_traduzioni}")


    def test_modulo(self):
        parola1="kassa"


    if __name__ == '__main__':
        test_modulo()