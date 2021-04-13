class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):
    def __init__(self, nome, conto, importoIniziale):
        super().__init__(nome, conto)
        self.__saldo = importoIniziale
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuovoSaldo):
       self.preleva(self.__saldo)
       self.deposita(nuovoSaldo)

    def preleva(self, importoPrelevato):
        self.__saldo -= importoPrelevato
    
    def deposita(self, importoDaDepositare):
        self.__saldo += importoDaDepositare
    
    def descrizione(self):
        print(f"Nome titolare del conto: {self.nome} - Numero conto: {self.conto} - Saldo: {self.__saldo}")


class GestoreContiCorrenti:    
    @staticmethod 
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)



contoCorrente1 = ContoCorrente("Mario Rossi", "IT12345", 150.25)
contoCorrente2 = ContoCorrente("Anna Verdi", "IT57432", 650.70)

contoCorrente1.descrizione()
contoCorrente2.descrizione()

contoCorrente1.preleva(25)
contoCorrente1.descrizione()
contoCorrente1.deposita(450.75)
contoCorrente1.descrizione()
print(f"\nValore della property Saldo per Mario Rossi: {contoCorrente1.saldo} \n")

contoCorrente2.preleva(50.70)
contoCorrente2.descrizione()
contoCorrente2.deposita(400)
contoCorrente2.descrizione()
print(f"\nValore della property Saldo per Anna Verdi: {contoCorrente2.saldo} \n")

GestoreContiCorrenti.bonifico(contoCorrente2, contoCorrente1, 200)
print(f"Saldo conto corrente #1: {contoCorrente1.saldo} - Saldo conto corrente #2: {contoCorrente2.saldo}")

#contoCorrente1.saldo = 5000
#print(contoCorrente1.saldo)