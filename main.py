import pyautogui
import time
from tkinter import *


#This will disable the fail-safe mode to enable 
#the pyautogui to click on the window corner
pyautogui.FAILSAFE = False



hora_saida = "00:00"
hora_entrada = "00:00"

tipo_ponto = ""

def auto_point():
    tempo_atual = time.ctime()
    tempo_atual = tempo_atual.split()
    tempo_atual = tempo_atual[3].split(":",2)
    
    global hora_entrada
    global hora_saida
    global tipo_ponto
    

    def marca_ponto():

        global hora_atual
        global min_atual

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

        if(tipo_ponto == "entrada"):
            time.sleep(10)

            print(tempo_atual)
            auto_point()


    #Pegando tempo atual do sistema e distribuindo em variaveis a hora 
    # e minuto para conversão para quantos segundos o sistema devera ficar
    # em sleep
    

    hora_atual = tempo_atual[0]
    min_atual = tempo_atual[1]
    #seg_atual = tempo_atual[2] sem uso

    tempo_atual_txt = str(hora_atual+":"+min_atual)
    
    if(tempo_atual_txt < hora_entrada):
        
        tipo_ponto = "entrada"

        #Minutos convertidos para segundo + soma dos segundos
        hora_para_seg = (int(hora_entrada.split(":",1)[0]) - int(hora_atual)) * 3600
        min_para_seg = (int(hora_entrada.split(":",1)[1]) - int(min_atual)) * 60

        seg_em_sleep = hora_para_seg + min_para_seg
        print(seg_em_sleep)
        time.sleep(seg_em_sleep)

        while(tempo_atual_txt != hora_entrada):
                #Make "While" wait 1 sec till run again

                print(tempo_atual_txt+" ainda não é hora")
                tempo_atual = time.ctime()
                tempo_atual = tempo_atual.split()
                tempo_atual = tempo_atual[3].split(":",3)

                hora_atual = tempo_atual[0]
                min_atual = tempo_atual[1]
                
                tempo_atual_txt = str(hora_atual+":"+min_atual);

                time.sleep(1)

                if(tempo_atual_txt == hora_entrada):
                    print("Deu a hora")
                    marca_ponto()

    else:
        print("Tempo de saida")
        #Minutos convertidos para segundo + soma dos segundos
        hora_para_seg = (int(hora_saida.split(":",1)[0]) - int(hora_atual)) * 3600
        min_para_seg = (int(hora_saida.split(":",1)[1]) - int(min_atual)) * 60

        seg_em_sleep = hora_para_seg + min_para_seg
        print(seg_em_sleep)
        time.sleep(seg_em_sleep)

        while(tempo_atual_txt != hora_saida):
                #Make "While" wait 1 sec till run again

                print(tempo_atual_txt+" ainda não é hora")
                tempo_atual = time.ctime()
                tempo_atual = tempo_atual.split()
                tempo_atual = tempo_atual[3].split(":",3)

                hora_atual = tempo_atual[0]
                min_atual = tempo_atual[1]
                
                tempo_atual_txt = str(hora_atual+":"+min_atual);

                time.sleep(1)

                if(tempo_atual_txt == hora_saida):
                    print("Deu a hora")
                    marca_ponto()
        
#INTERFACE GRAFICA
def editar_horario(entrada, saida):
    #This function close the actual window and rebuild
    # the main window with the hour what user saved
    janela_editar.destroy()
    janela.destroy()

    global hora_entrada
    global hora_saida
    hora_entrada = entrada
    hora_saida = saida

    abrir_janela()
    

def abrir_janela2():
    global janela_editar

    janela_editar = Tk()
    janela_editar.title("AutoPoint - Editar")

    titulo_txt2 = Label(janela_editar, text="Defina o horário para bater ponto")
    titulo_txt3 = Label(janela_editar, text="Ex: 09:00")
    input_txt1 = Label(janela_editar, text="Horário de entrada: ")
    input_entrada = Entry(janela_editar)
    input_txt2 = Label(janela_editar, text="Horário de saida: ")
    input_saida = Entry(janela_editar)
    btn_salvar = Button(janela_editar, text="Salvar" )

    btn_salvar["command"] = lambda btn=btn_salvar: editar_horario(input_entrada.get(), input_saida.get())

    titulo_txt2.grid(column=0, row=0)
    titulo_txt3.grid(column=0, row=1)
    input_txt1.grid(column=0, row=2)
    input_entrada.grid(column=1, row=2)
    input_txt2.grid(column=0, row=3)
    input_saida.grid(column=1, row=3)
    btn_salvar.grid(column=0, row=4)

    janela_editar.mainloop()

def abrir_janela():
    global janela
    global hora_saida
    global hora_entrada

    janela = Tk()
    janela.title("AutoPoint")


    titulo_txt = Label(janela, text="AutoPoint")
    subtitulo_txt = Label(janela, text="Sistema automatico para bater ponto")
    hora_entrada_txt = Label(janela, text=f"\n Horario atual de entrada: {hora_entrada}")
    hora_saida_txt = Label(janela, text=f"\n Horario atual de saida: {hora_saida}")
    btn_iniciar = Button(janela, text="Iniciar", command=auto_point)
    btn_editar = Button(janela, text="Editar", command=abrir_janela2)



    titulo_txt.grid(column=0, row=0)
    subtitulo_txt.grid(column=0, row=1)
    btn_iniciar.grid(column=0, row=2)
    btn_editar.grid(column=0, row=3)
    hora_entrada_txt.grid(column=0, row=4)
    hora_saida_txt.grid(column=0, row=5)
    
    janela.mainloop()

abrir_janela()

