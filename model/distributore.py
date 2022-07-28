class Distributore:
    def __init__(self):
        self.bibite = {}
        self.tessere = {}
        self.colonne = {}

    def aggiungiBibita(self, codice, nome, prezzo):
        self.bibite[codice] = Bibita(codice, nome, prezzo)

    def aggiungiTessera(self, codice, credito):
        self.tessere[codice] = Tessera(codice, credito)

    def aggiungiColonna(self, numero, bibita, quantita):
        self.colonne[numero] = Colonna(numero, bibita, quantita)

    def getPrezzo(self, codiceBevanda):
        print(self.bibite[codiceBevanda].prezzo)

    def getNome(self, codiceBevanda):
        print(self.bibite[codiceBevanda].nome)

    def getCredito(self, codiceTessera):
        print(self.tessere[codiceTessera].credito)

    def eroga(self, codiceBibita, codiceTessera):
        self.tessere[codiceTessera].credito = (self.tessere[codiceTessera].credito - self.bibite[codiceBibita].prezzo)
        for bibita in self.colonne.values():
            if bibita.bibita == codiceBibita:
                bibita.quantita -= 1


class Bibita:
    def __init__(self, codice, nome, prezzo):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return self.nome + ' ' + str(self.prezzo) + '$'


class Tessera:
    def __init__(self, codice, credito):
        self.codice = codice
        self.credito = credito

    def __str__(self):
        return self.codice + ' ' + str(self.credito) + '$'


class Colonna:
    def __init__(self, numero, bibita, quantita):
        self.numero = numero
        self.bibita = bibita
        self.quantita = quantita

    def __str__(self):
        return str(self.numero) + ' ' + self.bibita + ' ' + str(self.quantita)


# Creiamo un distributore dove possiamo prelevare bibite inserendo una tessera

d = Distributore()
d.aggiungiBibita("01", "acqua", 0.5)
d.aggiungiBibita("02", "cocacola", 2.5)
d.aggiungiTessera("ab01",22)
d.aggiungiColonna(1, "01", 5)
d.aggiungiColonna(2, "02", 4)

print("Il distributore ha le seguenti bibite:")
for bibita in d.bibite:
    print(d.bibite[bibita])

print("Tessere e relativo credito disponibile:")
for tessera in d.tessere:
    print(d.tessere[tessera])

print("Codice delle bibite e quantità disponibile:")
for colonna in d.colonne:
    print(d.colonne[colonna])

print("Il nome della bibita selezionata è:")
d.getNome("01")

print("Il prezzo della bibita selezionata è:")
d.getPrezzo("01")

print("Il credito della tessera inserita è:")
d.getCredito("ab01")
print("erogazione bibita...")
d.eroga("01", "ab01")
print("erogazione bibita...")
d.eroga("01", "ab01")
print("Il credito della tessera inserita è:")
d.getCredito("ab01")

print("Codice delle bibite e quantità disponibile:")
for colonna in d.colonne:
    print(d.colonne[colonna])
