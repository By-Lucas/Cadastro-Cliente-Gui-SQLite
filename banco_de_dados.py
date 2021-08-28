from os import path
import sqlite3


#conexão com banco de dados sqlite3
# para criar um banco de dados, precisa estar na pasta onde deseja criar
'''conn = sqlite3.connect('clientesMT5.db') 
'''
#criar um banco de dados selecionando a pasta onde desejo criar
#Selecionar caminho onde dese ser criado o banco de dados
#path = r'C:\Users\Juliano\Desktop\Sistema Tkinter e sqlite'
conn = sqlite3.connect('sistema.db') #Criar banco de dados chamando o caminho e o nome do banco de dados

# definindo um cursor
cursor = conn.cursor()

#============== CRIANDO TABELAS ==========================
# criando a tabela (schema) produtos
'''
CREATE_TABLE_PRODUTOS = cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo INTEGER NOT NULL,
        grupo TEXT NOT NULL,
        fornecedor TEXT,
        contato_fornecedor INTEGER NOT NULL,
        data_validade DATE NOT NULL
);
""")
print('Tabela de Produtos criada com sucesso!')

# inserindo dados na tabela produtos ===========================
cursor.execute("""
INSERT INTO produtos (nome, tipo, grupo, fornecedor, contato_fornecedor, data_validade )
VALUES ('Xiaomi 10', 'eletronico','smartfone', 'jose', '74981199190', '22021-08-10')
""")

cursor.execute("""
INSERT INTO produtos (nome, tipo, grupo, fornecedor, contato_fornecedor, data_validade )
VALUES ('Iphone X Pró', 'eletronico','smartfone', 'jose', '74981199190', '22021-08-10')
""")
'''

APAGAR_TABELA_CLIENTES = cursor.execute('DROP TABLE clientes')

# criando a tabela (schema) clientes
CRIAR_TABELA_CLIENTES = cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
        cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT (50)NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        cidade INTEGER NOT NULL,
        idmt5 INTEGER NOT NULL,
        senhamt5 INTEGER NOT NULL,
        vencimento DATE NOT NULL,
        corretora TEXT NOT NULL
);
""")




print('Tabela de Clientes criada com sucesso!')

# criando a tabela (schema) usuarios
CRIAR_TABELA_USUARIOS = cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        data_cadastrada DATE NOT NULL
);
""")
print('Tabela de Usuarios criada com sucesso!')
#============== TABELAS ACIMA CRIADA ==========================

print('Tabelas criada com sucesso.') #Informação quando banco de dados for criado

# SE DESEJAR COLOCAR MAIS INFORMAÇÕES NA TABELA JÁ CRIADA COLCOAR UMAS INFORMÇÕES
# SÓ PRECISAR APAGAR AS 3 ASPAS SIMPES ECRIAR UM NOVO ARQUIVO .py  E COLOCAR O CODIGO ABAIXO

#============== INSERIR DADOS DENTRO DA TABELA ACIMA ==========================

# inserindo dados na tabela clientes ===========================
cursor.execute("""
INSERT INTO clientes (nome, email, telefone , cidade, idmt5, senhamt5, vencimento, corretora )
VALUES ('lucas', 'lucas@email.com', '74981199190', 'CG', '123456789', 'robo123', '2021/12-12', 'Robo Forex')
""")

cursor.execute("""
INSERT INTO clientes (nome, email, telefone , cidade, idmt5, senhamt5, vencimento, corretora )
VALUES ('monica', 'monica@email.com','74981199190', 'CG', '123456789', 'robo123', '2021/12-12', 'Robo Forex')
""")

cursor.execute("""
INSERT INTO clientes (nome, email, telefone , cidade, idmt5, senhamt5, vencimento, corretora )
VALUES ('valdelic', 'valdelic@email.com','74981199190', 'CG', '123456789','robo123', '2021/12-12', 'Robo Forex')
""")


# inserindo dados na tabela usuarios ===========================
cursor.execute("""
INSERT INTO usuarios (nome, senha, email, telefone, data_cadastrada)
VALUES ('lucas', '123','regis@email.com','74981199190', '2021-07-10')
""")

cursor.execute("""
INSERT INTO usuarios (nome, senha, email, telefone, data_cadastrada)
VALUES ('monicaadm','123', 'regis@email.com','74981199190', '2021-07-10')
""")

mostrar = cursor.execute('SELECT * FROM clientes ')
for i in mostrar:
        print(i)

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.') # Se estiver inserido os dados com sucesso


#conn.close() #Desconectar banco de dados
