# SIZE: Tamanho de cada tipo de objecto que compõe o mundo
SIZE = {
    "OBJECT": 25,
    "WALL"  : 15
}

# OBJETOS: Identifica segundo os nomes dados pelo robô
OBJ = {
    "ADULT"    : "adulto",
    "CHILD"    : "criança",
    "EMPLOYEE" : "funcionário",
    "CART"     : "carrinho",
    "ZONE"     : "zona",
    "CASHIER"  : "caixa"
}

# CATEGORIAS: Agrupa os varios objetos para identificação nos algoritmos correspondentes
CATEGORY = {
    "OBJECT": [OBJ["CART"], OBJ["CASHIER"]],                   # Objetos
    "PEOPLE": [OBJ["EMPLOYEE"], OBJ["ADULT"], OBJ["CHILD"]],   # Pessoas
    "LOCALS": [OBJ["ZONE"]]                                    # Locais
}

SPLITTER = "_"
