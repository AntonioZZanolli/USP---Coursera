segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
dias_resto = total_segs % 86400
horas = dias_resto // 3600
horas_resto = dias_resto % 3600
minutos = horas_resto // 60
segundos_final = horas_resto % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segundos_final, " segundos.")
