import tkinter
import mysql.connector

#Conectando com o banco de dados
connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="bdescola"
)

#Função para pedir e gravar os dados 
def gravar_dados():
    cursor = connection.cursor()
    sql="INSERT INTO aluno (nome,endereco,telefone) VALUES (%s, %s, %s)"
    data = (
        entrada1.get(),
        entrada2.get(),
        entrada3.get()
    )
    cursor.execute(sql, data)
    connection.commit()

#Função para pesquisar um registro no banco e verificar suas informações e chave primaria, permitindo atualizar ou excluir o cadastro
def pesquisar_dados():
    cursor = connection.cursor()
    sql="select codigo,nome,endereco,telefone from aluno where nome like'"+entrada1.get()+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    entrada2.insert(0, result[2])
    entrada3.insert(0, result[3])
    entrada5.insert(0, result[0])

#Função para excluir um registro do banco de dados
def atualizar_dados():
    cursor = connection.cursor()
    sql = "update aluno set nome=%s,endereco=%s,telefone=%s where codigo = "+ entrada5.get()
    data = (
        entrada1.get(),
        entrada2.get(),
        entrada3.get()
    )
    cursor.execute(sql, data)
    connection.commit()
    
#Função para excluir um registro do banco de dados    
def excluir_dados():
    cursor = connection.cursor()
    sql="delete from aluno where codigo like'"+entrada5.get()+"'"
    cursor.execute(sql)   
    connection.commit() 

#Criação da janela
janela = tkinter.Tk()
janela.title("Banco de dados Escola")
janela.geometry('600x400')
texto = tkinter.Label(janela, text="Cadastro de Aluno")
texto.grid(column=0, row=0, padx=10, pady=10)

#Caixa de texto e entrada do nome do aluno
texto2 = tkinter.Label(text="Nome do aluno: ")
texto2.grid(column=0, row=1)
entrada1 = tkinter.Entry(width=50)
entrada1.grid(column=1, row=1)

#Caixa de texto e entrada do endereço do aluno
texto3 = tkinter.Label(text="Endereço: ")
texto3.grid(column=0, row = 3)
entrada2 = tkinter.Entry(width=50)
entrada2.grid(column=1, row=3)

#Caixa de texto e entrada do telefone do aluno
texto4 = tkinter.Label(text="Telefone: ")
texto4.grid(column=0, row=5)
entrada3 = tkinter.Entry(width=50)
entrada3.grid(column=1, row=5)

#Id
entrada5 = tkinter.Entry(width=10)
entrada5.grid(column=1, row=0)

#Botão para gravar registro dos dados do aluno no banco de dados
botao= tkinter.Button(janela, text="Gravar Registro", command=gravar_dados)
botao.grid(column=0, row=7, padx=10, pady=10)

#Botão para atualizar registro dos dados do aluno no banco de dados
botao2 = tkinter.Button(janela, text="Atualizar Registro", command=atualizar_dados)
botao2.grid(column=1, row=7)

#Botão para pesquisar um registro dos dados de um aluno no banco de dados
botao3= tkinter.Button(janela, text="Pesquisar registro", command=pesquisar_dados)
botao3.grid(column=2, row=1, padx=10, pady=10)

#Botão para excluir registro dos dados do aluno no banco de dados
botao4 = tkinter.Button(janela, text="Excluir Registro", command=excluir_dados)
botao4.grid(column=2, row=7)

janela.mainloop()