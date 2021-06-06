data = 'ini adalah string'
print(data,'\n',type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
    
'''

data = 'menggunaan single quote'
print(data)

data = "menggunaan double quote"
print(data)

print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("mari shalat jum'at")

# 2. menggunakan tanda \
    
    #membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it')
    #membuat tanda \ menjadi string (backlash)
print('C:\\User\\Ucup')

    #tab
print('ucup\totong, jadi jauhan')
print('ucup\t\t\totong, semakin jauhan')

    #backspace
print('ucup \botong, jadi deketan')

    #newline
print('baris pertama. \nbaris kedua.') # LF -> line feed -> unix, macos, linux
print('baris pertama. \rbaris kedua.') # CR -> carriage return -> commodore, acorn,lisp
print('baris pertama. \r\nbaris kedua.') # CRLF -> carriage return line feed -> dipakai oleh windows

# 3. string literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya 
print('C:\\new folder')

# menggunakan raw string
print(r'C:\new folder')
print(r'C:\new \b\r\\\ folder')

# multiline literal string
print('''
      nama : bagas
      asal : panggul
      kelas: 3c
      ''')

# multiline literal string dan raw
print(r'''
      nama   : bagas
      asal   : panggul
      kelas  : 3c
      website: www.bagas.com\newID
      ''')








