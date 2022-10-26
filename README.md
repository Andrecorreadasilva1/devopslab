# DevOps Hands On
Removendo Bug da aplicação 

#REMOVER AS LINHAS

@app.route('/bug')                                                                                                                               
def bad():                                                                                                                                       
    try:                                                                                                                                         
        raise TypeError()                                                                                                                        
    except TypeError as e:                                                                                                                       
        print(e)                                                                                                                                 
    except TypeError as e:                                                                                                                       
        print("Duplicado, ou seja, nunca vai entrar aqui.")