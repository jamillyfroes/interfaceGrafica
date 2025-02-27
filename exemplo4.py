import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica

# Função para abrir uma nova janela
def abrir_janela():
    janela2 = tk.Toplevel()  # Cria uma nova janela secundária
    janela2.title('Janela Nova')  # Define o título da nova janela
    
    # Botão dentro da nova janela para fechá-la
    botao_fechar = tk.Button(janela2, text="Fechar", command=janela2.destroy)
    botao_fechar.grid(row=1, column=0)  # Posiciona o botão na grade da janela

# Cria a janela principal
janela = tk.Tk()

# Botão na janela principal para abrir a nova janela
botao = tk.Button(janela, text='Ir para outra janela', command=abrir_janela)
botao.grid(row=2, column=3)  # Posiciona o botão na interface

# Mantém a janela aberta até que o usuário a feche
janela.mainloop()


