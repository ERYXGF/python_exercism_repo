def label(colors):
    #First define the list of all the colours
    pallette = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    #Im then finding the index of the 3 inputted colours
    value1 = pallette.index(colors[0])
    value2 = pallette.index(colors[1])
    value3 = pallette.index(colors[2])
    #Creation of the base number
    base = int(str(value1) + str(value2))
    #Adding the zeros by using the powers of 10
    whole = base*(10**value3)
    #Determining if its kilo, mega or normal ohms
    if whole >= 1000000000:
        result = whole//1000000000
        return (f"{result} gigaohms")
    elif whole >= 1000000:
        result = whole//1000000
        return (f"{result} megaohms")
    elif whole >=1000:
        result = whole//1000
        return (f"{result} kiloohms")
    else:
        return (f"{whole} ohms")
 
    

        
