import tkinter as tk

class SemaforoConjuncionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla de Verdad y Semáforo")
        self.root.geometry("500x700")
        
        #Tabla de Verdad (A, B y C)
        self.tabla = [
            {"A": 0, "B": 0, "C": 0, "Resultado": 0},
            {"A": 0, "B": 0, "C": 1, "Resultado": 0},
            {"A": 0, "B": 1, "C": 0, "Resultado": 0},
            {"A": 0, "B": 1, "C": 1, "Resultado": 0},
            {"A": 1, "B": 0, "C": 0, "Resultado": 0},
            {"A": 1, "B": 0, "C": 1, "Resultado": 1},
            {"A": 1, "B": 1, "C": 0, "Resultado": 1},
            {"A": 1, "B": 1, "C": 1, "Resultado": 1},
        ]
        self.index = 0
        self.running = False

        self.start_button = tk.Button(root, text="Iniciar", font=("Arial", 14), command=self.start_logic)
        self.start_button.pack(pady=10)

        #canvas semáforo
        self.canvas = tk.Canvas(root, width=100, height=300, bg="black")
        self.canvas.pack(pady=10)

        self.red_light = self.canvas.create_oval(20, 20, 80, 80, fill="gray")
        self.yellow_light = self.canvas.create_oval(20, 110, 80, 170, fill="gray")
        self.green_light = self.canvas.create_oval(20, 200, 80, 260, fill="gray")

        #puertas lógicas
        self.and_canvas = tk.Canvas(root, width=300, height=250, bg="white")
        self.and_canvas.pack(pady=10)
        self.and_canvas.pack_forget()  
        
        #mostrar valores de (A, B y C)
        self.label_a = tk.Label(root, text="A: 0", font=("Arial", 16))
        self.label_a.pack(pady=5)

        self.label_b = tk.Label(root, text="B: 0", font=("Arial", 16))
        self.label_b.pack(pady=5)

        self.label_c = tk.Label(root, text="C: 0", font=("Arial", 16))
        self.label_c.pack(pady=5)

        self.label_resultado = tk.Label(root, text="f: 0", font=("Arial", 16))
        self.label_resultado.pack(pady=10)

        self.label_counter = tk.Label(root, text="Contador: 0", font=("Arial", 16))
        self.label_counter.pack(pady=10)

    def start_logic(self):
        if not self.running:
            self.running = True
            self.update_logic()

    def update_logic(self):
        if self.index < len(self.tabla):
            fila = self.tabla[self.index]

            self.label_a.config(text=f"A: {fila['A']}")
            self.label_b.config(text=f"B: {fila['B']}")
            self.label_c.config(text=f"C: {fila['C']}")
            self.label_resultado.config(text=f"f: {fila['Resultado']}")

            self.and_canvas.delete("all")
            self.start_counter(fila["Resultado"], fila["A"], fila["B"], fila["C"])
        else:
            self.running = False
            self.index = 0

    def start_counter(self, resultado, a, b, c):
        self.counter = 0
        self.update_counter(resultado, a, b, c)

    def update_counter(self, resultado, a, b, c):
        if self.counter < 2:
            self.label_counter.config(text=f"Contador: {self.counter}")
            self.counter += 1
            self.root.after(1000, self.update_counter, resultado, a, b, c)
        else:
            self.change_light(resultado, a, b, c)
            self.index += 1
            self.root.after(2000, self.update_logic)

    def change_light(self, resultado, a, b, c):
        # Apagar todas las luces primero
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="gray")

        # Si el resultado es 1, encender la luz verde y mostrar la gráfica
        if resultado == 1:
            self.canvas.itemconfig(self.green_light, fill="green")
            self.and_canvas.pack()  # Mostrar el canvas de la compuerta cuando la luz sea verde
        else:
            # Si no, encender la luz roja y ocultar la gráfica
            self.canvas.itemconfig(self.red_light, fill="red")
            self.and_canvas.pack_forget()  # Ocultar el canvas de la compuerta

        self.draw_logic_gates(a, b, c, resultado)

    def draw_logic_gates(self, a, b, c, resultado):
        # Entrada A, B y C
        self.and_canvas.create_line(40, 50, 100, 50, width=3, fill="black")  # A
        self.and_canvas.create_text(20, 50, text=f"A={a}", font=("Arial", 10), fill="black")

        self.and_canvas.create_line(40, 90, 100, 90, width=3, fill="black")  # B
        self.and_canvas.create_text(20, 90, text=f"B={b}", font=("Arial", 10), fill="black")

        self.and_canvas.create_line(40, 130, 100, 130, width=3, fill="black")  # C
        self.and_canvas.create_text(20, 130, text=f"C={c}", font=("Arial", 10), fill="black")

        # Compuerta AND para A, B, C (curvada)
        self.and_canvas.create_line(100, 50, 180, 50, width=3, fill="black")  # A
        self.and_canvas.create_line(100, 90, 180, 90, width=3, fill="black")  # B
        self.and_canvas.create_line(100, 130, 180, 130, width=3, fill="black")  # C
        
        # Dibujo de la compuerta AND curvada de 3 entradas
        self.and_canvas.create_arc(150, 40, 200, 160, start=270, extent=180, outline="black", width=3)

        # Línea de salida (resultado)
        self.and_canvas.create_line(200, 100, 240, 100, width=3, fill="black")  # Salida de AND
        self.and_canvas.create_text(260, 100, text=f"f={resultado}", font=("Arial", 10), fill="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforoConjuncionApp(root)
    root.mainloop()
