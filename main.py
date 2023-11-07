from tkinter import Tk, Button, Entry
import tkinter as tk
num1 = ""
num2 = ""
op = ""
nums = "0123456789"
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("345x335")

def num(evento):
    global num1
    global num2
    global op
    pantalla.delete(0, "end")
    k = evento.widget.cget("text")
    if k in nums and op == "":
        num1 += k
        pantalla.insert(0,num1)
    elif k == "." and "." in num1 and op == "":
        pantalla.insert(0,num1)
    elif k == "." and "." not in num1 and op == "":
        num1+=k
        pantalla.insert(0,num1)
    elif (k == ".") and ("." in num2) and (op != ""):
        pantalla.insert(0,num2)
    elif (k == ".") and ("." not in num2) and (op != ""):
        num2+=k
        pantalla.insert(0,num2)
    elif k in nums and op != "":
        num2 += k
        pantalla.insert(0,num2)
    elif k not in nums and op == "" and num1 != "":
        op = k
        pantalla.insert(0,op)
    elif k == "=" and (num1 != "" and num2 != ""):
        pantalla.insert(0, eval(num1 + op + num2))
        num1, num2, op = "", "", ""

    else: 
        pantalla.insert(0, "Error")
        num1, num2, op = "", "", ""



# Configuración pantalla de salida 
pantalla = Entry(root, width=20, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1, sticky="ew")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1, sticky="ew")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1, sticky="ew")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1, sticky="ew")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1, sticky="ew")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1, sticky="ew")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1, sticky="ew")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1, sticky="ew")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1, sticky="ew")
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="ew")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1, sticky="ew")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1, sticky="ew")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1, sticky="ew")
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1, sticky="ew")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1, sticky="ew")



boton_1.bind("<Button-1>", num)
boton_2.bind("<Button-1>", num)
boton_3.bind("<Button-1>", num)
boton_4.bind("<Button-1>", num)
boton_5.bind("<Button-1>", num)
boton_6.bind("<Button-1>", num)
boton_7.bind("<Button-1>", num)
boton_8.bind("<Button-1>", num)
boton_9.bind("<Button-1>", num)
boton_igual.bind("<Button-1>", num)
boton_punto.bind("<Button-1>", num)
boton_mas.bind("<Button-1>", num)
boton_menos.bind("<Button-1>", num)
boton_multiplicacion.bind("<Button-1>", num)
boton_division.bind("<Button-1>", num)




root.mainloop()