def eliminaNones(d):
    
    lst = []
    for k in d.keys(): # Cadastro as chaves de dic
        if d[k] == None: # Que possuem None como valor
            lst.append(k)

    for k in lst: # Elimino as chaves de dic que possuem
        del d[k]  # None como valor
    
    return d   
# fim eliminaNones