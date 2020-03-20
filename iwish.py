from tkinter import*
import tkinter.messagebox


def command():
    enter_txt = e1.get()
    txt.delete(0.0, END)
    try:
        definition = the_dictionary[enter_txt]
    except:
        definition = "Sorry i think it is not about Programming."
    txt.insert(END, definition)

root = Tk()
root.title("Programming Dictionary")
root.geometry("500x300+120+120")
root.config(bg = "black")

def message():
    tkinter.messagebox.showinfo("About Dictionary", "This dictionary is for programming purposes only")

bttn1 = Button(root, text="?", font="algerian", command=message)
bttn1.place(x=0, y=0)

label1 = Label(root, text="WEBSTER", font="algerian 24", bg="black", fg="white")
label1.pack()
label2 = Label(root, text="PROGRAMMING", font="algerian 22", bg="black", fg="white")
label2.pack()

label3 = Label(root, text="What do you need to know?(just type here):", font="arial 10", bg="black", fg="white")
label3.pack()
e1 = Entry(root, font="Arial 12", width=20, justify=CENTER)
e1.pack()

bttn2 = Button(root, text="Search", font="algerian", padx=5, pady=3, command=command)
bttn2.pack()

label4 = Label(root, text="Definition:", font="arial 10", bg="black", fg="white")
label4.pack()

txt = Text(root, font="arial 12 italic ", width=20, height=20, wrap=WORD, bg="white")
txt.pack(fill=BOTH)

the_dictionary = {"software": "is a collection of data or computer instructions that tell the computer how to work.",
                  "hardware": "Refers to the physical elements of a computer. This is also sometime called the machinery of a computer.",
                  "programming": "is defined as the process of creating computer software using a programming language.",
                  "data": "is a information processed or stored by a computer. this information may be in the form of text, documents, images, audio clips, software programs, or other types of data.",
                  "file": "is an object on a computer that stores data, information, settings or commands used with a computer program. ",
                  "memory": "is any physical device capable of storing information temporarily, like RAM or permanently like ROM. Memory devices utilize integrated circuits and are used by operating system, software, and hardware ",
                  "RAM": "Random Access Memory is a hardware device that allows information to be stored and retrieved on a computer. it is also alternatively referred to as main memory, primary memory or system memory.",
                  "ROM": "Read Only Memory is a storage medium that is used with computers and other electronic devices. As the name indicates, data stored in ROM may only be read.",
                  "operating system": "is a software program that enables the computer hardware to communicates and operate with the computer software.",
                  "BIOS": "Basic Input/Output System, is a ROM chip found on motherboards that allows you to access and setup your computer system at the most basic level.",
                  "debug": "Refers to the process of examining and removing errors from a program's source code.",
                  "command line": "Also called the Windows command line, command screen, or text interface, is a user interface that is navigated by typing commands at prompts, instead of using the mouse.",
                  "prompt": "Is a text or symbols used to represent the system's readiness to perform the next command. A prompt may also  be a text representation of where the user is currently. ",
                  }

root.mainloop()
