def list_input():
    """
    Function for getting input and cnvert as list
    input:
        string having spaces
    output:
        list of the words,split based on spaces
    """
    return list(map(str, input("\nEnter the words :  ")
                .strip().split()))[:list_limit]


def len_calculator(input_list, limit):
    """
    Parameters
    ----------
    input_list : list
        contains list of words.

    Returns
    -------
    lar_word : string
        varibale to store calcualted string.

    """
    lar_word = ''
    for i in input_list:
        if len(i) <= limit:
            if len(i) > len(lar_word):
                lar_word = i
    return lar_word

try:
    print("Enter the list length:")
    list_limit = int(input())
    print("Enter word length checker:")
    len_limit = int(input())
    print("Please Enter word list::")
    word_list = list_input()
    print("Input words are:", word_list, "\n")
    print("The largest Word having lenth less than or equal to {} is {}".format(len_limit, len_calculator(word_list, len_limit))
            )
except ValueError:
    print("Plese Enter Numeric input")
    