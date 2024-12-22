#### Imports et définition des variables globales
"""kkk"""


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
        for liste in lines:
            liste = liste.strip()
            if liste:
                l.append([int(x) for x in liste.split(';')])


    return l

def get_list_k(data, k):
    """kkk"""

    return data[k] if 0 <= k < len(data) else None

def get_first(l):
    """lll"""


    return l[0]

def get_last(l):
    """kkk"""

    return l[-1]

def get_max(l):
    """dd"""
    max_value=l[0]
    for nombre in l :
        max_value = max(max_value, nombre)

def get_min(l):
    """jjj"""
    min_value=l[0]
    for nombre in l:
        min_value = min(min_value, nombre)

def get_sum(l):
    """,,,"""
    s=0
    for nombre in l:
        s+=nombre
    return s


#### Fonction principale


def main():
    """lll"""

    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
