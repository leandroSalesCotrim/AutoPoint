import pyautogui
import time
from tkinter import *


#This will disable the fail-safe mode to enable 
#the pyautogui to click on the window corner
pyautogui.FAILSAFE = False

hora_atual = time.ctime()
hora_atual = hora_atual.split()

def auto_point():
    def marca_ponto():

        #1-Click to desktop
        pyautogui.click(x=1919, y=1079)

        #2-Click on the "RH_Online" icon
        pyautogui.click(x=164, y=205)

        #3-Press on the "Enter" key
        pyautogui.press("enter")

        #4-Wait 5 seconds till the page loads and
        #Press on "Marcação de ponto" Card
        time.sleep(5)
        pyautogui.click(x=513, y=450)

        #5-Wait 5 seconds till the page loads and
        #Press on "Marcar ponto" Button
        time.sleep(7)
        pyautogui.click(x=949, y=966)

        #6-Wait 2 seconds till the box open and press on "Confirmar" Button
        #time.sleep(2)
        #pyautogui.click(x=1402, y=838)

    time.sleep(2)
    global hora_atual
    global hora_marcada

    while(hora_atual[3] != "14:45:00"):
        #Make "While" wait 1 sec till run again
        time.sleep(1)

        print(f"ainda não\n {hora_atual[3]}")
        hora_atual = time.ctime()
        hora_atual = hora_atual.split()

        if(hora_atual[3] == "14:52:00"):
            marca_ponto()
        
#INTERFACE GRAFICA
def editar_horario(hora):
    janela.destroy()
    abrir_janela()

    global hora_saida
    hora_saida = hora

def abrir_janela2():
    global janela_editar
    janela_editar = Tk()
    janela_editar.title("AutoPoint - Editar")


    titulo_txt2 = Label(janela_editar, text="Defina o horário para bater ponto")
    titulo_txt2.grid(column=0, row=0)

    input_txt1 = Label(janela_editar, text="Horário de entrada: ")
    input_txt1.grid(column=0, row=1)

    input_entrada = Entry(janela_editar)
    input_entrada.grid(column=1, row=1)

    input_txt2 = Label(janela_editar, text="Horário de saida: ")
    input_txt2.grid(column=0, row=2)

    input_saida = Entry(janela_editar)
    input_saida.grid(column=1, row=2)
    
    btn_salvar = Button(janela_editar, text="Salvar" )
    btn_salvar["command"] = lambda btn=btn_salvar: editar_horario(input_saida.get())
    btn_salvar.grid(column=0, row=3)

    janela_editar.mainloop()



def abrir_janela():
    global janela
    janela = Tk()
    janela.title("AutoPoint")

    hora_saida = "00:00:00"

    titulo_txt = Label(janela, text="AutoPoint")
    subtitulo_txt = Label(janela, text="Sistema automatico para bater ponto")
    hora_entrada_txt = Label(janela, text="\n Horario atual de entrada:")
    hora_saida_txt = Label(janela, text=f"\n Horario atual de saida: {hora_saida}")



    titulo_txt.grid(column=0, row=0)
    subtitulo_txt.grid(column=0, row=1)
    hora_entrada_txt.grid(column=0, row=3)
    hora_saida_txt.grid(column=0, row=4)

    btn_iniciar = Button(janela, text="Iniciar", command=auto_point)
    btn_iniciar.grid(column=0, row=2)

    btn_editar = Button(janela, text="Editar", command=abrir_janela2)
    btn_editar.grid(column=0, row=3)
    
    janela.mainloop()

abrir_janela()

