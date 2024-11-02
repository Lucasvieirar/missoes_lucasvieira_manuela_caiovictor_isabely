import sqlite3  
from tkinter import Toplevel, Frame, Scrollbar 
from tkinter import *
from tkinter import ttk
from datetime import datetime
from update import TelaAtualizacao

class TelaVisualizacao:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.tela_2()
        self.frame_da_tela()
        self.listas()
        self.carregar_dados() 
        self.ordem_data = True  

        # Botões de Update e Delete
        self.botoes_frame = Frame(self.top, bg='#4682B4')
        self.botoes_frame.place(relx=0.05, rely=0.92, relwidth=0.9, relheight=0.05)

        self.botao_update = Button(self.botoes_frame, text="Atualizar", bd=4, bg="#1e3743",
                                  fg='white', font=('verdana', 8, 'bold'), command=self.missao_update)
        self.botao_update.place(relx=0.65, rely=0.2, relwidth=0.15, relheight=0.9)

        self.botao_delete = Button(self.botoes_frame, text="Deletar", bd=4, bg="#1e3743",
                                  fg='white', font=('verdana', 8, 'bold'), command=self.deletar_missao)
        self.botao_delete.place(relx=0.82, rely=0.2, relwidth=0.15, relheight=0.9)

    def tela_2(self):
        self.top.title("Visualização")
        self.top.geometry("900x500")
        self.top.configure(background='#1e3743')
        self.top.resizable(True, True)
        self.top.maxsize(width=1200, height=600)
        self.top.minsize(width=400, height=300)

    def frame_da_tela(self):
        self.frame_1 = Frame(self.top, bd=4, bg='#4682B4', 
                             highlightbackground='#dfe3ee', highlightthickness=4)
        self.frame_1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.85)

        self.label_titulo = Label(self.frame_1, text="Gerenciamento", font=("Verdana", 16, "bold"), bg='#4682B4', fg="white")
        self.label_titulo.place(relx=0.5, rely=0.0, anchor='center')

    def listas(self):
        estilo = ttk.Style()
        estilo.configure("Treeview",
                         background="#1e3743",
                         foreground="white",
                         rowheight=25)
        estilo.configure("Treeview.Heading",
                         background="yellow",
                         foreground="#1e3743",
                         font=("Arial", 10, "bold"))

        self.lista_missao = ttk.Treeview(self.frame_1, height=15, 
                                          columns=('col0','col1', 'col2', 'col3', 'col4', 'col5', 'col6','col7', 'col8', 'col9', 'col10'))
        self.lista_missao.heading("#0", text="")
        self.lista_missao.heading("#1", text="ID")
        self.lista_missao.heading("#2", text="Missão")
        self.lista_missao.heading("#3", text="Data", command=self.ordenar_data)  
        self.lista_missao.heading("#4", text="Destino")
        self.lista_missao.heading("#5", text="Tripulação")
        self.lista_missao.heading("#6", text="Carga")
        self.lista_missao.heading("#7", text="Custo")
        self.lista_missao.heading("#8", text="Custo")
        self.lista_missao.heading("#9", text="Descrição")
        self.lista_missao.heading("#10", text="Status")
        

        # Ajuste do espaço das colunas
        self.lista_missao.column('#0', width=10)
        self.lista_missao.column('#1', width=70)
        self.lista_missao.column('#2', width=70)
        self.lista_missao.column('#3', width=70)
        self.lista_missao.column('#4', width=70)
        self.lista_missao.column('#5', width=70)
        self.lista_missao.column('#6', width=70)
        self.lista_missao.column('#7', width=70)
        self.lista_missao.column('#8', width=70)
        self.lista_missao.column('#9', width=70)
        self.lista_missao.column('#10', width=100)
        

        # Posição
        self.lista_missao.place(relx=0.02, rely=0.1, relwidth=0.93, relheight=0.85)

        # Barra de rolagem
        self.scroolLista = Scrollbar(self.frame_1, orient='vertical', command=self.lista_missao.yview)
        self.lista_missao.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.94, rely=0.1, relwidth=0.05, relheight=0.85)

    def carregar_dados(self):
        conn = sqlite3.connect('missao.db')  
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, data_lancamento, destino, tripulacao, carga_util, custo, duracao, descricao, status FROM missao")  
        registros = cursor.fetchall()

        for registro in registros:
            self.lista_missao.insert('', 'end', values=registro)

        conn.close()

    def ordenar_data(self):
    
        self.ordem_data = not self.ordem_data
        dados = [(self.lista_missao.item(item)['values']) for item in self.lista_missao.get_children()]
    
    
        dados.sort(key=lambda x: datetime.strptime(x[1], "%Y/%m/%d"), reverse=not self.ordem_data)

    
           

    def deletar_missao(self):
        selected_item = self.lista_missao.selection()
        if selected_item:
            item_values = self.lista_missao.item(selected_item[0])['values']
            mission_id = item_values[0]
            conn = sqlite3.connect('missao.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM missao WHERE id=?", (mission_id,))
            conn.commit()
            conn.close()
            self.lista_missao.delete(selected_item)
            print(f"Missão com ID: {mission_id} deletada")
    def missao_update(self):
            TelaAtualizacao(self.top)