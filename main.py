import tkinter as tk
from tkinter import messagebox
import sqlite3


class Tarefa:
    def __init__(self, id, descricao, data, hora, local, coletor_id):
        self.id = id
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.local = local
        self.coletor_id = coletor_id

    def abrir_tela(self):
        janela = tk.Toplevel()
        janela.title("Criação de Tarefa")
        Sistema.centralizar_janela(janela, 400, 300)
        tk.Label(janela, text="Bem-vindo, Gestor!",
                 font=("Helvetica", 16)).pack(pady=20)


class Usuario:
    def __init__(self, id, username, password, cpf, email, nome, telefone, tipo):
        self.id = id
        self.username = username
        self.password = password
        self.cpf = cpf
        self.email = email
        self.nome = nome
        self.telefone = telefone
        self.tipo = tipo
        self.conn = sqlite3.connect('data.db')


class Gestor(Usuario):
    def __init__(self, id, username, password, cpf, email, nome, telefone):
        super().__init__(id, username, password, cpf, email, nome, telefone, "Gestor")

    def abrir_tela(self):
        janela = tk.Toplevel()
        janela.title("Tela do Gestor")
        Sistema.centralizar_janela(janela, 400, 300)
        tk.Label(janela, text="Bem-vind o, Gestor!",
                 font=("Helvetica", 16)).pack(pady=20)
        tk.Button(janela, text="Cadastrar Coletor", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.cadastrar_coletor).pack(pady=20)
        tk.Button(janela, text="Criar Tarefa", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.criar_tarefa).pack(pady=30)

    def cadastrar_coletor(self):
        Sistema.abrir_janela_cadastro_gestor(self)

    def criar_tarefa(self):
        Sistema.abrir_janela_criar_tarefa(self)


class Coordenador(Usuario):
    def __init__(self, id, username, password, cpf, email, nome, telefone):
        super().__init__(id, username, password, cpf, email, nome, telefone, "Coordenador")

    def abrir_tela(self):
        janela = tk.Toplevel()
        janela.title("Tela do Coordenador")
        Sistema.centralizar_janela(janela, 400, 300)
        tk.Label(janela, text="Bem-vindo, Coordenador!",
                 font=("Helvetica", 16)).pack(pady=20)


