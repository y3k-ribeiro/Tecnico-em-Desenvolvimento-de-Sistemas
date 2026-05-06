posicao_inicial = float(input("Posição Incial: "))
posicao_final = float(input("Posição Final: "))
tempo_inicial = float(input("Tempo Inicial: "))
tempo_final = float(input("Tempo Final: "))

velocidade_media = (posicao_final-posicao_inicial)/(tempo_final-tempo_inicial)
print("Velocidade média ", velocidade_media)