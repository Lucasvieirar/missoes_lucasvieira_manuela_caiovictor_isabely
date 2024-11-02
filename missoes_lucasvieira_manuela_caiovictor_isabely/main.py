from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from tela import TelaVisualizacao 
import sqlite3
from bd import Database




class Application:
    def __init__(self):
        self.db = Database()  
        self.root = Tk()
        self.tela()
        self.frames_da_tela()
        self.funcionalidades()
        self.root.mainloop()

    def tela(self):
        self.root.title("Sistema de Gerenciamento")
        self.root.configure(background='#1e3743')
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        self.root.maxsize(width=1600, height=800)
        self.root.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#4682B4',
                             highlightbackground='#dfe3ee', highlightthickness=4)
        self.frame_1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

    def funcionalidades(self):
        self.titulo = Label(self.frame_1, text="Cadastro da Missão",
                            font=("Verdana", 16, "bold"), bg='#4682B4', fg="white")
        self.titulo.place(relx=0.5, rely=0.0, anchor='center')

        self.bt_cadastro = Button(self.frame_1, text='Cadastrar', bd=4, bg="#1e3743",
                                  fg='white', font=('verdana', 8, 'bold'), command=self.cadastrar)
        self.bt_cadastro.place(relx=0.40, rely=0.90, relheight=0.10)

        self.bt_visualizar = Button(self.frame_1, text='Visualizar', bg="#1e3743",
                                     fg='white', font=('verdana', 8, 'bold'), command=self.tela_visualizacao)
        self.bt_visualizar.place(relx=0.80, rely=0.90, relwidth=0.15, relheight=0.10)

        # Label missão
        self.lb_missao = Label(self.frame_1, text="Missão", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_missao.place(relx=0.10, rely=0.03)

        # Input Entry missão
        self.missao_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.missao_entry.place(relx=0.10, rely=0.06, relwidth=0.25)

        # Label data
        self.lb_data = Label(self.frame_1, text="Data", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_data.place(relx=0.40, rely=0.03)

        # Input Entry data
        self.data_entry = DateEntry(self.frame_1, date_pattern='yyyy/mm/dd', width=12, background='#1e3743', 
                                     foreground='white', borderwidth=2, bg='#4682B4', font=('verdana', 10, 'bold'))
        self.data_entry.place(relx=0.40, rely=0.06, relwidth=0.175)

        # Label destino
        self.lb_destino = Label(self.frame_1, text="Destino", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_destino.place(relx=0.65, rely=0.03)

        # Input Entry destino
        self.destino_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.destino_entry.place(relx=0.65, rely=0.06, relwidth=0.3)

        # Label tripulação
        self.lb_tripulacao = Label(self.frame_1, text="Tripulação", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_tripulacao.place(relx=0.10, rely=0.32)

        # Input Entry tripulação
        self.tripulacao_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.tripulacao_entry.place(relx=0.10, rely=0.36, relwidth=0.4, relheight=0.1)

        # Label carga
        self.lb_carga = Label(self.frame_1, text="Carga", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_carga.place(relx=0.65, rely=0.32)

        # Input Entry carga
        self.carga_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.carga_entry.place(relx=0.65, rely=0.36, relwidth=0.3, relheight=0.1)

        # Label custo
        self.lb_custo = Label(self.frame_1, text="Custo", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_custo.place(relx=0.10, rely=0.14)

        # Input Entry custo
        self.custo_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.custo_entry.place(relx=0.10, rely=0.18, relwidth=0.1)

        # Label duração
        self.lb_duracao = Label(self.frame_1, text="Duração", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_duracao.place(relx=0.65, rely=0.12)
        
        # Input Entry duração
        self.duracao_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.duracao_entry.place(relx=0.65, rely=0.16, relwidth=0.1)

        # Label descricao
        self.lb_descricao = Label(self.frame_1, text="Descrição da missão", bg='#4682B4', fg='#1e3743', font=('verdana', 10, 'bold'))
        self.lb_descricao.place(relx=0.10, rely=0.50)

        # Input Entry descricao
        self.descricao_entry = Entry(self.frame_1, fg='#1e3743', font=('verdana', 10, 'bold'))
        self.descricao_entry.place(relx=0.10, rely=0.56, relwidth=0.8, relheight=0.2)

    def cadastrar(self):
        nome = self.missao_entry.get()
        data_lancamento = self.data_entry.get()
        destino = self.destino_entry.get()
        tripulacao = self.tripulacao_entry.get()
        carga_util = self.carga_entry.get()
        duracao = self.duracao_entry.get()
        custo = self.custo_entry.get()
        descricao = self.descricao_entry.get()
        status = 'Ativo'  

        if nome and data_lancamento and destino: 
            self.db.insert_missao(nome, data_lancamento, destino, tripulacao, carga_util, duracao, custo, descricao, status)
            self.clear_entries()
        else:
            print("Preencha todos os campos obrigatórios.")

    def clear_entries(self):
        self.missao_entry.delete(0, END)
        self.data_entry.set_date('')  
        self.destino_entry.delete(0, END)
        self.tripulacao_entry.delete(0, END)
        self.carga_entry.delete(0, END)
        self.duracao_entry.delete(0, END)
        self.custo_entry.delete(0, END)
        self.descricao_entry.delete(0, END)

    def tela_visualizacao(self):
        TelaVisualizacao(self.root)

Application()
