from tkinter import *
import random
import string
#import pyperclip


def generate():
    small_alphabet=string.ascii_lowercase
    capital_alphabet=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabet+capital_alphabet+numbers+special_characters
    
    password_length=int(lengthbox.get())


    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabet,password_length))
    
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabet+capital_alphabet,password_length))
    
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
    
    #password=random.sample(all,passlen)
    #passwordField.insert(0,password)

root = Tk()
root.geometry("400x400")  

choice = IntVar()

Label(root, text="Password Generator Application", font="calibri 20 bold").grid(pady=10)

lengthbox=Spinbox(root,from_=5,to_=18,width=5,font='arial')
lengthbox.grid(pady=5)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font='arial')
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font='arial')
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font='arial')
strongradioButton.grid(pady=5)

generateButton=Button(root, text="Generate Password", command=generate) 
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2)
passwordField.grid()



#copyButton=Button(root,text='Copy',font='arial',command=copy)
#copyButton.grid(pady=5)

root.mainloop()
