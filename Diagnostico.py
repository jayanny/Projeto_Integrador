"""
Dados das doenças coletados em:
    https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1

"""

# sets / conjuntos de sintomas

covid_19 = {'Tosse', 'Febre', 'Coriza', 'Dor de garganta', 'Dificuldade para respirar', 'Perda de olfato (anosmia)',
            'Alteração do paladar (ageusia)', 'Náuseas', 'Vômitos', 'Diarreia', 'Cansaço (astenia)',
            'Diminuição do apetite (hiporexia)', 'Dispneia (falta de ar)'}

asma = {'Tosse', 'Chiado no peito', 'Dificuldade para respirar', 'Respiração rápida e curta', 'Desconforto torácico'}

dengue = {'Febre Alta > 38.5°c', 'Dores musculares intensas', 'Dor ao movimentar os olhos', 'Mal estar', 'Perda de apetite',
          'Dor de cabeça', 'Manchas vermelhas no corpo'}

gripe_influenza = {'Febre', 'Dor de garganta', 'Tosse', 'Dor no corpo', 'Dor de cabeça'}

sindrome_gripal = {'Febre', 'Dor de garganta', 'Tosse', 'Coriza', 'Dificuldade para respirar'}

sintomas = {'Perda de olfato (anosmia)', 'Alteração do paladar (ageusia)', 'Náuseas', 'Vômitos', 'Diarreia',
            'Cansaço (astenia)', 'Diminuição do apetite (hiporexia)', 'Dispneia (falta de ar)', 'Chiado no peito',
            'Respiração rápida e curta', 'Desconforto torácico', 'Febre Alta > 38.5°c', 'Dores musculares intensas',
            'Dor ao movimentar os olhos', 'Mal estar', 'Perda de apetite', 'Dor de cabeça', 'Manchas vermelhas no corpo'}

sintomas_paciente = set()  # conjunto vazio

for n in sindrome_gripal:  # iterando em cima de sindrome gripal
    print(f'Você apresenta {n}?')
    print('Responda S/N')
    positivo = input('>>>> ')
    positivo = positivo.upper()  # colocando tudo pra maiusculo
    if positivo == 'S':  # se a resposta for S então
        sintomas_paciente.add(n)  # acrescenta o sintomas ao conjunto de sintomas do paciente

print('Possue algum outro sintoma? S/N')
outro_sintoma = input('>>>> ')
outro_sintoma = outro_sintoma.upper()

if outro_sintoma == 'S':  # caso o paciente tenha mais sintomas
    for n in sintomas:  # iterar em cima o conjunto com o restande dos sintomas
        print(f'Você apresenta {n}?')
        print('Responda S/N')
        positivo = input('>>>> ')
        positivo = positivo.upper()
        if positivo == 'S':
            sintomas_paciente.add(n)  # adicionar ou conjunto de sintomas do paciente

    # Gerando uma porcentagem baseada no sintomas do paciente
    # gera um cojunto pegando apenas os sintomas em comum do conjunto sintomas_paciente e o conjunto (covid_19, asma ...)

    resultado_covid = len(sintomas_paciente.intersection(covid_19)) / len(covid_19) * 100
    resultado_asma = len(sintomas_paciente.intersection(asma)) / len(asma) * 100
    resultado_dengue = len(sintomas_paciente.intersection(dengue)) / len(dengue) * 100
    resultado_gripe = len(sintomas_paciente.intersection(gripe_influenza)) / len(gripe_influenza) * 100

    print(f'Covid-19: {round(resultado_covid, 2)} % de chances!!!')
    print(f'Asma: {round(resultado_asma, 2)} % de chances!!!')
    print(f'Dengue: {round(resultado_dengue, 2)} % de chances!!!')
    print(f'Gripe (influenza): {round(resultado_gripe, 2)} % de chances!!!')

else:
    print('Você possui suspeita de gripe procure um médico')
