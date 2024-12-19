#exercicio numero 06

def dic4ListaDics(d):
    
    lstdics = []

    lstchaves = list(d.keys())
    lstvalors = list(d.values())

    tam = len(lstvalors[0])

    for i in range(tam):
        d = {}
        d [lstchaves[0]] = lstvalors[0][i]
        d [lstchaves[1]] = lstvalors[1][i]
        lstdics.append(d)

    ['ciência', 'Linguagem']
    [[88, 89, 62, 95], [77, 78, 84, 80]]

    return lstdics


#teste