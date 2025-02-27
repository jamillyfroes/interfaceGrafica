import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica

# Cria a janela principal
janela = tk.Tk()

# Variável que armazenará a opção selecionada pelo usuário nos botões de rádio
var_aviao = tk.StringVar()

# Cria os botões de rádio para seleção da classe do avião
botao_classeeconomica = tk.Radiobutton(text="Classe Econômica", variable=var_aviao, value="Classe Econômica")
botao_classexecutiva = tk.Radiobutton(text="Classe Executiva", variable=var_aviao, value="Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="Primeira Classe", variable=var_aviao, value="Primeira Classe")

# Posiciona os botões de rádio na interface
botao_classeeconomica.grid(row=0, column=0)
botao_classexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)

# Função chamada ao clicar no botão "Enviar"
def enviar():
    print(var_aviao.get())  # Exibe a opção selecionada no console

# Cria um botão para enviar a seleção
botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)  # Posiciona o botão na interface

# Mantém a janela aberta até que o usuário a feche
tk.mainloop()
