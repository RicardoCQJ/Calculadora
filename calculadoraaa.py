import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Calculadora Elegante")
        self.ventana.geometry("350x500")
        self.ventana.configure(bg="#1e1e2f")  # Fondo oscuro
        self.expresion = ""

        # Estilo general
        self.color_fondo = "#1e1e2f"
        self.color_boton = "#3a3a5c"
        self.color_texto = "#ffffff"
        self.color_resultado = "#0affd4"
        self.fuente = ("Consolas", 20)

        # Pantalla de entrada
        self.entrada = tk.Entry(self.ventana, font=self.fuente, bg="#26263a", fg=self.color_resultado,
                                bd=10, insertwidth=2, width=18, borderwidth=5, justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

        # Botones de la calculadora
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        columna = 0
        for boton in botones:
            self.crear_boton(boton, fila, columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

        # Botón de limpiar
        tk.Button(self.ventana, text='C', width=32, height=2, bg="#e06c75", fg="white",
                  font=("Consolas", 14, "bold"), command=self.limpiar).grid(row=fila, column=0, columnspan=4, pady=10)

    def crear_boton(self, valor, fila, columna):
        tk.Button(self.ventana, text=valor, width=5, height=2, bg=self.color_boton, fg=self.color_texto,
                  font=self.fuente, command=lambda: self.click(valor)).grid(row=fila, column=columna, padx=5, pady=5)

    def click(self, valor):
        if valor == "=":
            try:
                resultado = str(eval(self.expresion))
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, resultado)
                self.expresion = resultado
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "Error")
                self.expresion = ""
        else:
            self.expresion += str(valor)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, self.expresion)

    def limpiar(self):
        self.expresion = ""
        self.entrada.delete(0, tk.END)

# Ejecutar la calculadora
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
