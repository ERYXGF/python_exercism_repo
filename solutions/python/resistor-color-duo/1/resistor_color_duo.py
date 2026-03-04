def value(colors):
    
    pallette = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    
    
    value1 = pallette.index(colors[0])
    value2 = pallette.index(colors[1])

    return int(str(value1) + str(value2))
    

