def alphabet_position(letter):
    alphabet1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alphabet1:
        letterIndex = alphabet1.index(letter)

        return letterIndex
    elif letter in alphabet2:
        letterIndex = alphabet2.index(letter)

        return letterIndex

def rotate_character(char, rot):

    alphabet1 = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#return non alphabet characters
    if char not in alphabet1 and char not in alphabet2:
        newChar = char
    else:
        index = int(alphabet_position(char)) + int(rot)

#check for lowercase andd rotate
        if char in alphabet1:
            if index < 26:
                newChar = alphabet1[index]
            else:
                index = index % 26
                newChar = alphabet1[index]
    #check uppercase and rotate
        if char in alphabet2:
            if index < 26:
                newChar = alphabet2[index]
            else:
                index = index % 26
                newChar = alphabet2[index]
    return newChar
