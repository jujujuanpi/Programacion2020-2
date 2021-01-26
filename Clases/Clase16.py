diccionario = {}
diccionario ["Nombres"] = ["Laura", "Karla", "Santi", "Juan Pablo", "Melany", "Mario", "Valeria"]
diccionario ["Edades"] = ["18, 18, 19, 21, 20, 19, 17"]

print (diccionario)
print (diccionario.keys())
print (diccionario.values())

alimentos = {}
alimentos ["Carnes"] = {"Cerdo": ["Costilla", "Chuleta", "Pierna"],
                        "Res": ["Cola", "Solomo", "Punta de Anca"],
                        "Pollo": ["Pechuga", "Muslo", "Ala"]}
alimentos ["Lacteos"] = ["Queso", "Leche", "Yogurt"]

print (alimentos)
print (alimentos.keys())

print (alimentos ["Carnes"])
print (alimentos ["Carnes"].keys())
print (alimentos ["Carnes"]["Cerdo"])
print (alimentos ["Carnes"]["Cerdo"] [1])

## COPY

alimentos2 = alimentos.copy()
alimentos3 = alimentos

print (alimentos2 ["Carnes"])

## FROM KEYS

keys = ["Nombres", "Edades", "Semestres"]

estudiantesCES = dict.fromkeys(keys)
print (estudiantesCES)

## GET ()

alimentos.get("Carnes")
alimentos.get ("Carnes").get("Cerdo")
print (alimentos)