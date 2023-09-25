# Christopher Arias and Alex Ha
# I pledge my honor that I have abided by the Stevens Honor System

def stringtobinary(str1):
    allwords = str1.split()
    first = allwords[0]
    return first

def binarytohex(str2):
    return str2

def regaddress(reg):
    try: 
        if reg == 'X0':
            return '00'
        elif reg == 'X1':
            return '01'
        elif reg == 'X2':
            return '10'
        elif reg == 'X3':
            return '11'
        else:
            raise ValueError
    except ValueError:
        print('Invalid Register')
        

formatarray = ['00: ', '10: ', '20: ', '30: ', '40: ', '50: ', '60: ', '70: ', '80: ', '90: ', 'a0: ', 'b0: ', 'c0: ', 'd0: ', 'e0: ', 'f0: ']

with open('assembly.txt') as assfile:
    counter = 0
    formatcounter = 0
    instructions = open("image.txt", 'x')
    instructions.write('v3.0 hex words addressed\n')
    for line in assfile:
        if counter == 0:
            instructions.write(formatarray[formatcounter])
            formatcounter += 1
        inst = line[0:3]
        imm = line[12]
        if inst == 'ADD':
            opcode = ''
            if imm == 'X':
                opcode += '0'
            else:
                opcode += '1' 
            opcode = '0' + opcode
            opcode = '1' + opcode
            opcode = regaddress(line[8:10]) + opcode
            if imm == 'X':
                opcode = regaddress(line[12:14]) + opcode
                opcode = regaddress(line[4:6]) + opcode
                opcode = '0000000' + opcode
            else:
                opcode = '00' + opcode
                opcode = regaddress(line[4:6]) + opcode
                splitList = line.split(' ')
                immediate = splitList[-1]
                immediate = (bin(int(immediate)))[2:]
                opcode = immediate + opcode
                opcode = '0' + opcode 
        elif inst == 'SUB':
            opcode = ''
            if imm == 'X':
                opcode += '0'
            else:
                opcode += '1' 
            opcode = '0' + opcode
            opcode = '0' + opcode
            opcode = regaddress(line[8:10]) + opcode
            if imm == 'X':
                opcode = regaddress(line[12:14]) + opcode
                opcode = regaddress(line[4:6]) + opcode
                opcode = '0000000' + opcode
            else:
                opcode = '00' + opcode
                opcode = regaddress(line[4:6]) + opcode
                splitList = line.split(' ')
                immediate = splitList[-1]
                immediate = (bin(int(immediate)))[2:]
                opcode = immediate + opcode
                opcode = '0' + opcode 
        elif inst == 'LDR':
            opcode = ''
            opcode += '111'
            opcode = regaddress(line[9:11]) + opcode
            opcode = '00' + opcode
            opcode = regaddress(line[4:6]) + opcode
            splitList = line.split(' ')
            immediate = splitList[-1]
            immediate = immediate[:-2]
            immediate = (bin(int(immediate)))[2:]
            opcode = immediate + opcode
            opcode = '0' + opcode
        else:
            raise Exception("Incorrect registers")
        
        opcode = int(opcode, 2)
        opcode = (hex(opcode))[2:]
        instructions.write(opcode)
        counter += 1
        if counter == 15:
            instructions.write('\n')
            counter = 0
        else:
            instructions.write(' ')

print(instructions)



assfile.close()
