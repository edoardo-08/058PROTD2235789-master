class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungiContatto(self, nome, cognome, telefono):
        contatto = Contatto(nome, cognome, telefono)
        self.contatti.append(contatto)

    def rimuoviContatto(self, position):
        del self.contatti[position]

    # ricerca la key in nome cognome telefono di ogno contatto
    def cercaContatto(self, key):
        for contatto in self.contatti:
            if contatto.telefono == key:
                print(contatto.nome, contatto.cognome)

    # restituisce una stringa contenente nome cognome e telefono
    def stampaContatto(self, position):
        print(self.contatti[position])

    # restituisce una stringa con elenco dei contatti, uno per riga
    def listaContatti(self):
        for contatto in self.contatti:
            print(contatto)


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono

    def __str__(self):
        return self.nome + ' ' + self.cognome + ' ' + self.telefono


# Creiamo una rubrica telefonica


r = Rubrica()

r.aggiungiContatto("alba", "chiara", "401-754")
print("contatto aggiunto ...")
r.aggiungiContatto("blu", "celeste", "051-442")
print("contatto aggiunto ...")
print("il contatto selezionato è:")
r.stampaContatto(1)
print("i contatti disponibili sono:")
r.listaContatti()
print("il numero inserito è di:")
r.cercaContatto("401-754")
r.rimuoviContatto(0)
print("contatto rimosso ...")
print("i contatti disponibili sono:")
r.listaContatti()
