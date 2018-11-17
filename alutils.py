import os






def num2String(number, num_char=6):
    str_number = str(number)
    while(len(str_number) < num_char):
        str_number = "0" + str_number
    return str_number

def gen_dir(new_dir):
	if not os.path.exists(new_dir):
		os.mkdir(new_dir)
	return (new_dir + '/')