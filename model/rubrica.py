class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungiContatto(self, nome, cognome, telefono):
        self.contatti.append((nome, cognome, telefono))

    def rimuoviContatto(self, position):
        del self.contatti[position]

    def cercaContatto(self, key):
        pass

    def stampaContatto(self, position):
        return self.contatti[position]

    def listaContatti(self):
        for i in self.contatti:
            print(i)


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
