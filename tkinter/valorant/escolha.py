import customtkinter as tk
janela = tk.CTk()
janela.title('partida competitiva')
janela.geometry('1920x1080')
titulo = tk.CTkLabel(janela, text='ESCOLHA ',text_color='white')
titulo.pack()

#mapa
nome_mapa = tk.CTkLabel(janela, text='mapa ', bg_color='blue')
nome_mapa.pack()

nome = tk.CTkLabel(janela, text='', text_color='white')
nome.pack(pady=(10, 500))

#nick
nick = tk.CTkEntry(janela,placeholder_text='coloque seu Nick')
nick.pack(pady=(150, 10))
def pronto():
    escolha = nick.get()
    nome.configure(text = f'{escolha}')
    nick.destroy()
    botao_nome.destroy()


botao_nome = tk.CTkButton(janela,text='confirma', command= pronto)
botao_nome.pack()



#chat
def enviar():
    msg = chat.get()
    chating.configure(text = f'{msg}')
    
chating = tk.CTkLabel(janela,text='',font=('arial',12,'bold'), text_color= 'white', bg_color= 'black')
chating.pack()
chat = tk.CTkEntry(janela,placeholder_text='escreve para o time')
chat.pack(pady=(20, 10))
botão_chat = tk.CTkButton(janela, text='enviar',command=enviar)
botão_chat.pack()

    
    


#personagem
def escolha_personagem():
    jet = tk.CTkLabel(janela,text='JETT')
    jet.pack()

#botão
botão_escolha = tk.CTkButton(janela ,text='escolha', command= escolha_personagem)
botão_escolha.pack()

janela.mainloop()
