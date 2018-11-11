






def num2String(number, num_char=6):
    str_number = str(number)
    while(len(str_number) < num_char):
        str_number = "0" + str_number
    return str_number