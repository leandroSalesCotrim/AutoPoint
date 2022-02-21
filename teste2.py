import time

hora_saida = "15:38"

# #Pegando tempo atual do sistema e distribuindo em variaveis a hora 
# # e minuto para conversão para quantos segundos o sistema devera ficar
# # em sleep
tempo_atual = time.ctime()
tempo_atual = tempo_atual.split()
tempo_atual = tempo_atual[3].split(":",3)

hora_atual = tempo_atual[0]
min_atual = tempo_atual[1]
# seg_atual = tempo_atual[2]

# tempo_atual_txt = str(hora_atual+":"+min_atual);

# #Minutos convertidos para segundo + soma dos segundos
# hora_para_seg = (16 - int(hora_atual)) * 3600
# min_para_seg = (55 - int(min_atual)) * 60

# seg_em_sleep = hora_para_seg + min_para_seg

# while(tempo_atual_txt != "15:05"):
#         #Make "While" wait 1 sec till run again
#         time.sleep(1)

#         print(tempo_atual_txt+" ainda não é hora")
#         tempo_atual = time.ctime()
#         tempo_atual = tempo_atual.split()
#         tempo_atual = tempo_atual[3].split(":",3)

#         hora_atual = tempo_atual[0]
#         min_atual = tempo_atual[1]
        
#         tempo_atual_txt = str(hora_atual+":"+min_atual);

#         if(tempo_atual_txt == "15:05"):
#             print("Deu a hora")
           

# print(str(hora_atual+":"+min_atual))

hora_para_seg = (int(hora_saida.split(":",1)[0]) - int(hora_atual)) * 3600
min_para_seg = (int(hora_saida.split(":",1)[1]) - int(min_atual)) * 60

seg_em_sleep = hora_para_seg + min_para_seg
time.sleep(seg_em_sleep)
print(seg_em_sleep)