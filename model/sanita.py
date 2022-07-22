class Sanita:
    def __init__(self):
        self.dottori = {}
        self.pazienti = {}

    def aggiungiDottore(self, nome, cognome, codiceFiscale, matricola):
        self.dottori = Dottore(matricola,nome, cognome, codiceFiscale)

    def aggiungiPaziente(self, nome, cognome, codiceFiscale, codicePaziente):
        self.pazienti[codicePaziente] = [codiceFiscale, nome, cognome]

    # restituisce il paziente dato il codice
    def getPaziente(self, codicePaziente):
        print(self.pazienti[codicePaziente])

    # restituisce il medico data la matricola
    def getDottore(self, matricola):
        print(self.dottori[matricola])

    # assegna un aziente a un medico
    def assegnaMedico(self, matricola, codice):
        matricola.pazienti.append(self.pazienti[codice.codice])
        codice.dottori.append(self.dottori[matricola.matricola])

    # restituisce una stringa contenente
    # l'elenco dei pazienti assegnati a un medico

    def getPazienti(self, matricola):
        print(self.dottori[matricola])

# sia il dottore che il paziente hanno
# come attributo nome cognome e codice fiscale
# il paziente ha un codice univoco e il dottore una matricola


class Dottore:
    def __init__(self, matricola):
        self.matricola = matricola
        self.pazienti = []


class Paziente:
    def __init__(self, codice):
        self.codice = codice
        self.dottori = []


s = Sanita()

s.aggiungiDottore("mario", "rossi", "MRRSS000", "0000")
print(s.dottori)

s.aggiungiPaziente("Sara", "Salice", "SRSLC3657", "1000")
s.aggiungiPaziente("elio", "trini", "ELTRC3657", "1001")
print(s.pazienti)

s.getDottore("0000")
s.getPaziente("1000")

dottore1 = Dottore("0000")
paziente1 = Paziente("1000")
paziente2 = Paziente("1001")

s.assegnaMedico(dottore1, paziente1)

s.assegnaMedico(dottore1, paziente2)

print(dottore1.pazienti)
print(paziente1.dottori)
print(paziente2.dottori)
