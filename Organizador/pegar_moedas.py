import xmltodict

def nomes_moedas():
    with open('moedas.xml', 'rb') as arquivo_moedas: # O arquivo 'moedas.xml' é aberto em modo de leitura binária ('rb') e atribuído à variável 'arquivo_moedas'.
        dic_moedas = xmltodict.parse(arquivo_moedas) # O conteúdo do arquivo XML é lido e convertido em um dicionário Python usando a função 'parse' da biblioteca 'xmltodict', e o resultado é armazenado na variável 'dic_moedas'.

    moedas = dic_moedas['xml'] # Acessa a chave 'xml' do dicionário 'dic_moedas' para obter a lista de moedas, e essa lista é atribuída à variável 'moedas'.
    return moedas # Retorna a lista de moedas.

def nomes_conversoes():
    with open('conversoes.xml', 'rb') as arquivo_conversoes: # O arquivo 'conversoes.xml' é aberto em modo de leitura binária ('rb') e atribuído à variável 'arquivo_conversoes'.
        dic_conversoes = xmltodict.parse(arquivo_conversoes) # O conteúdo do arquivo XML é lido e convertido em um dicionário Python usando a função 'parse' da biblioteca 'xmltodict', e o resultado é armazenado na variável 'dic_conversoes'.
 
    conversoes = dic_conversoes['xml'] # Acessa a chave 'xml' do dicionário 'dic_conversoes' para obter a lista de conversões, e essa lista é atribuída à variável 'conversoes'.
    dic_conversoes_disponiveis = {} # Inicializa um dicionário vazio chamado 'dic_conversoes_disponiveis' para armazenar as conversões disponíveis.
    for par_conversao in conversoes: # O loop for itera sobre cada item na lista 'conversoes', e a variável 'par_conversao' representa cada item individualmente.
        moeda_origem, moeda_destino = par_conversao.split('-')
        if moeda_origem in dic_conversoes_disponiveis:
            dic_conversoes_disponiveis[moeda_origem].append(moeda_destino) # Se a moeda de origem já estiver presente no dicionário 'dic_conversoes_disponiveis', a moeda de destino é adicionada à lista associada a essa chave.
        else:
            dic_conversoes_disponiveis[moeda_origem] = [moeda_destino] # Se a moeda de origem não estiver presente no dicionário, uma nova chave é criada com a moeda de origem e uma lista contendo a moeda de destino como valor.

    return dic_conversoes_disponiveis # Retorna o dicionário de conversões disponíveis.