import json

with open("dados.json") as jr_json:
    dados = json.load(jr_json)

    for i in dados:
        print(i[dia])