class Coletor(Usuario):
    def __init__(self, id, username, password, cpf, email, nome, telefone, conn=None):
        super().__init__(id, username, password, cpf, email, nome, telefone, "Coletor")
        self.conn = conn

    def abrir_tela(self):
        if self.conn is None:
            print("Erro: Conexão não foi definida.")
            return

        self.janela = tk.Toplevel()
        self.janela.title("Tela do Coletor")
        Sistema.centralizar_janela(self.janela, 400, 400)
        tk.Label(self.janela, text="Bem-vindo, Coletor!",
                 font=("Helvetica", 16)).pack(pady=20)
        # Restante do código continua aqui
        # Adicionar campos para o cadastro de coleta
        tk.Label(self.janela, text="Data da Coleta:",
                 font=("Helvetica", 12)).pack()
        self.data_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.data_entry.pack()

        tk.Label(self.janela, text="Tipo de Material:",
                 font=("Helvetica", 12)).pack()
        self.tipo_material_entry = tk.Entry(
            self.janela, font=("Helvetica", 12))
        self.tipo_material_entry.pack()

        tk.Label(self.janela, text="Quantidade (kg):",
                 font=("Helvetica", 12)).pack()
        self.quantidade_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.quantidade_entry.pack()

        tk.Label(self.janela, text="Local da Coleta:",
                 font=("Helvetica", 12)).pack()
        self.local_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.local_entry.pack()

        # Botão para cadastrar coleta
        tk.Button(self.janela, text="Cadastrar Coleta", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.cadastrar_coleta).pack(pady=20)

    def cadastrar_coleta(self):
        data = self.data_entry.get()
        tipo_material = self.tipo_material_entry.get()
        quantidade = self.quantidade_entry.get()
        local = self.local_entry.get()

        if all([data, tipo_material, quantidade, local]):
            # Inserir os dados da coleta no banco de dados
            self.conn.execute("INSERT INTO coletas (Coletor_id, data, tipo_material, quantidade, local) VALUES (?, ?, ?, ?, ?)",
                              (self.id, data, tipo_material, quantidade, local))
            self.conn.commit()
            messagebox.showinfo("Cadastro de Coleta",
                                "Coleta cadastrada com sucesso!")
        else:
            messagebox.showerror("Cadastro de Coleta",
                                 "Por favor, preencha todos os campos.")

    def abrir_tela(self):
        self.janela = tk.Toplevel()
        self.janela.title("Tela do Coletor")
        Sistema.centralizar_janela(self.janela, 400, 400)
        tk.Label(self.janela, text="Bem-vindo, Coletor!",
                 font=("Helvetica", 16)).pack(pady=20)

        # Adicionar campos para o cadastro de coleta
        tk.Label(self.janela, text="Data da Coleta:",
                 font=("Helvetica", 12)).pack()
        self.data_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.data_entry.pack()

        tk.Label(self.janela, text="Tipo de Material:",
                 font=("Helvetica", 12)).pack()
        self.tipo_material_entry = tk.Entry(
            self.janela, font=("Helvetica", 12))
        self.tipo_material_entry.pack()

        tk.Label(self.janela, text="Quantidade (kg):",
                 font=("Helvetica", 12)).pack()
        self.quantidade_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.quantidade_entry.pack()

        tk.Label(self.janela, text="Local da Coleta:",
                 font=("Helvetica", 12)).pack()
        self.local_entry = tk.Entry(self.janela, font=("Helvetica", 12))
        self.local_entry.pack()

        # Botão para cadastrar coleta
        tk.Button(self.janela, text="Cadastrar Coleta", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.cadastrar_coleta).pack(pady=20)

    def cadastrar_coleta(self):
        data = self.data_entry.get()
        tipo_material = self.tipo_material_entry.get()
        quantidade = self.quantidade_entry.get()
        local = self.local_entry.get()

        if all([data, tipo_material, quantidade, local]):
            # Inserir os dados da coleta no banco de dados
            self.conn.execute("INSERT INTO coletas (Coletor_id, data, tipo_material, quantidade, local) VALUES (?, ?, ?, ?, ?)",
                              (self.id, data, tipo_material, quantidade, local))
            self.conn.commit()
            messagebox.showinfo("Cadastro de Coleta",
                                "Coleta cadastrada com sucesso!")
        else:
            messagebox.showerror("Cadastro de Coleta",
                                 "Por favor, preencha todos os campos.")


