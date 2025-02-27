import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import ttk  # Importa o módulo ttk para widgets mais avançados

# Criação da janela principal
janela = tk.Tk()
janela.title("Cotação de Moedas")  # Define o título da janela

# Função para buscar a cotação de uma moeda específica
def buscar_cotacao():
    moeda_preenchida = moeda.get()  # Obtém a moeda selecionada
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)  # Busca a cotação no dicionário

    # Cria um rótulo para exibir a mensagem de cotação
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)

    # Se a moeda estiver no dicionário, exibe a cotação
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'

# Função para buscar múltiplas cotações ao mesmo tempo
def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)  # Obtém o texto da caixa de entrada
    lista_moedas = texto.split("\n")  # Separa os itens por linha
    mensagem_cotacoes = []

    # Percorre a lista de moedas e busca suas cotações
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}: {cotacao}')

    # Exibe as cotações encontradas
    mensagem4 = tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)

# Configurações da grade da janela para melhor organização dos elementos
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

# Rótulo de título
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='white', bg='#FFC0CB', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# Rótulo de instrução
mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

#moeda = tk.Entry()
#moeda.grid(row=1, column=1)

# Botão para buscar a cotação da moeda selecionada
botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

# Dicionário com as cotações das moedas disponíveis
dicionario_cotacoes = {
    'Dólar': 5.47,
    'Euro': 6.68,
    'Bitcoin': 20000
}

# Criação de uma Combobox (menu suspenso) para seleção de moeda
moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)

# Rótulo com instrução para buscar múltiplas cotações
mensagem3 = tk.Label(text="Caso você queira pegar mais de 1 cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem3.grid(row=4, column=0, columnspan=2)

# Caixa de texto para entrada de múltiplas moedas
caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5, column=0, sticky='nswe')

# Botão para buscar múltiplas cotações
botao_multiplascotacoes = tk.Button(text="Buscar Cotações", command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5, column=1)

# Inicia o loop principal da interface gráfica
janela.mainloop()
