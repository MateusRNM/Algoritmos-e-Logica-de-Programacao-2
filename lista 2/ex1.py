def processar_sensores(sensores):
    max_temperatura = 0
    min_umidade = sensores[0][2]
    alertas = []
    for sensor in sensores:
        max_temperatura = max(max_temperatura, sensor[1])
        min_umidade = min(min_umidade, sensor[2])
        if sensor[1] > 35 or sensor[2] < 20:
            alertas.append(sensor[0])
    return (alertas, (max_temperatura, min_umidade))

def main():
    sensores = [(0, 30, 25), (1, 36, 25), (2, 30, 11), (3, 56, 2)]
    res = processar_sensores(sensores)
    print("IDs dos sensores em alerta:")
    for id in res[0]:
        print(id)
    print(f"Temperatura máxima registrada: {res[1][0]}")
    print(f"Umidade mínima registrada: {res[1][1]}")

main()