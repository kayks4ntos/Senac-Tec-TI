import tkinter as tk
class interface_iniciar:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("__________bem vindo a interface grafica_______________")
        self.janela.geometry("1920x1080")
        self.clique()
        self.check()
        self.entradas()
        self.verificar()
        self.botaoes()
        self.textos()
        self.janela.mainloop() 
              
    def clique(self):
        label = tk.Label(self.janela, text= 'clicou' )
        label.pack()
    def check(self):
        self.var = tk.IntVar()
        check = tk.Checkbutton(self.janela, text= 'legal ', variable= self.var)
        check.pack()

    def entradas(self):
        entrada = tk.Entry(self.janela)
        entrada.pack()

    def verificar(self):    
        if self.var.get() == 1:
            label = tk.Label(self.janela, text= 'sim e maior' )
            label.pack()
            botao2 = tk.Button(self.janela, text= 'verificar', command= self.clique, background='blue')
            botao2.pack()
        else:
            label = tk.Label(self.janela, text= 'nao e maior' )
            label.pack()
    def botaoes(self):
        self.botao = tk.Button(self.janela, text= 'verificar', command= self.verificar, background='red')
        self.botao.pack()
    def textos(self):
        self.texto = tk.Text(self.janela, height=50, width= 5 )
        self.texto.pack()
        

app = interface_iniciar()
            








