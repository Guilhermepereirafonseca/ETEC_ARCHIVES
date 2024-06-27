import tkinter as tk

import psycopg2

from tkinter import messagebox


# Função para conectar ao PostgreSQL

def conectar_postgresql():

    try:

        conn = psycopg2.connect(

            dbname="postgres",

            user="postgres",

            password="123456",

            host="localhost",

            port="5432"

        )

        return conn

    except Exception as e:

        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao PostgreSQL: {e}")

        return None


# Função para inserir dados no PostgreSQL

def inserir_dados(conn, nome, idade):

    try:

        cursor = conn.cursor()

        sql = "INSERT INTO tabela_exemplo (nome, idade) VALUES (%s, %s)"

        cursor.execute(sql, (nome, idade))

        conn.commit()

        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")

        return True

    except Exception as e:

        messagebox.showerror("Erro ao Inserir Dados", f"Erro ao inserir dados: {e}")

        return False


# Função para carregar os dados da tabela

def carregar_dados(conn):

    try:

        cursor = conn.cursor()

        cursor.execute("SELECT nome, idade FROM tabela_exemplo")

        dados = cursor.fetchall()

        return dados

    except Exception as e:

        messagebox.showerror("Erro ao Carregar Dados", f"Erro ao carregar dados: {e}")

        return []


# Função para atualizar a lista de visualização

def atualizar_lista(lista, conn):

    lista.delete(0, tk.END)

    dados = carregar_dados(conn)

    for nome, idade in dados:

        lista.insert(tk.END, f"{nome} - {idade}")


# Função para criar a interface gráfica

def criar_tela():

    root = tk.Tk()

    root.title("Inserir e Visualizar Dados PostgreSQL")

   

    # Labels e entradas de texto

    tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10)

    tk.Label(root, text="Idade:").grid(row=1, column=0, padx=10, pady=10)

   

    entry_nome = tk.Entry(root)

    entry_nome.grid(row=0, column=1, padx=10, pady=10)

   

    entry_idade = tk.Entry(root)

    entry_idade.grid(row=1, column=1, padx=10, pady=10)

   

    # Botão para inserir dados

    def inserir():

        nome = entry_nome.get()

        idade = entry_idade.get()

       

        conn = conectar_postgresql()

        if conn:

            if inserir_dados(conn, nome, idade):

                atualizar_lista(lista_visualizacao, conn)

                conn.close()

       

        entry_nome.delete(0, tk.END)

        entry_idade.delete(0, tk.END)

   

    btn_inserir = tk.Button(root, text="Inserir Dados", command=inserir)

    btn_inserir.grid(row=2, columnspan=2, padx=10, pady=10)

   

    # Lista para visualização dos dados inseridos

    lista_visualizacao = tk.Listbox(root)

    lista_visualizacao.grid(row=3, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

   

    # Atualizar lista inicialmente ao carregar a tela

    conn = conectar_postgresql()

    if conn:

        atualizar_lista(lista_visualizacao, conn)

        conn.close()

   

    root.mainloop()


# Chamando a função para criar a tela

criar_tela()