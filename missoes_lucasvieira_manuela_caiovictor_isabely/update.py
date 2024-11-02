from tkinter import *
from tkcalendar import DateEntry
import sqlite3

class TelaAtualizacao:
    def __init__(self, master):
        self.top = Toplevel(master)

        self.tela()
        self.frames_da_tela()
        self.funcionalidades()
        self.top.mainloop()

    def tela(self):
        self.top.title("Sistema de Gerenciamento")
        self.top.configure(background='#1e3743')
        self.top.geometry("1000x800")
        self.top.resizable(True, True)
        self.top.maxsize(width=1600, height=800)
        self.top.minsize(width=400, height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.top, bd=4, bg='#4682B4',
                             highlightbackground='#dfe3ee', highlightthickness=4)
        self.frame_1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

    def funcionalidades(self):
        self.titulo = Label(self.frame_1, text="Atualização",
                            font=("Verdana", 16, "bold"), bg='#4682B4', fg="white")
        self.titulo.place(relx=0.5, rely=0.0, anchor='center')

        self.bt_atualizar = Button(self.frame_1, text='Atualizar', bd=4, bg="#1e3743",
                                  fg='white', font=('verdana', 8, 'bold'), command=self.atualizar_dados)
        self.bt_atualizar.place(relx=0.40, rely=0.90, relheight=0.10)

        

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


    def atualizar_dados(self):

        nome = self.missao_entry.get()
        data_lancamento = self.data_entry.get()
        destino = self.destino_entry.get()
        tripulacao = self.tripulacao_entry.get()
        carga_util = self.carga_entry.get()
        duracao = self.duracao_entry.get()
        custo = self.custo_entry.get()
        descricao = self.descricao_entry.get()
        
        


        conn = sqlite3.connect('missao.db')
        cursor = conn.cursor()

        
        try:
            cursor.execute("""
                UPDATE missao
                SET nome = ?, data_lancamento = ?, destino = ?, tripulacao = ?, carga_util = ?, duracao = ?, custo = ?, descricao = ?
                
            """, (nome, data_lancamento, destino, tripulacao, carga_util, duracao, custo, descricao))
            conn.commit()
            print("Dados atualizados com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")
        finally:
            conn.close()

    
