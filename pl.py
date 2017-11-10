# @author Patrick Amaral
# @since 09/11/2017

import pulp
from pulp import *

from tkinter import *
janela = Tk()

def calcular():
    mn1 = float(txtX1m.get())
    mn2 = float(txtX2m.get())
    mn3 = float(txtX3m.get())
    mn4 = float(txtX4m.get())

    s1n1 = float(txtX1S1.get())
    s1n2 = float(txtX2S1.get())
    s1n3 = float(txtX3S1.get())
    s1n4 = float(txtX4S1.get())

    s2n1 = float(txtX1S2.get())
    s2n2 = float(txtX2S2.get())
    s2n3 = float(txtX3S2.get())
    s2n4 = float(txtX4S2.get())

    s3n1 = float(txtX1S3.get())
    s3n2 = float(txtX2S3.get())
    s3n3 = float(txtX3S3.get())
    s3n4 = float(txtX4S3.get())

    b1 = float(txtB1.get())
    b2 = float(txtB2.get())
    b3 = float(txtB3.get())

    myprob = pulp.LpProblem('myprob', pulp.LpMinimize)
    x1 = pulp.LpVariable('x1', 0)
    x2 = pulp.LpVariable('x2', 0)
    x3 = pulp.LpVariable('x3', 0)
    x4 = pulp.LpVariable('x4', 0)

    myprob += mn1 * x1 + mn2 * x2 + mn3 * x3 + mn4 *x4
    myprob += s1n1 * x1 + s1n2 * x2 + s1n3 * x3 + s1n4 * x4 >= b1
    myprob += s2n1 * x1 + s2n2 * x2 + s2n3 * x3 + s2n4 * x4 >= b2
    myprob += s3n1 * x1 + s3n2 * x2 + s3n3 * x3 + s3n4 * x4 >= b3
    myprob.solve()

    X1=x1.value()
    X2=x2.value()
    X3=x3.value()
    X4=x4.value()

    resultado = ((mn1 * X1) + (mn2 * X2) + (mn3 * X3) + (mn4 * X4))
    lblResultado["text"]="x1={}, x2={}, x3={}, x4={}, Z={}".format(X1,X2,X3,X4,resultado)

btnCalcular = Button(janela, width=20, text = "Calcular", command = calcular)
btnCalcular.place(x=260, y=260)

lblLeite = Label(janela, text = "X1 = Quantidade de Leite")
lblLeite.place(x=30, y=20)

lblCarne = Label(janela, text = "X2 = Quantidade de Carne")
lblCarne.place(x=30, y=40)

lblPeixe = Label(janela, text = "X3 = Quantidade de peixe")
lblPeixe.place(x=30, y=60)

lblSalada = Label(janela, text = "X4 = Quantidade de Salada")
lblSalada.place(x=30, y=80)

lblFuncao = Label(janela, text = "Função Objetivo")
lblFuncao.place(x=50, y=100)

txtX1m = Entry(janela, width = 5)
txtX1m.place(x=50, y=120)

lbl = Label(janela, text = "x1 +")
lbl.place(x=100, y=120)

txtX2m = Entry(janela, width = 5)
txtX2m.place(x=135, y=120)

lbl = Label(janela, text = "x2 +")
lbl.place(x=185, y=120)

txtX3m = Entry(janela, width = 5)
txtX3m.place(x=220, y=120)

lbl = Label(janela, text = "x3 +")
lbl.place(x=270, y=120)

txtX4m = Entry(janela, width = 5)
txtX4m.place(x=305, y=120)

lbl = Label(janela, text = "x4")
lbl.place(x=355, y=120)

lblRestricoes = Label(janela, text = "Restrições")
lblRestricoes.place(x=50, y=160)

##Sujeito a linha 1
txtX1S1 = Entry(janela, width = 5)
txtX1S1.place(x=50, y=180)

lbl = Label(janela, text = "x1 +")
lbl.place(x=100, y=180)

txtX2S1 = Entry(janela, width = 5)
txtX2S1.place(x=135, y=180)

lbl = Label(janela, text = "x2 +")
lbl.place(x=185, y=180)

txtX3S1 = Entry(janela, width = 5)
txtX3S1.place(x=220, y=180)

lbl = Label(janela, text = "x3 +")
lbl.place(x=270, y=180)

txtX4S1 = Entry(janela, width = 5)
txtX4S1.place(x=305, y=180)

lbl = Label(janela, text = "x4 >=")
lbl.place(x=355, y=180)

txtB1 = Entry(janela, width = 5)
txtB1.place(x=400, y=180)

#Sujeito a linha 2
txtX1S2 = Entry(janela, width = 5)
txtX1S2.place(x=50, y=200)

lbl = Label(janela, text = "x1 +")
lbl.place(x=100, y=200)

txtX2S2 = Entry(janela, width = 5)
txtX2S2.place(x=135, y=200)

lbl = Label(janela, text = "x2 +")
lbl.place(x=185, y=200)

txtX3S2 = Entry(janela, width = 5)
txtX3S2.place(x=220, y=200)

lbl = Label(janela, text = "x3 +")
lbl.place(x=270, y=200)

txtX4S2 = Entry(janela, width = 5)
txtX4S2.place(x=305, y=200)

lbl = Label(janela, text = "x4 >=")
lbl.place(x=355, y=200)

txtB2 = Entry(janela, width = 5)
txtB2.place(x=400, y=200)

#Sujeito a linha 3
txtX1S3 = Entry(janela, width = 5)
txtX1S3.place(x=50, y=220)

lbl = Label(janela, text = "x1 +")
lbl.place(x=100, y=220)

txtX2S3 = Entry(janela, width = 5)
txtX2S3.place(x=135, y=220)

lbl = Label(janela, text = "x2 +")
lbl.place(x=185, y=220)

txtX3S3 = Entry(janela, width = 5)
txtX3S3.place(x=220, y=220)

lbl = Label(janela, text = "x3 +")
lbl.place(x=270, y=220)

txtX4S3 = Entry(janela, width = 5)
txtX4S3.place(x=305, y=220)

lbl = Label(janela, text = "x4 >=")
lbl.place(x=355, y=220)

txtB3 = Entry(janela, width = 5)
txtB3.place(x=400, y=220)

lbl = Label(janela, text = "Resultado")
lbl.place(x=50, y=300)

lblResultado = Label(janela, text = "")
lblResultado.place(x=50, y=320)


janela.title("Programação Linear Trabalho 4")
janela.geometry("500x600+400+50")
janela.mainloop()