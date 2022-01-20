
data = "ini adalah string"
print(data,type(data))

# 1. cara membuat string 

"""  
    1. dengan menggunakan single quate '...'
    2. dengan menggunakan double quate "..."
"""

data = 'menggunakan single quate'
print(data)

data = "menggunakan double quate"
print(data)

print("'hello world ?'")
print('"hello world ?"')
print("ini adalah hari jum'at")

# menggunakan tanda (\)

# membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, ins\'t it ?')

# backlash
print("C:\\user\\yoga")

# tab 
print("aku\tdia,jauhan")
print("aku\t\t\tdia,semakain jauhan")

# backspace
print("aku \bdia,jadi dekatan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix,macos,linux
print("baris pertama.\rbaris kedua.") # CR -> carrige return -> commandore,acorn,lisp
print("baris pertama.\r\nnbaris kedua.") # CRLF -> line feed carrige return -> windows

# 3. string literal atau raw

# hati hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string 
print(""" 
Nama : Yoga
Kelas : Kuliah
 """)

# multiline literal string dan raw
print(r""" 
Nama : Yoga
Kelas : Kuliah \new normal
Website : www.yoga.com/newID 
""")

