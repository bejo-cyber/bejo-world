import tkinter
root = tkinter.Tk()
def event_tekan():
    label2 = tkinter.Label(root,text= 'selamat anda mendapatkan uang 20 juta rupiah')
    label2.pack()
label = tkinter.Label(root,text= 'silahkan di klik:')
tombol = tkinter.Button(root,text= 'klik', command = event_tekan)

label.pack()
tombol.pack()

#root.mainloop()