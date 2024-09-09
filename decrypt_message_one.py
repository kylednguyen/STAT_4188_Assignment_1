cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

decipher_dict = {v: k for k, v in cipher.items()}


encrypted_file = open("encrypted_message_one.txt", 'r')


encrypted_message = encrypted_file.readline()


encrypted_file.close()


decipher = ""
for char in encrypted_message:
   if char in decipher_dict:
       decipher += decipher_dict[char]
   else:
       decipher += char
print(decipher)
