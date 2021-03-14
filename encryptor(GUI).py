import tkinter as tk



root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

h1 = root.title('Encryptor')


label1 = tk.Label(root, text='Basic Image Encryption using XOR operation')
label1.config(font=('Georgia', 14))
canvas1.create_window(200, 25, window=label1)


label2 = tk.Label(root, text='Enter the path of the image: ')
label2.config(font=('Georgia', 10))
canvas1.create_window(200, 75, window=label2)

label3 = tk.Label(root, text='Enter the Encryption key: ')
label3.config(font=('Georgia', 10))
canvas1.create_window(200, 150, window=label3)


entry1 = tk.Entry(root)
canvas1.create_window(200, 100, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(200, 180, window=entry2)



def encrypt():
    try:

        path = entry1.get()

        key = int(entry2.get())

        ex = 0

        print('The path of file : ', path)
        print('Key for encryption : ', key)

        fin = open(path, 'rb')

        image = fin.read()
        fin.close()

        image = bytearray(image)

        for index, values in enumerate(image):
            image[index] = values ^ key

        fin = open(path, 'wb')

        fin.write(image)
        fin.close()
        print('Encryption Done...')

    except Exception:
        print('Error caught : Please enter a proper file path and an integer key. ')
        ex+=1

    if ex == 0:
        label3 = tk.Label(root, text='Your image has been encrypted.')
        label3.config(font=('Calibri', 14))
        canvas1.create_window(200, 220, window=label3)
    else:
        label4 = tk.Label(root, text='Please enter the correct file path and key.')
        label4.config(font=('Calibri', 14))
        canvas1.create_window(200, 220, window=label4)











button1 = tk.Button(text='Quit', command=root.quit, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(240, 280, window=button1)

button2 = tk.Button(text='OK', command=encrypt, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(150, 280, window=button2)




root.mainloop()