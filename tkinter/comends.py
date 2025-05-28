import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


janela = ctk.CTk()
janela.title("__________bem vindo a interface grafica_______________")
janela.geometry("1920x1080")


label = ctk.CTkLabel(janela, text='clicou')
label.pack(pady=5)


var = ctk.IntVar()
check = ctk.CTkCheckBox(janela, text='legal', variable=var)
check.pack(pady=5)


entrada = ctk.CTkEntry(janela)
entrada.pack(pady=5)


texto = ctk.CTkTextbox(janela, height=100, width=300)
texto.pack(pady=5)


def verificar():
    if var.get() == 1:
        resultado = ctk.CTkLabel(janela, text='sim, é maior')
    else:
        resultado = ctk.CTkLabel(janela, text='não é maior')
    resultado.pack(pady=5)

botao = ctk.CTkButton(janela, text='Verificar', command=verificar, fg_color='red')
botao.pack(pady=5)


janela.mainloop()








