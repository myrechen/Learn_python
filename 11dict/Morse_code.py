#dict的使用:莫尔斯码
codes = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
         'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
         'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
         'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
         'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..',
         '0':'-----', '1':'.----', '2':'..---', '3':'...--',
         '4':'....-', '5':'.....', '6':'-....', '7':'--...',
         '8':'---..', '9':'----.',
         '.':'.-.-.-', ':':'---...', ',':'--..--', ';':'-.-.-.',
         '?':'..--..', '=':'-...-', '\'':'.----.', '/':'-..-.',
         '!':'-.-.--', '-':'-....-', '_':'..--.-', '"':'.-..-.',
         '(':'-.--.', ')':'-.--.-', '$':'...-..-', '&':'....',
         '@':'.--.-.', '+':'.-.-.',}

words = input('请输入一句英文:')
for s in words:
    m_code = codes.get(s.upper(),s)
    print(m_code,end="")