import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica

# Cria a janela principal
janela = tk.Tk()

# Variável que armazena o estado do checkbox de promoções (1 = marcado, 0 = desmarcado)
var_promocoes = tk.IntVar()

# Cria um checkbox para perguntar se o usuário deseja receber e-mails promocionais
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocionais?", variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)  # Posiciona o checkbox na janela

# Variável que armazena o estado do checkbox de aceitação de políticas
var_politicas = tk.IntVar()

# Cria um checkbox para perguntar se o usuário aceita os Termos de Uso e Políticas de Privacidade
checkbox_politicas = tk.Checkbutton(text="Aceitar Termos de Uso e Políticas de Privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1, column=0)  # Posiciona o checkbox na janela

# Função chamada ao clicar no botão "Enviar"
def enviar():
    # Verifica se o usuário deseja receber promoções e imprime a resposta no console
    if var_promocoes.get():
        print('Usuário deseja receber promoções')
    else:
        print('Usuário NÃO deseja receber promoções')

    # Verifica se o usuário aceitou os Termos de Uso e imprime a resposta no console
    if var_politicas.get():
        print('Usuário concordou com Termos de Uso e Políticas de Privacidade')
    else:
        print('Usuário NÃO concordou')

# Cria um botão que chama a função "enviar" quando pressionado
botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=2, column=0)  # Posiciona o botão na janela

# Mantém a janela aberta em um loop até que o usuário a feche
janela.mainloop()
