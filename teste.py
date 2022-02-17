from tkinter import *

janela = Tk()
janela.title("AutoPoint")


titulo_txt = Label(janela, text="AutoPoint")
titulo_txt.grid(column=0, row=0)

subtitulo_txt = Label(janela, text="Sistema automatico para bater ponto")
subtitulo_txt.grid(column=0, row=1)

def abrir_janela2():
    janela_editar = Tk()
    janela_editar.title("AutoPoint - Editar")


    titulo_txt2 = Label(janela_editar, text="Defina o horário para bater ponto")
    titulo_txt2.grid(column=0, row=0)

    input_txt1 = Label(janela_editar, text="Horário de entrada: ")
    input_txt1.grid(column=0, row=1)

    input_entrada1 = Entry(janela_editar)
    input_entrada1.grid(column=1, row=1)

    input_txt2 = Label(janela_editar, text="Horário de saida: ")
    input_txt2.grid(column=0, row=2)

    input_entrada2 = Entry(janela_editar)
    input_entrada2.grid(column=1, row=2)
    
    janela_editar.mainloop()

btn_iniciar = Button(janela, text="Iniciar", command=abrir_janela2)
btn_iniciar.grid(column=0, row=2)

btn_editar = Button(janela, text="Editar", command=abrir_janela2)
btn_editar.grid(column=0, row=3)

janela.mainloop()