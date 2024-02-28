def ler_dados(arquivo):
    with open(arquivo, "r") as file:
        linhas = file.readlines()
    return [linha.strip().split(',') for linha in linhas[1:]]

def lista_modalidades_ordenadas(data):
    modalidades = sorted(set(dado[8] for dado in data))  # dado[8] é a modalidade
    with open("resultados.txt", "a") as output_file:
        output_file.write("Lista de modalidades desportivas em ordem alfabética:\n")
        for modalidade in modalidades:
            output_file.write(modalidade + "\n")
        output_file.write("\n___________________________________\n")

def calcular_percentagens_aptos_inaptos(data):
    total_atletas = len(data)
    aptos = sum(dado[12] == 'true' for dado in data)
    inaptos = total_atletas - aptos
    perc_aptos = (aptos/total_atletas) * 100
    perc_inaptos = (inaptos/total_atletas) * 100
    with open("resultados.txt", "a") as output_file:
        output_file.write("Percentagens de atletas aptos e não aptos para a prática desportiva:\n")
        output_file.write(f"Percentagem de atletas aptos: {perc_aptos:.2f}%\n")
        output_file.write(f"Percentagem de atletas inaptos: {perc_inaptos:.2f}%\n")
        output_file.write("\n___________________________________\n")

def distribuicao_atletas_por_faixa_etaria(data):
    distribuicao_idades = {}
    for dado in data:
        idade = int(dado[5])
        intervalo = f"[{idade // 5 * 5}-{idade // 5 * 5 + 4}]"
        distribuicao_idades[intervalo] = distribuicao_idades.get(intervalo, 0) + 1
    with open("resultados.txt", "a") as output_file:
        output_file.write("Distribuição de atletas por faixa etária:\n")
        for intervalo, quantidade in sorted(distribuicao_idades.items()):
            output_file.write(f"{intervalo}: {quantidade}\n")
        output_file.write("\n___________________________________\n")

# Execução das funções
dados = ler_dados("emd.csv")
lista_modalidades_ordenadas(dados)
calcular_percentagens_aptos_inaptos(dados)
distribuicao_atletas_por_faixa_etaria(dados)