class Sistema:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.centralizar_janela(self.root, 500, 200)
        self.root.configure(bg="#f0f0f0")

        self.conn = sqlite3.connect('data.db')
        self.criar_tabelas()
        self.inserir_users_padrao()

        self.username_entry = self.criar_campo(
            self.root, "Nome de usuário:", 30, 30)
        self.password_entry = self.criar_campo(
            self.root, "Senha:", 70, 30, show="*")

        tk.Button(self.root, text="Login", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.login).place(x=80, y=120)
        tk.Button(self.root, text="Cadastrar", bg="#4CAF50", fg="#ffffff", font=(
            "Helvetica", 12), command=self.abrir_janela_cadastro).place(x=150, y=120)

    def criar_tabelas(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS gestor
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT NOT NULL,
                              password TEXT NOT NULL,
                              cpf TEXT NOT NULL UNIQUE,
                              email TEXT NOT NULL,
                              nome TEXT NOT NULL,
                              telefone TEXT NOT NULL)''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS coordenador
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT NOT NULL,
                              password TEXT NOT NULL,
                              cpf TEXT NOT NULL UNIQUE,
                              email TEXT NOT NULL,
                              nome TEXT NOT NULL,
                              telefone TEXT NOT NULL)''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS coletor
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT NOT NULL,
                              password TEXT NOT NULL,
                              cpf TEXT NOT NULL UNIQUE,
                              email TEXT NOT NULL,
                              nome TEXT NOT NULL,
                              telefone TEXT NOT NULL)''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS coletas
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          coletor_id INTEGER NOT NULL,
                          data TEXT NOT NULL,
                          tipo_material TEXT NOT NULL UNIQUE,
                          quantidade REAL NOT NULL,
                          local TEXT NOT NULL,
                          FOREIGN KEY (coletor_id) REFERENCES usuarios(id))''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS tarefa
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descricao TEXT NOT NULL,
                            data DATE NOT NULL,
                            hora TIME NOT NULL,
                            local TEXT NOT NULL,
                            Coletor_id INTEGER NOT NULL,
                            FOREIGN KEY (Coletor_id) REFERENCES usuarios(id))
                          ''')

    # faz o controle dos users padrao
        self.conn.execute('''CREATE TABLE IF NOT EXISTS controle_inserts
                         (tabela TEXT PRIMARY KEY,
                          inserido INTEGER NOT NULL)''')

        self.conn.commit()

    def inserir_users_padrao(self):
        res = self.conn.execute(
            '''SELECT inserido FROM controle_inserts WHERE tabela = 'gestor' ''').fetchone()
        if res is None:
            self.conn.execute('''INSERT INTO gestor (username, password, cpf, email, nome, telefone)
                                VALUES (?, ?, ?, ?, ?, ?)''',
                              ('adminG', 'adminG', '123342456789', 'gestor@email.com', 'Dolenc', '19999999999'))
            self.conn.execute(
                '''INSERT INTO controle_inserts (tabela, inserido) VALUES (?, ?)''', ('gestor', 1))

        res = self.conn.execute(
            '''SELECT inserido FROM controle_inserts WHERE tabela = 'coordenador' ''').fetchone()
        if res is None:
            self.conn.execute('''INSERT INTO coordenador (username, password, cpf, email, nome, telefone)
                                VALUES (?, ?, ?, ?, ?, ?)''',
                              ('admin', 'admin', '12345678901', 'coordenador@email.com', 'Pedro', '12 212121212'))
            self.conn.execute(
                '''INSERT INTO controle_inserts (tabela, inserido) VALUES (?, ?)''', ('coordenador', 1))

        self.conn.commit()

    @staticmethod
    def centralizar_janela(janela, width, height):
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        janela.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def criar_campo(self, janela, texto, y, x, show=None):
        tk.Label(janela, text=texto, bg="#f0f0f0", fg="#333333",
                 font=("Helvetica", 12)).place(x=30, y=y)
        entry = tk.Entry(janela, show=show, font=("Helvetica", 12))
        entry.place(x=250, y=y)
        return entry

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE username=? AND password=?", (username, password, ))
        usuario_data = cursor.fetchone()

        if usuario_data:
            self.abrir_tela_usuario(usuario_data)
        else:
            messagebox.showerror(
                "Login", "Nome de usuário ou senha incorretos.")

    def abrir_tela_usuario(self, usuario_data):
        self.root.withdraw()
        id, username, password, cpf, email, nome, telefone, tipo_usuario = usuario_data

        if tipo_usuario == "Gestor":
            Gestor(id, username, password, cpf,
                   email, nome, telefone).abrir_tela()
        elif tipo_usuario == "Coordenador":
            Coordenador(id, username, password, cpf,
                        email, nome, telefone).abrir_tela()
        elif tipo_usuario == "Coletor":
            Coletor(id, username, password, cpf,
                    email, nome, telefone).abrir_tela()

    def abrir_janela_cadastro(self):
        nova_janela = tk.Toplevel()
        nova_janela.title("Cadastro de Usuário")
        self.centralizar_janela(nova_janela, 400, 400)
        nova_janela.configure(bg="#f0f0f0")

        entries = {}
        campos = ["username", "password", "cpf", "email", "nome", "telefone"]
        y_positions = [30, 60, 90, 120, 150, 180]

        for campo, y in zip(campos, y_positions):
            tk.Label(nova_janela, text=f"{campo.capitalize()}:", bg="#f0f0f0", fg="#333333", font=(
                "Helvetica", 12)).place(x=30, y=y)
            entry = tk.Entry(nova_janela, font=("Helvetica", 12),
                             show="*" if campo == "password" else None)
            entry.place(x=150, y=y)
            entries[campo] = entry

        tk.Label(nova_janela, text="Tipo de Usuário:", bg="#f0f0f0",
                 fg="#333333", font=("Helvetica", 12)).place(x=30, y=210)
        tipo_var = tk.StringVar(value="")

        tipos = ["Gestor", "Coordenador", "Coletor"]
        y_tipo_positions = [210, 240, 270]

        for tipo, y in zip(tipos, y_tipo_positions):
            tk.Radiobutton(nova_janela, text=tipo, bg="#f0f0f0", fg="#333333",
                           variable=tipo_var, value=tipo, font=("Helvetica", 12)).place(x=180, y=y)

        tk.Button(nova_janela, text="Cadastrar", bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12),
                  command=lambda: self.cadastrar_usuario(nova_janela, entries, tipo_var)).place(x=150, y=320)

    @staticmethod
    def abrir_janela_cadastro_gestor(self):
        nova_janela = tk.Toplevel()
        nova_janela.title("Cadastro de Coletor")
        Sistema.centralizar_janela(nova_janela, 400, 400)
        nova_janela.configure(bg="#f0f0f0")

        entries = {}
        campos = ["username", "password", "cpf", "email", "nome", "telefone"]
        y_positions = [30, 60, 90, 120, 150, 180]

        for campo, y in zip(campos, y_positions):
            tk.Label(nova_janela, text=f"{campo.capitalize()}:", bg="#f0f0f0", fg="#333333", font=(
                "Helvetica", 12)).place(x=30, y=y)
            entry = tk.Entry(nova_janela, font=("Helvetica", 12),
                             show="*" if campo == "password" else None)
            entry.place(x=150, y=y)
            entries[campo] = entry

        tk.Button(nova_janela, text="Cadastrar", bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12),
                  command=lambda: Sistema.cadastrar_coletor(self, nova_janela, entries)).place(x=150, y=220)

    @staticmethod
    def abrir_janela_criar_tarefa(self):
        nova_janela = tk.Toplevel()
        nova_janela.title("Criação de tarefa")
        Sistema.centralizar_janela(nova_janela, 400, 400)
        nova_janela.configure(bg="#f0f0f0")

        entries = {}
        campos = ["descricao", "data", "hora", "local", "coletor_id"]
        y_positions = [30, 60, 90, 120, 150]

        for campo, y in zip(campos, y_positions):
            tk.Label(nova_janela, text=f"{campo.capitalize()}:", bg="#f0f0f0", fg="#333333", font=(
                "Helvetica", 12)).place(x=30, y=y)
            entry = tk.Entry(nova_janela, font=("Helvetica", 12),
                             show="*" if campo == "password" else None)
            entry.place(x=150, y=y)
            entries[campo] = entry

        tk.Button(nova_janela, text="Cadastrar", bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12),
                  command=lambda: Sistema.criar_tarefa(self, nova_janela, entries)).place(x=150, y=220)

    @staticmethod
    def criar_tarefa(self, nova_janela, entries):
        descricao = entries['descricao'].get()
        data = entries['data'].get()
        hora = entries['hora'].get()
        local = entries['local'].get()
        coletor_id = entries['coletor_id'].get()

        if all([descricao, data, hora, local, coletor_id]):
            self.conn.execute("INSERT INTO tarefa (descricao, data, hora, local, coletor_id) VALUES (?, ?, ?, ?, ?)",
                              (descricao, data, hora, local, coletor_id))
            self.conn.commit()
            messagebox.showinfo("Cadastro", "Tarefa cadastrada com sucesso!")
            nova_janela.destroy()
        else:
            messagebox.showerror(
                "Cadastro", "Por favor, preencha todos os campos.")

    @staticmethod
    def cadastrar_coletor(self, nova_janela, entries):
        username = entries['username'].get()
        password = entries['password'].get()
        cpf = entries['cpf'].get()
        email = entries['email'].get()
        nome = entries['nome'].get()
        telefone = entries['telefone'].get()
        tipo = "Coletor"

        if all([username, password, cpf, email, nome, telefone, tipo]):
            self.conn.execute("INSERT INTO usuarios (username, password, cpf, email, nome, telefone, tipo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                              (username, password, cpf, email, nome, telefone, tipo))
            self.conn.commit()
            messagebox.showinfo("Cadastro", "Coletor cadastrado com sucesso!")
            nova_janela.destroy()
        else:
            messagebox.showerror(
                "Cadastro", "Por favor, preencha todos os campos.")

    def cadastrar_usuario(self, nova_janela, entries, tipo_var):
        username = entries['username'].get()
        password = entries['password'].get()
        cpf = entries['cpf'].get()
        email = entries['email'].get()
        nome = entries['nome'].get()
        telefone = entries['telefone'].get()
        tipo = tipo_var.get()

        if all([username, password, cpf, email, nome, telefone, tipo]):
            self.conn.execute("INSERT INTO usuarios (username, password, cpf, email, nome, telefone, tipo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                              (username, password, cpf, email, nome, telefone, tipo))
            self.conn.commit()
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            nova_janela.destroy()
        else:
            messagebox.showerror(
                "Cadastro", "Por favor, preencha todos os campos.")


def encerrar_aplicacao():
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    sistema = Sistema(root)
    # Associando a função de encerramento à ação de fechar a janela
    root.protocol("WM_DELETE_WINDOW", encerrar_aplicacao)
    root.mainloop()
