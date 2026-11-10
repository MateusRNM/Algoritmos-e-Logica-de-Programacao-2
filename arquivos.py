import json

file = open("arquivo.txt", "w+")
file.write(json.dumps({
    "nome": "Mateus",
    "idade": 19
}))
file.close()