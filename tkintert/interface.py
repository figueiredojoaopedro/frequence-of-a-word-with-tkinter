from tkinter import *
from tkinter import scrolledtext


# this function will take the search word in the other script and analyse all the file to see the occurrencies
def checking():
    txtOutput.delete("1.0",END)
    outputWord.delete("0", END)
    word = ' ' + inputWord.get() + ' '
    lista = []
    chat = open('chat.txt', 'r')
    for lines in chat.readlines():
        if word.lower() in lines.lower():
            lista.append(lines)
        else:
            pass
    aux = 0 # i will use this variable just to count how many occurrencies there are in the text
    for i in range(len(lista)):
        aux += 1
        txtOutput.insert(END,lista[i])
    # it will show up how many times we got the words
    outputWord.insert(END,aux)


#creating the window
window = Tk()
window.title('Filtro de palavras')

# suspect word / input / search button / frequence
# suspect word label
susWord = Label(window, text = 'Palavra Suspeita:', font=('Arial Bold', 14))
susWord.place(relx = 0.1,rely=0.05,anchor=CENTER)

# input for suspect word
inputWord = Entry(window, width=20, font=('Arial', 14))
inputWord.place(relx=0.4, rely=0.05, anchor=CENTER)

#search button
searchButton = Button(window, text='Pesquisar!', command=checking)
searchButton.place(relx=0.6, rely=0.05, anchor=CENTER)

#frequence text
freqWord = Label(window, text = 'Frequência:', font=('Arial Bold', 14))
freqWord.place(relx = 0.1,rely=0.1,anchor=CENTER)

# output for frequence of the word
outputWord = Entry(window, width=20, font=('Arial', 14))
outputWord.place(relx=0.4, rely=0.10, anchor=CENTER)

# occurrencies text
occurrence = Label(window, text='Ocorrências:', font=('Arial Bold',14))
occurrence.place(relx=0.1,rely=0.2,anchor=CENTER)

#scrolled area 
txtOutput = scrolledtext.ScrolledText(window, width=100,height=20)
txtOutput.place(relx=0.05,rely=0.4,anchor=W)
#size of the window
window.state('zoomed') #iconic would show the app only in the taskbar
window.iconbitmap('images/notebook.png')
window.minsize(width=800,height=800)
# window.resizable(false,false) will disallow the resize of the window
#main loop to keep the window opened
window.mainloop()