def classify(number):
    #Raise an exception:
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    #Determining the aliquot sum
    aliquot = 0
    for nums in range(1,number):
        if number%nums==0:
            aliquot+=nums
    #Determining if the number is perfect:
    if number == aliquot:
        return "perfect"
    #Determining if the number is abundant:
    elif number < aliquot:
        return "abundant"
    #Determining if the number is deficient:
    elif number > aliquot:
        return "deficient"