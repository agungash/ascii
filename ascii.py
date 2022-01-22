import ascii_magic
try :
    x = input("Masukkan path gambar : ")
    my_art = ascii_magic.from_image_file(x)
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print("Error!", e)