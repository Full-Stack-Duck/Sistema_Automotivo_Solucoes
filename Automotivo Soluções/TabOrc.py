import sqlite3 as sql
from tkinter import messagebox


class Banco():
    database = "banco.db"
    conn = None
    cursor = None
    connected = False

    def connect(self):
        Banco.conn = sql.connect(Banco.database)
        Banco.cursor = Banco.conn.cursor()
        Banco.connected = True

    def disconnect(self):
        Banco.conn.close()
        Banco.connected = False

    def execute(self, sql, parms=None):
        if Banco.connected:
            if parms == None:
                Banco.cursor.execute(sql)
            else:
                Banco.cursor.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return Banco.cursor.fetchall()

    def persist(self):
        if Banco.connected:
            Banco.conn.commit()
            return True
        else:
            return False

# Função para iniciar o banco de dados


def initDB():
    banco = Banco()
    banco.connect()
    banco.execute("CREATE TABLE IF NOT EXISTS orcamentos(id INTEGER PRIMARY KEY AUTOINCREMENT,cliente TEXT NOT NULL, carro TEXT NOT NULL, cpf_cliente TEXT NOT NULL, mecanico TEXT NOT NULL, cpf_mec TEXT NOT NULL, valor REAL NOT NULL, descricao TEXT NOT NULL, status TEXT)")
    banco.persist()
    banco.disconnect()


initDB()


def view():
    banco = Banco()
    banco.connect()
    banco.execute(
        "SELECT id, cliente, carro, valor, descricao FROM orcamentos")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def inserir_orc(cliente, cpf_cliente, carro, nome_mec, cpf_mec, valor, descricao, status):
    banco = Banco()
    try:
        banco.connect()
        banco.execute("INSERT INTO orcamentos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (cliente, carro, cpf_cliente, nome_mec, cpf_mec, valor, descricao, status))
        banco.persist()
        banco.disconnect()
        return messagebox.showinfo('Informe', 'Orçamento cadastrado com sucesso!')
    except:
        return messagebox.showwarning('Atenção', 'Ocorreu um erro no cadastro')


def search(chave=''):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM orcamentos WHERE cliente LIKE '%"
                  + chave+"%' OR carro LIKE '%"
                  + chave+"%' OR valor LIKE '%"
                  + chave+"%' OR descricao LIKE '%"
                  + chave+"%' OR mecanico LIKE '%"
                  + chave+"%' OR id LIKE '%"
                  + chave+"%' ")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def update(cliente, carro, valor, descricao, mecanico, id):
    banco = Banco()
    banco.connect()
    banco.execute("UPDATE orcamentos SET cliente=?, carro=?, valor=?, descricao=? , mecanico=?WHERE id=?",
                  (cliente, carro, valor, descricao, mecanico, id))
    banco.persist()
    banco.disconnect()


def delete(id):
    banco = Banco()
    banco.connect()
    banco.execute("DELETE FROM orcamentos WHERE id=?", (id, ))
    banco.persist()
    banco.disconnect()


def viewClientes():
    banco = Banco()
    banco.connect()
    banco.execute("SELECT idcliente, nome, carro, cpf FROM clientes")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def searchCliente(chave=""):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM clientes WHERE nome LIKE '%"
                  + chave+"%' OR carro LIKE '%"
                  + chave+"%' ")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


## ==============|  VER ORÇAMENTOS  |=============== ##
def populate():
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM orcamentos")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def select_item(id):
    banco = Banco()
    banco.connect()
    banco.execute(
        "SELECT cliente, carro, cpf_cliente, mecanico, cpf_mec, valor, descricao FROM orcamentos WHERE id=?", (id, ))
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def delete_aprov(idorc):
    banco = Banco()
    banco.connect()
    banco.execute("DELETE FROM orcamentos WHERE id=?", (idorc, ))
    banco.persist()
    banco.disconnect()


def filtrar(chave=''):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM orcamentos WHERE cliente LIKE '%"
                  + chave+"%' OR carro LIKE '%"
                  + chave+"%' OR mecanico LIKE '%"
                  + chave+"%' ")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def inserir_ord(cliente, cpf_cliente, carro, mecanico, cpf_mec, valor, descricao, status):
    banco = Banco()
    try:
        banco.connect()
        banco.execute("INSERT INTO ordem VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (cliente, carro, cpf_cliente, mecanico, cpf_mec, valor, descricao, status))
        banco.persist()
        banco.disconnect()
        return messagebox.showinfo('Informe', 'Ordem cadastrada com sucesso!')
    except:
        return messagebox.showwarning('Atenção', 'Ocorreu um erro no cadastro')


def update_status(state, idordem):
    banco = Banco()
    banco.connect()
    banco.execute("UPDATE orcamentos SET status=? WHERE id=?",
                  (state, idordem))
    banco.persist()
    banco.disconnect()
