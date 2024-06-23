#tkinter cira interface
c
import tkinter as tk

class Tela:
    def __init__(self):
       
        self.tela = tk.Tk()
        self.tela.title("Calculadora teste1")
        self.tela.resizable(width=False, height=False)
        
        # Atributos da classe
        self.Res = ""
        self.Valores = 0
        self.Width = 8
        self.Height = 2
        self.Fonte = "Arial 14 bold"
        
        def atualizar(auxBt):  # Atualiza o display
            self.Res += auxBt
            print(self.Res)
            self.auxResultado.set(self.Res)
        
        def calcular():  # Calcula o resultado
            Digitos = []
            Oper = []
            Num = []

            for i in self.Res:
                if i.isdigit():
                    Digitos.append(i)
                else:
                    Oper.append(i)
                    Digitos.append("*")

            print(Digitos)

            NumStr = "".join(Digitos)
            NumStr = NumStr.split("*")

            for j in NumStr:
                Num.append(j)

            print(NumStr)
            print(Num)


   # operadORES] 
            if Oper:
                operador = Oper[0]
                if operador == '+':
                    ResTotal = int(Num[0]) + int(Num[1])
                elif operador == '-':
                    ResTotal = int(Num[0]) - int(Num[1])
                elif operador == '*':
                    ResTotal = int(Num[0]) * int(Num[1])
                elif operador == '/':
                    if int(Num[1]) != 0:
                        ResTotal = int(Num[0]) / int(Num[1])
                    else:
                        ResTotal = "Erro: Divisão por zero"
                else:
                    ResTotal = "Erro: Operador inválido"

                self.auxResultado.set(str(ResTotal))
            else:
                self.auxResultado.set("Erro: Nenhum operador encontrado")
        
        # Mostrar o resultado
        self.auxResultado = tk.StringVar()
        self.auxResultado.set("---")
        self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font=self.Fonte)
        self.lbResultado.grid(row=0, columnspan=3)

        # Botões
        self.auxBt0 = tk.StringVar()
        self.auxBt0.set(0)
        self.Bt0 = tk.Button(self.tela, textvariable=self.auxBt0, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt0.get()))
        self.Bt0.grid(row=1, column=0, padx=2, pady=2)
          
        # Botão 1         
        self.auxBt1 = tk.StringVar()
        self.auxBt1.set(1)
        self.Bt1 = tk.Button(self.tela, textvariable=self.auxBt1, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt1.get()))
        self.Bt1.grid(row=1, column=1, padx=2, pady=2)
        
        # Botão 2
        self.auxBt2 = tk.StringVar()
        self.auxBt2.set(2)
        self.Bt2 = tk.Button(self.tela, textvariable=self.auxBt2, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt2.get()))
        self.Bt2.grid(row=1, column=2, padx=2, pady=2)
        
        # Botão 3
        self.auxBt3 = tk.StringVar()
        self.auxBt3.set(3)
        self.Bt3 = tk.Button(self.tela, textvariable=self.auxBt3, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt3.get()))
        self.Bt3.grid(row=2, column=0, padx=2, pady=2)
        
        # Botão 4
        self.auxBt4 = tk.StringVar()
        self.auxBt4.set(4)
        self.Bt4 = tk.Button(self.tela, textvariable=self.auxBt4, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt4.get()))
        self.Bt4.grid(row=2, column=1, padx=2, pady=2)
        
        # Botão 5
        self.auxBt5 = tk.StringVar()
        self.auxBt5.set(5)
        self.Bt5 = tk.Button(self.tela, textvariable=self.auxBt5, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt5.get()))
        self.Bt5.grid(row=2, column=2, padx=2, pady=2)
        
        # Botão 6
        self.auxBt6 = tk.StringVar()
        self.auxBt6.set(6)
        self.Bt6 = tk.Button(self.tela, textvariable=self.auxBt6, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt6.get()))
        self.Bt6.grid(row=3, column=0, padx=2, pady=2)
        
        # Botão 7
        self.auxBt7 = tk.StringVar()
        self.auxBt7.set(7)
        self.Bt7 = tk.Button(self.tela, textvariable=self.auxBt7, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt7.get()))
        self.Bt7.grid(row=3, column=1, padx=2, pady=2)
        
        # Botão 8
        self.auxBt8 = tk.StringVar()
        self.auxBt8.set(8)
        self.Bt8 = tk.Button(self.tela, textvariable=self.auxBt8, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt8.get()))
        self.Bt8.grid(row=3, column=2, padx=2, pady=2)
        
        # Botão 9
        self.auxBt9 = tk.StringVar()
        self.auxBt9.set(9)
        self.Bt9 = tk.Button(self.tela, textvariable=self.auxBt9, width=self.Width, height=self.Height, font=self.Fonte, command=lambda: atualizar(self.auxBt9.get()))
        self.Bt9.grid(row=4, column=0, padx=2, pady=2)
        
        # Botão -
        self.auxBt10 = tk.StringVar()
        self.auxBt10.set("-")
        self.Bt10 = tk.Button(self.tela, textvariable=self.auxBt10, width=self.Width, height=self.Height, bg="LIGHT BLUE", font=self.Fonte, command=lambda: atualizar(self.auxBt10.get()))
        self.Bt10.grid(row=4, column=1, padx=2, pady=2)
        
        # Botão +
        self.auxBt11 = tk.StringVar()
        self.auxBt11.set("+")
        self.Bt11 = tk.Button(self.tela, textvariable=self.auxBt11, width=self.Width, height=self.Height, bg="LIGHT BLUE", font=self.Fonte, command=lambda: atualizar(self.auxBt11.get()))
        self.Bt11.grid(row=4, column=2, padx=2, pady=2)
        
        # Botão *
        self.auxBt12 = tk.StringVar()
        self.auxBt12.set("*")
        self.Bt12 = tk.Button(self.tela, textvariable=self.auxBt12, width=self.Width, height=self.Height, bg="LIGHT BLUE", font=self.Fonte, command=lambda: atualizar(self.auxBt12.get()))
        self.Bt12.grid(row=5, column=0, padx=2, pady=2)
        
        # Botão /
        self.auxBt13 = tk.StringVar()
        self.auxBt13.set("/")
        self.Bt13 = tk.Button(self.tela, textvariable=self.auxBt13, width=self.Width, height=self.Height, bg="LIGHT BLUE", font=self.Fonte, command=lambda: atualizar(self.auxBt13.get()))
        self.Bt13.grid(row=5, column=1, padx=2, pady=2)
        
        # Botão =
        self.auxBt14 = tk.StringVar()
        self.auxBt14.set("=")
        self.Bt14 = tk.Button(self.tela, textvariable=self.auxBt14, width=self.Width, height=self.Height, bg="LIGHT BLUE", font=self.Fonte, command=calcular)
        self.Bt14.grid(row=5, column=2, padx=2, pady=2)
        
        
        
        
        self.tela.mainloop()

Tela()