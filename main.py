import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()
    t.loadDictionary("dictionary.txt")
    txtIn = input("Seleziona un'opzione: ")


    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        entry = input().lower()
        if all(x.isalpha() or x.isspace() for x in entry):
            risultato_lista = t.handleAdd(entry)
            if risultato_lista:
                print(risultato_lista)  # Stamperà ['cnd', 'home']
                print("Aggiunta!")
            else:
                print("Errore: inserire sia la parola che la traduzione.")
        else:
            print("Errore: caratteri non ammessi.")

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?")
        query = input().lower()
        risultato = t.handleTranslate(query)
        if risultato:
            print(risultato)
        else:
            print("Parola non trovata.")

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        query = input().lower()

        # Validazione base per ammettere il carattere '?'
        if all(x.isalpha() or x == '?' for x in query) and query.count('?') == 1:
            risultato_lista = t.handleAdd(query)
            match_trovati = t.handleWildCard(query)

            if match_trovati:
                for parola_aliena, traduzioni in match_trovati:
                    # Stampa la parola aliena (es: rakast.n)
                    print(parola_aliena)
                    # Stampa la lista delle traduzioni (es: ['amo'])
                    print(traduzioni)
            else:
                print("Nessun match trovato.")
        else:
            print("Errore: caratteri non ammessi.")

    if int(txtIn) == 4:
        t.stampaDizionario()

    if int(txtIn) == 5:
        break