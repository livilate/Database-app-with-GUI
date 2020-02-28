from tkinter import *
import sqlite3

root = Tk()
root.title('Boisson app')
root.geometry('400x700')

#DEF

#funcion Guardar, para poder guardar en nuestra ventana de editar
def guardar():
    # conexion a la database
    Conexion = sqlite3.connect('precios.cvs')
    # busca cosas en nuestra base de datos
    cursor = Conexion.cursor()

    valor_oid = n_delete.get()

    cursor.execute("""UPDATE bebida SET
        
        Nombre = :nombre, 
        Precio = :precio,
        lugar = :lugar,
        tipo = :tipo
        
        WHERE oid = :oid""",
        {'nombre': n_bebida_editor.get(),
         'precio': n_tipo_editor.get(),
         'lugar': n_lugar_editor.get(),
         'tipo': n_precio_editor.get(),

         'oid': valor_oid}
      )

    # guardar los cambios en nuestra database
    Conexion.commit()
    # cerrar conexion
    Conexion.close()
    editor.destroy()

#Funcion para editar un valor en la base de datos
def editar():

    root.withdraw()
    global editor
    editor = Tk()
    editor.title('Editar un valor')
    editor.geometry("400x150")

    # conexion a la database
    Conexion = sqlite3.connect('precios.cvs')
    # busca cosas en nuestra base de datos
    cursor = Conexion.cursor()

    valor_id = n_delete.get()

    # query la base de datos
    cursor.execute("SELECT * FROM bebida WHERE oid = " + valor_id)
    valores = cursor.fetchall()


    #Valores globales para usar en la def guardar

    global n_bebida_editor
    global n_precio_editor
    global n_lugar_editor
    global n_tipo_editor


    #BOTON

    editar_editor = Button(editor, text='Guardar cambios', bd=1, command=guardar)
    editar_editor.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 3), ipadx=140)


    # ENTRY

    n_bebida_editor = Entry(editor, width=30, bd=3)
    n_bebida_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    n_precio_editor = Entry(editor, width=30, bd=3)
    n_precio_editor.grid(row=1, column=1, padx=20)

    n_lugar_editor = Entry(editor, width=30, bd=3)
    n_lugar_editor.grid(row=2, column=1, padx=20)

    n_tipo_editor = Entry(editor, width=30, bd=3)
    n_tipo_editor.grid(row=3, column=1, padx=20)

    # LABELS

    n_bebida_label = Label(editor, text="Marca")
    n_bebida_label.grid(row=0, column=0, pady=(10, 0))

    n_precio_label = Label(editor, text="Precio")
    n_precio_label.grid(row=1, column=0)

    n_lugar_label = Label(editor, text="Distribuidor")
    n_lugar_label.grid(row=2, column=0)

    n_tipo_label = Label(editor, text="Tipo de alcohol ej: vodka, whisky")
    n_tipo_label.grid(row=3, column=0)

    #loop resultado
    for valor in valores:
        n_bebida_editor.insert(0, valor[0])
        n_precio_editor.insert(0, valor[1])
        n_lugar_editor.insert(0, valor[2])
        n_tipo_editor.insert(0, valor[3])


    # guardar los cambios en nuestra database
    Conexion.commit()

    # cerrar conexion
    Conexion.close()

#funcion para eliminar valores de la base de datos1
def eliminar():
    # conexion a la database
    Conexion = sqlite3.connect('precios.cvs')
    # busca cosas en nuestra base de datos
    cursor = Conexion.cursor()

    #eliminar

    cursor.execute("DELETE from bebida WHERE oid=" + n_delete.get())

    # guardar los cambios en nuestra database
    Conexion.commit()

    # cerrar conexion
    Conexion.close()

#funcion para agregar a nuesta base de datos
def submit():
    # conexion a la database
    Conexion = sqlite3.connect('precios.cvs')
    # busca cosas en nuestra base de datos
    cursor = Conexion.cursor()

    # crear table
    #cursor.execute("""CREATE TABLE bebida (Nombre text, tipo text, lugar text, Precio integer)""")


    #agregar lo que hicimos a la table
    cursor.execute("INSERT INTO bebida VALUES (:n_bebida, :n_precio, :n_lugar, :n_tipo)",
                   {
                       'n_bebida': n_bebida.get(),
                       'n_precio': n_precio.get(),
                       'n_lugar': n_lugar.get(),
                       'n_tipo': n_tipo.get()
                   })

    # guardar los cambios en nuestra database
    Conexion.commit()

    # cerrar conexion
    Conexion.close()

    #borrar los cajas de texto
    n_tipo.delete(0, END)
    n_lugar.delete(0, END)
    n_precio.delete(0, END)
    n_bebida.delete(0, END)

#funcion para ver la base de datos, querry
def ver():
    # conexion a la database
    Conexion = sqlite3.connect('precios.cvs')
    # busca cosas en nuestra base de datos
    cursor = Conexion.cursor()

    #query la base de datos
    cursor.execute("SELECT *,oid FROM bebida")
    valores = cursor.fetchall()

    print_valor = ""
    for valor in valores:
        print_valor += str(valor[4]) + "  -  " + str(valor[0]) + "    $" + str(valor[1]) + "   En   " + str(valor[3]) + "\n"

    ver_label = Label(root, text=print_valor)
    ver_label.grid(row=9, column=0, columnspan=2)

    # guardar los cambios en nuestra database
    Conexion.commit()
    # cerrar conexion
    Conexion.close()


#BOTONES

button_agregar = Button(root, text= 'Agregar a la base de datos', bd=1, command=submit)
button_agregar.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 3), ipadx=100)

ver_button = Button(root, text='Mostrar Base de datos', bd=1, command=ver)
ver_button.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 5), ipadx=111)

editar_button = Button(root, text='Editar ID', bd=1, command=editar)
editar_button.grid(row=7, column=0, columnspan=2, padx=10, pady=(10, 3), ipadx=145)

borrar_button = Button(root, text='Eliminar ID', bd=1, command=eliminar)
borrar_button.grid(row=8, column=0, columnspan=2, padx=10, pady=(0, 5), ipadx=139)


#ENTRY

n_bebida = Entry(root, width=30, bd=3)
n_bebida.grid(row=0, column=1, padx=20, pady=(10, 0))

n_precio = Entry(root, width=30, bd=3)
n_precio.grid(row=1, column=1, padx=20)

n_lugar = Entry(root, width=30, bd=3)
n_lugar.grid(row=2, column=1, padx=20)

n_tipo = Entry(root, width=30, bd=3)
n_tipo.grid(row=3, column=1, padx=20)

n_delete = Entry(root, width=30, bd=3)
n_delete.grid(row=6, column=1, padx=20)


#LABELS

n_bebida_label = Label(root, text="Marca")
n_bebida_label.grid(row=0, column=0, pady=(10, 0))

n_precio_label = Label(root, text="Precio")
n_precio_label.grid(row=1, column=0)

n_lugar_label = Label(root, text="Distribuidor")
n_lugar_label.grid(row=2, column=0)

n_tipo_label = Label(root, text="Tipo de alcohol ej: vodka, whisky")
n_tipo_label.grid(row=3, column=0)

n_delete_label = Label(root, text="Seleccionar ID")
n_delete_label.grid(row=6, column=0, pady=(10, 0))

#MAIN LOOP

root.mainloop()