from sql import Produto
import customtkinter as ctk
from tkinter import messagebox as box
from PIL import Image 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

imagem_estoque = Image.open('estoque.png')
imagem_estoques = ctk.CTkImage(light_image=imagem_estoque, dark_image=imagem_estoque, size=(100, 100))


class Menu:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.geometry('600x600')
        self.janela.title('Estoque')

        self.menu_principal = ctk.CTkLabel(self.janela, text='Bem-vindo ao sistema de estoque')
        self.imagens = ctk.CTkLabel(self.janela, text='', image=imagem_estoques)

        self.bo_inserir = ctk.CTkButton(
            self.janela,
            text='Inserir',
            font=("Arial", 18),
            command=self.abrir_tela_cadastro
        )
        self.bo_ver_todos = ctk.CTkButton(self.janela,text='Ver todos',font=('Arial',18),command=self.abrir_tela_ver_todos)
        self.menu_principal.grid(row=0, column=0, columnspan=2, pady=10)
        self.imagens.grid(row=1, column=0, rowspan=5, padx=10, pady=10)
        self.bo_inserir.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.bo_ver_todos.grid(row=2, column=1, sticky="ew", padx=10, pady=5)


        self.janela.mainloop()

    def abrir_tela_cadastro(self):
        self.janela.withdraw()  
        TelaCadastroProduto(self.janela) 
    def abrir_tela_ver_todos(self):
        self.janela.withdraw()  
        VerTodosProdutos(self.janela)  
class VerTodosProdutos:
    def __init__(self, master_menu):
        self.master_menu = master_menu
        self.master_menu.withdraw()  # Esconde a janela principal

        self.janela = ctk.CTkToplevel()
        self.janela.title("Todos os Produtos")
        self.janela.geometry("600x400")
        self.janela.protocol("WM_DELETE_WINDOW", self.voltar_ao_menu)

        self.titulo = ctk.CTkLabel(self.janela, text="Lista de Produtos", font=("Arial", 18))
        self.titulo.pack(pady=10)

        self.texto = ctk.CTkTextbox(self.janela, width=580, height=300)
        self.texto.pack(padx=10, pady=10)
        self.texto.configure(state="normal")

        self.preencher_texto()

        self.botao_voltar = ctk.CTkButton(self.janela, text="Voltar", command=self.voltar_ao_menu)
        self.botao_voltar.pack(pady=10)

    def preencher_texto(self):
        produtos = Produto.ver_todos()
        if not produtos:
            self.texto.insert("end", "Nenhum produto encontrado.")
        else:
            for (id, nome_produto, descricao, categoria, quantidade, data_saida) in produtos:
                self.texto.insert("end", f"{'-'*30}\n")
                self.texto.insert("end", f"ID: {id}\nNome: {nome_produto}\nDescrição: {descricao}\n")
                self.texto.insert("end", f"Categoria: {categoria}\nQuantidade: {quantidade}\nData de saída: {data_saida}\n")
        self.texto.configure(state="disabled")  # Impede edição

    def voltar_ao_menu(self):
        self.janela.destroy()
        self.master_menu.deiconify()

    
 


class TelaCadastroProduto:
    def __init__(self, master):
        self.master_menu = master  
        self.janela = ctk.CTkToplevel()  
        self.janela.title("Cadastro de Produto")

        self.label_titulo = ctk.CTkLabel(self.janela, text="Cadastrar Novo Produto", font=("Arial", 18))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.imagens = ctk.CTkLabel(self.janela, text='', image=imagem_estoques)
        self.imagens.grid(row=1, column=0, rowspan=5, padx=10, pady=10)

        self.entry_nome = self._criar_entrada("Nome do Produto:", 1)
        self.entry_descricao = self._criar_entrada("Descrição:", 2)
        self.entry_categoria = self._criar_entrada("Categoria:", 3)
        self.entry_data = self._criar_entrada("Data de Saída:", 4)
        self.entry_quantidade = self._criar_entrada("Quantidade:", 5)

        self.botao_inserir = ctk.CTkButton(self.janela, text="Inserir Produto", command=self.inserir_produto)
        self.botao_inserir.grid(row=6, column=0, columnspan=2, pady=10)

        self.botao_voltar = ctk.CTkButton(self.janela, text="Voltar ao Menu", command=self.voltar_ao_menu)
        self.botao_voltar.grid(row=7, column=0, columnspan=2, pady=10)

    def _criar_entrada(self, texto, linha):
        label = ctk.CTkLabel(self.janela, text=texto)
        label.grid(row=linha, column=0, padx=10, pady=5, sticky="e")
        entrada = ctk.CTkEntry(self.janela)
        entrada.grid(row=linha, column=1, padx=10, pady=5, sticky="w")
        return entrada

    def inserir_produto(self):
        try:
            nome = self.entry_nome.get()
            descricao = self.entry_descricao.get()
            categoria = self.entry_categoria.get()
            data_final = self.entry_data.get()
            quantidade = int(self.entry_quantidade.get())

            produto = Produto(nome, descricao, categoria, quantidade, data_final)
            Produto.inserir_produto_novo(produto)

            box.showinfo("Sucesso", "Produto inserido com sucesso!")
        except ValueError:
            box.showerror("Erro", "Quantidade deve ser um número inteiro.")

    def voltar_ao_menu(self):
        self.janela.destroy()           
        self.master_menu.deiconify()   



if __name__ == '__main__':
    Menu()
