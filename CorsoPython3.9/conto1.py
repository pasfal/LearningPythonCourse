class ContoCorrente:
    def __init__(self, nome, conto, importoIniziale):
        self.nome = nome
        self.conto = conto
        self.saldo = importoIniziale
    
    def preleva(self, importoPrelevato):
        self.saldo -= importoPrelevato
    
    def deposita(self, importoDaDepositare):
        self.saldo += importoDaDepositare
    
    def descrizione(self):
        print(f"Nome titolare del conto: {self.nome} - Numero conto: {self.conto} - Saldo: {self.saldo}")

contoCorrente1 = ContoCorrente("Mario Rossi", "IT12345", 150.25)
contoCorrente2 = ContoCorrente("Anna Verdi", "IT57432", 650.70)

contoCorrente1.descrizione()
contoCorrente2.descrizione()

contoCorrente1.preleva(25)
contoCorrente1.descrizione()
contoCorrente1.deposita(450.75)
contoCorrente1.descrizione()

contoCorrente2.preleva(50.70)
contoCorrente2.descrizione()
contoCorrente2.deposita(400)
contoCorrente2.descrizione()