import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Dados de login válidos
email_valido = "a"
senha_valida = "a"

# Função executada ao clicar no botão de login
def clique():
    email_inserido = campo_email.get()
    senha_inserida = campo_senha.get()

    if email_inserido != email_valido:
        mensagem.configure(text="E-mail inválido.", text_color="red")
    elif senha_inserida != senha_valida:
        mensagem.configure(text="Senha inválida.", text_color="red")
    else:
        mensagem.configure(text="Login realizado com sucesso!", text_color="green")
        janela.destroy()  # Fecha a tela de login
        abrir_tela()  # Chama a função para abrir a nova janela

# Função que abre uma nova tela após login bem-sucedido
def abrir_tela():
    nova_janela = ctk.CTk()  # Nova janela
    nova_janela.geometry("500x400")
    nova_janela.title("Gatinhos!")
    
    # Caminhos das imagens
    caminho_imagem = r"imagens/cat1.jpeg"
    caminho_imagem1 = r"imagens/cat2.jpeg"
    caminho_imagem2 = r"imagens/cat3.jpeg"
    caminho_imagem3 = r"imagens/cat4.jpeg"
    
    # Abrir e redimensionar as imagens usando PIL
    imagem = Image.open(caminho_imagem).resize((200, 200))
    imagem1 = Image.open(caminho_imagem1).resize((200, 200))
    imagem2 = Image.open(caminho_imagem2).resize((200, 200))
    imagem3 = Image.open(caminho_imagem3).resize((200, 200))
    
    # Converter as imagens para o formato usado no Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem)
    imagem_tk1 = ImageTk.PhotoImage(imagem1)
    imagem_tk2 = ImageTk.PhotoImage(imagem2)
    imagem_tk3 = ImageTk.PhotoImage(imagem3)
    
    # Labels para exibir as imagens em uma grade
    label_imagem = ctk.CTkLabel(nova_janela, image=imagem_tk, text="")
    label_imagem.image = imagem_tk
    label_imagem.grid(row=0, column=0, padx=10, pady=10)

    label_imagem1 = ctk.CTkLabel(nova_janela, image=imagem_tk1, text="")
    label_imagem1.image = imagem_tk1
    label_imagem1.grid(row=0, column=1, padx=10, pady=10)

    label_imagem2 = ctk.CTkLabel(nova_janela, image=imagem_tk2, text="")
    label_imagem2.image = imagem_tk2
    label_imagem2.grid(row=1, column=0, padx=10, pady=10)

    label_imagem3 = ctk.CTkLabel(nova_janela, image=imagem_tk3, text="")
    label_imagem3.image = imagem_tk3
    label_imagem3.grid(row=1, column=1, padx=10, pady=10)
    
    nova_janela.mainloop()  # Mantém a nova janela aberta

# Configurações do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Tema padrão (ou use um tema customizado)

# Criando a janela principal
janela = ctk.CTk()
janela.geometry("500x300")
janela.title("Site de Gatinhos")

# Componentes da interface
texto = ctk.CTkLabel(janela, text="Fazer Login")
campo_email = ctk.CTkEntry(janela, placeholder_text="E-mail")
campo_senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")

# Botão de login com cores personalizadas
botao = ctk.CTkButton(
    janela, 
    text="Login", 
    command=clique, 
    fg_color="#ff69b4",  # Rosa claro
    hover_color="#a13068"  # Rosa mais escuro ao passar o mouse
)

mensagem = ctk.CTkLabel(janela, text="")

# Posicionamento dos componentes na janela
texto.pack(padx=10, pady=10)
campo_email.pack(padx=10, pady=10)
campo_senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
mensagem.pack(padx=10, pady=10)

# Loop da interface gráfica
janela.mainloop()
