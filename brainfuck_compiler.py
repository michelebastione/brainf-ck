import numpy, time

check=''

print("Brainfuck Compiler\nby Michele Bastione\n")


def find_bracket_match (string):
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        if string[i] == ']':
            if count == 0:
                return i
            count -=1


def main(one_print = True):
        
    try:
        code = open('%s'%input("\nInsert name (and extension) of the file to compile: ")).read()
        length_c = len(code)
        print()
    except:
        print("\nLoadingError: the file was not found")
        return None

    if code.count('[')!= code.count(']'):
        print("SyntaxError: unmatched bracket found")
        return None    

    stream, data_pointer, instruction_pointer = numpy.zeros(10**5, dtype = int), 0, 0
    length_s = len(stream) 
    brackets, loop = 0, []

    text=''

    while instruction_pointer < length_c :
        if code[instruction_pointer] == '>' :
            data_pointer += 1
            if data_pointer > length_s :
                stream = numpy.append(stream, np.zeros(10000))

        elif code[instruction_pointer] == '<' :
            data_pointer -= 1
            if data_pointer < 0 :
                print("IndexError: the array does not account for negative indexes")
                return None

        elif code[instruction_pointer] == '+' :
            try:
                stream[data_pointer] += 1
            except:
                print('ValueError: the cells of the array cannot store this data')
                return None
            
        elif code[instruction_pointer] == '-' :
            try:
                stream[data_pointer] -= 1
            except:
                print("ValueError: the cells of the array cannot store this data")
                return None

        elif code[instruction_pointer] == '[' :
            start = instruction_pointer + 1
            end = start + find_bracket_match(code[start:]) + 1
            if stream[data_pointer] == 0 :
                instruction_pointer = end - 1
            else:
                loop.append(start)            
                brackets += 1
                instruction_pointer = start - 1
        
        elif code[instruction_pointer] == ']' :
            if stream[data_pointer] == 0 :
                del loop[-1]
                brackets -= 1
            else:
                instruction_pointer = loop[brackets - 1] - 1

        elif code[instruction_pointer] == ',':
            try:
                stream[data_pointer] = int(input("Input value required: "))
                if stream[data_pointer] > 255 :
                    raise ValueError
            except:
                print("ValueError: the input must be an integer less than 256")
                return None

        elif code[instruction_pointer] == '.' :
            char = chr(stream[data_pointer])
            if one_print:
                text += char
            else:
                print(char, end = '')
        instruction_pointer += 1
       
    if one_print:
        print(text)

if __name__ == "__main__":
    while check.lower()!='n':
        main(False)
        time.sleep(.8)
        check=input("\nDo you wish to continue?(Y/N) ")
        time.sleep(.3)
    print('\n\nGoodbye!')
    time.sleep(1.2)
