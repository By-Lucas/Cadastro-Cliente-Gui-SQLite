from bibliotecas import *
from usuarios import funcoes

#Gerar relatórios dos clientes
#Gerar relatório do cliente
class relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf") # Nome do PDF
    
    def gerarRelatorioCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoReal = self.ID_entry.get()
        self.nomeReal = self.nome_entry.get()
        self.emailReal = self.email_entry.get()
        self.telefoneReal = self.telefone_entry.get()
        self.cidadeReal = self.cidade_entry.get()
        self.idmt5Real = self.idmt5_entry.get()
        self.senhaReal = self.senha_entry.get()
        self.dataReal = self.data_entry.get()
        self.corretoraReal = self.corretora_entry.get()

        self.c.setFont("Helvetica-Bold", 24) #Fonte pdf e tamanho da letra
        self.c.drawString(200, 790, 'Ficha do cliente') #espacamento pdf e titulo

        #Informacões do cleinte no PDF
        self.c.setFont("Helvetica", 15)
        self.c.drawString(50, 755, f"Todas as informações do cadastro do cliente(a) {self.nomeReal}") 
        self.c.drawString(50, 720, 'Codigo: '+ self.codigoReal)
        self.c.drawString(50, 690, 'Nome do Cliente: '+ self.nomeReal)
        self.c.drawString(50, 660, 'E-mail: '+ self.emailReal)
        self.c.drawString(50, 630, 'Telefone: '+ self.telefoneReal)
        self.c.drawString(50, 600, 'Cidade: '+ self.cidadeReal)
        self.c.drawString(50, 570, 'ID do MT5: '+ self.idmt5Real)
        self.c.drawString(50, 540, 'Senha: '+ self.senhaReal)
        self.c.drawString(50, 510, 'Data: '+ self.dataReal)
        self.c.drawString(50, 480, 'Corretora: '+ self.corretoraReal)


        self.c.showPage()
        self.c.save()
        self.printCliente()
