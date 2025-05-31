import customtkinter as tk
from tkinter import messagebox as box
from PIL import Image 

janela = tk.CTk()
janela.title('Partida Competitiva')
janela.geometry('1920x1080')
#imagem 

imagem_btcs = Image.open('images.png')
imagem_btc = (tk.CTkImage(light_image= imagem_btcs, dark_image= imagem_btcs, size=(500,500)))
imagem = Image.open('jett.jpg')
imagem_ctk = (tk.CTkImage(light_image= imagem, dark_image= imagem, size=(500,500)))


# Título
titulo = tk.CTkLabel(janela, text='ESCOLHA', text_color='white')
titulo.grid(row=0, column=0)

# Mapa
nome_mapa = tk.CTkLabel(janela, text='Mapa', bg_color='blue')
nome_mapa.grid(row=1, column=0)

# Nome exibido após digitar nick
nome = tk.CTkLabel(janela, text='', text_color='white')
nome.grid(row=3, column=0)

# Nick input
nick = tk.CTkEntry(janela, placeholder_text='Coloque seu Nick')
nick.grid(row=2, column=0)

def pronto():
    escolha = nick.get()
    nome.configure(text=f'{escolha}')
    nick.destroy()
    botao_nome.destroy()

botao_nome = tk.CTkButton(janela, text='Confirmar', command=pronto)
botao_nome.grid(row=2, column=1)

# Chat
def enviar():
    msg = chat.get()
    chating.configure(text=f'{msg}')

chating = tk.CTkLabel(janela, text='', font=('Arial', 12, 'bold'), text_color='white', bg_color='black')
chating.grid(row=4, column=0)

chat = tk.CTkEntry(janela, placeholder_text='Escreve para o time')
chat.grid(row=5, column=0, pady=(20, 10))

botao_chat = tk.CTkButton(janela, text='Enviar', command=enviar)
botao_chat.grid(row=5, column=1)

# Escolha de personagem
def escolha_personagem():
    box.showinfo('Aviso', 'Você escolheu a Jett')
    jet = tk.CTkLabel(janela, text='',image= imagem_ctk)
    jet.grid(row=6, column=0)

botao_escolha = tk.CTkButton(janela, image=imagem_btc, command=escolha_personagem)
botao_escolha.grid(row=6, column=1)



janela.mainloop()
