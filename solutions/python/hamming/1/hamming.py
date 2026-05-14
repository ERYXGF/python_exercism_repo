def distance(strand_a, strand_b):
    #Checks if the strands are of the same length
    length1 = len(strand_a)
    length2 = len(strand_b)
    if length1 != length2:
        raise ValueError("Strands must be of equal length.")
    #Iterates through the strands:
    count = 0
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            count +=1
    return count
                
