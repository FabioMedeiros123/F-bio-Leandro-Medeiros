import tkinter as tk
import sqlite3
import pandas as pd

# A criação do banco de dados abaixo foi comentada para não criar o banco 2 vezes

# #Criando o banco de dados -> cadastro_clientes.db é o nome do banco de dados
# conexao = sqlite3.connect('cadastro_clientes.db')
# #Criando cursor para executar comandos em SQL
# cursor = conexao.cursor()
# #Criando a tabela clientes dentro do banco de dados cadastro_clientes usando SQL
# cursor.execute('''CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
# #Fazendo commit
# conexao.commit()
# #Fechando a conexão
# conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect('cadastro_clientes.db')

    #Criando cursor para executar comandos em SQL
    cursor = conexao.cursor()

    #Inserindo informações na tabela clientes dentro do banco de dados cadastro_clientes usando SQL
    cursor.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
                   {
                        'nome':entry_nome.get(),
                        'sobrenome': entry_sobrenome.get(),
                        'email': entry_email.get(),
                        'telefone': entry_telefone.get()
                   }
                   )

    #Fazendo commit
    conexao.commit()

    #Fechando a conexão
    conexao.close()

    #Apagando os campos de cadastro após um cliente se cadastrar
    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")

def exporta_cliente():
    conexao = sqlite3.connect('cadastro_clientes.db')

    #Criando cursor para executar comandos em SQL
    cursor = conexao.cursor()

    #Criando a tabela clientes dentro do banco de dados cadastro_clientes usando SQL
    cursor.execute("SELECT * , oid FROM clientes")

    #Salvando os dados cadastrados no banco de dados em clientes_cadastrados
    clientes_cadastrados = cursor.fetchall()

    #Salvando em um dataframe usando pandas
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome','sobrenome','email','telefone','id_banco'])
    clientes_cadastrados.to_excel('Banco_de_clientes.xlsx')

    #Fazendo commit
    conexao.commit()

    #Fechando a conexão
    conexao.close()


# Criando interface gráfica
janela = tk.Tk()
janela.title("Cadastro de clientes")

#labels
label_nome = tk.Label(janela,text='Nome')
label_nome.grid(row=0, column=0, padx=10,pady=10)

label_sobrenome = tk.Label(janela,text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela,text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela,text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

#Entrys
entry_nome = tk.Entry(janela,text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10,pady=10)

entry_sobrenome = tk.Entry(janela,text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela,text='Email', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela,text='Telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

#Botões
botao_cadastrar = tk.Button(janela,text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_exportar = tk.Button(janela,text='Exportar', command=exporta_cliente)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

janela.mainloop()
