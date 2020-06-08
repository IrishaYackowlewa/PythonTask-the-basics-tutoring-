s = 'Луна, меняющая яркость от пепельной до ослепительной, дала жизнь легенде о возрождающейся птице Феникс'

def word_from_letters_string(word, string):
    arr_letters = list(word)
    
    arr_lett_from_str = []
    for i in range(len(arr_letters)):
        m = string.find(arr_letters[i])
        if m != -1:
            arr_lett_from_str.append(string[m])
        else:
            arr_lett_from_str.append('*')

    return ("").join(arr_lett_from_str)

arr_word = []

arr_word.append(word_from_letters_string('Феникс', s))
arr_word.append(word_from_letters_string('означает', s))
arr_word.append(word_from_letters_string('постоянство', s))

need_string = (" ").join(arr_word)

print(need_string)