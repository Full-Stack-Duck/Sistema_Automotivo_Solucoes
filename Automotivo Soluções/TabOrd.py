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
    banco.execute("CREATE TABLE IF NOT EXISTS ordem(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT NOT NULL, carro TEXT NOT NULL, cpf_cliente TEXT NOT NULL, mecanico TEXT NOT NULL, cpf_mec TEXT NOT NULL, valor REAL NOT NULL, descricao TEXT NOT NULL, status TEXT)")
    banco.persist()
    banco.disconnect()


initDB()


def view():
    banco = Banco()
    banco.connect()
    banco.execute(
        "SELECT id, cliente, carro, cpf_cliente, mecanico, cpf_mec, valor, descricao, FROM ordem")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def filtrar(chave=''):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM ordem WHERE cliente LIKE '%"
                  + chave+"%' OR carro LIKE '%"
                  + chave+"%' OR mecanico LIKE '%"
                  + chave+"%' OR status LIKE '%"
                  + chave+"%' ")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def update(status, idordem):
    try:
        banco = Banco()
        banco.connect()
        banco.execute("UPDATE ordem SET status=? WHERE id=?",
                      (status, idordem))
        banco.persist()
        banco.disconnect()
        return messagebox.showinfo('Informe', 'Ordem concluída com sucesso!')
    except:
        return messagebox.showwarning('Atenção', 'Ocorreu um erro na atualização')


def delete(idordem):
    banco = Banco()
    banco.connect()
    banco.execute("DELETE FROM ordem WHERE id=?", (idordem, ))
    banco.persist()
    banco.disconnect()


## ==============|  GERENCIAR ORÇAMENTOS  |=============== ##
def inserir_ord(cliente, cpf_cliente, carro, mecanico, cpf_mec, valor, descricao):
    banco = Banco()
    try:
        banco.connect()
        banco.execute("INSERT INTO ordem VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (cliente, carro, cpf_cliente, mecanico, cpf_mec, valor, descricao))
        banco.persist()
        banco.disconnect()
        return messagebox.showinfo('Informe', 'Ordem cadastrada com sucesso!')
    except:
        return messagebox.showwarning('Atenção', 'Ocorreu um erro no cadastro')


def populate(self):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM ordem")
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas


def select_item(id):
    banco = Banco()
    banco.connect()
    banco.execute("SELECT * FROM orcamentos WHERE id=?", (id, ))
    linhas = banco.fetchall()
    banco.disconnect()
    return linhas
