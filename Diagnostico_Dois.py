"""
Código diagnostico de doenças
"""

print('------------------------ Pré-Diagnóstico de doenças ------------------------')

# Listas de sintomas
asma = ['Tosse', 'Chiado no peito', 'Dificuldade para respirar', 'Respiração rápida e curta', 'Desconforto torácico', 'Ansiedade']

caxumba = ['Inchaço e dor nas glândulas salivares', 'Febre', 'Dor de cabeça',
           'Fadiga', 'Perda de apetite', 'Dor ao mastigar', 'Dor ao engolir']

chikungunya = ['Febre', 'Dores intensas nas juntas', 'Pele e olhos avermelhados', 'Dor no corpo',
               'Dor de cabeça', 'Náuseas', 'Vômitos']

covid_19 = ['Tosse', 'Dor de garganta', 'Coriza', 'Perda de olfato', 'Perda de paladar', 'Diarreia',
            'Dor abdominal', 'Febre', 'Calafrios', 'Dor no corpo', 'Fadiga', 'Dor de cabeça ']


dengue = ['Febre', 'Dores musculares intensas', 'Dor ao movimentar os olhos', 'Mal estar', 'Perda de apetite',
          'Dor de cabeça', 'Manchas vermelhas no corpo']

gripe = ['Febre', 'Dor de garganta', 'Tosse', 'Dor no corpo', 'Dor de cabeça']

tuberculose = ['Febre', 'Sudorese noturna', 'Perda de peso', 'Fadiga']

hipertensao = ['Dores no peito', 'Dor de cabeça', 'Tonturas', 'Zumbido no ouvido', 'Fraqueza', 'Visão embaçada', 'Sangramento nasal']

sintomas = ['Febre', 'Tosse', 'Dor de garganta', 'Dor no corpo', 'Dor de cabeça', 'Coriza',
            'Perda de olfato', 'Perda de paladar', 'Diarreia', 'Dor abdominal', 'Calafrios',
            'Fadiga', 'Inchaço e dor nas glãndulas salivares', 'Perda de apetite',
            'Dor ao mastigar', 'Dor ao engolir', 'Dores intensas nas juntas', 'Pele e olhos avermelhados',
            'Náuseas', 'Vômitos', 'Dores musculares intensas', 'Dor ao movimentar os olhos', 'Mal estar',
            'Manchas vermelhas no corpo', 'Sudorese noturna', 'Perda de peso', 'Chiado no peito',
            'Dificuldade para respirar', 'Respiração rápida e curta', 'Desconforto torácico', 'Ansiedade', 'Dores no peito',
            'Tonturas', 'Zumbido no ouvido', 'Fraqueza', 'Visão embaçada', 'Sangramento nasal']

lista_sintomas = []


def funcao(lista):  # função para iterar sobre a lista sintomas
    for i in lista:
        print(f' \nVocê apresenta {i}?')  # pergunta se a pessoa tem ou não determinado sintoma
        print('Responda Sim(S) ou Não (N)')
        positivo = input('>>> ')
        positivo = positivo.upper()  # trasnforma tudo pra letra maiuscula
        if positivo == 'S':  # caso ele tenha tal sintoma
            lista_sintomas.append(i)  # acrescenta na lista lista_sintomas


funcao(sintomas[0:5])  # inicia-se com os primeiros 5 sintomas da lista

for i in range(5, 37, 4):  # gerando os valores de i
    j = i + 4  # gerando valores de j
    print('\nVoce possui mais sintomas?')
    print('Responda Sim(S) ou Não (N)')
    confirm = input('>>> ')
    confirm = confirm.upper()
    if confirm == 'S':  # caso a pessoa tenha mais sintomas outros 4 sintomas aparecrão pra ela na tela
        funcao(sintomas[i:j])  # passa como parametro a sub lita que vai de i até j
    else:
        break

# converte as listas em conjuntos
asma = set(asma)
caxumba = set(caxumba)
chikungunya = set(chikungunya)
covid_19 = set(covid_19)
dengue = set(dengue)
gripe = set(gripe)
tuberculose = set(tuberculose)
hipertensao = set(hipertensao)
lista_sintomas = set(lista_sintomas)

# cria a porcentagem de cada doença
porcentagem_asma = len(lista_sintomas.intersection(asma)) / len(asma) * 100
porcentagem_caxumba = len(lista_sintomas.intersection(caxumba)) / len(caxumba) * 100
porcentagem_chikungunya = len(lista_sintomas.intersection(chikungunya)) / len(chikungunya) * 100
porcentagem_covid = len(lista_sintomas.intersection(covid_19)) / len(covid_19) * 100
porcentagem_dengue = len(lista_sintomas.intersection(dengue)) / len(dengue) * 100
porcentagem_gripe = len(lista_sintomas.intersection(gripe)) / len(gripe) * 100
porcentagem_tuberculose = len(lista_sintomas.intersection(tuberculose)) / len(tuberculose) * 100
porcentagem_hipertensao = len(lista_sintomas.intersection(hipertensao)) / len(hipertensao) * 100

porcentagem = [porcentagem_asma, porcentagem_caxumba, porcentagem_chikungunya, porcentagem_covid,
               porcentagem_dengue, porcentagem_gripe, porcentagem_tuberculose, porcentagem_hipertensao]

# cria a lista da diferença entre os conjuntos
diferenca_covid = list(lista_sintomas.difference(covid_19))
diferenca_gripe = list(lista_sintomas.difference(gripe))
diferenca_caxumba = list(lista_sintomas.difference(caxumba))
diferenca_chikungunya = list(lista_sintomas.difference(chikungunya))
diferenca_dengue = list(lista_sintomas.difference(dengue))
diferenca_tuberculose = list(lista_sintomas.difference(tuberculose))
diferenca_asma = list(lista_sintomas.difference(asma))
diferenca_hipertensao = list(lista_sintomas.difference(hipertensao))

maior = 0

# define qual tem a maior porcentagem:
for i in porcentagem:
    if maior < i:
        maior = i


if maior == porcentagem_asma and maior != 0:
    print("    Você apresenta em maioria sintomas de Asma, é fundamental procurar a unidade de sáude mais próxima"
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_asma) != 0:  # se a lista diferença não estiver vazia, significa que o usuário marcou algum sitoma
        # que não corresponde a essa doença
        print(f'\n    Você tambem possui outros sintomas que não são comuns a Asma, que são: {", ".join(diferenca_asma)}')

elif maior == porcentagem_gripe and porcentagem_covid > 40 and maior != 0:  # como a lista covid é maior que a da gripe e ambas
    # contem os sintomas da gripe pode gerar um erro dando sempre a gripe como tendo uma porcentagem maior que a do covid,
    #  então mesmo se a gripe der 100%, mais o covid der 40 % o passiente tem mais probabilidade de estar com covid...
    print("    Você apresenta em maioria sintomas de Covid_19, é fundamental procurar a unidade de sáude mais próxima "
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar "
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_covid) != 0:
        print(f'    Você tambem possui outros sintomas que não são comuns a Covid, que são: {", ".join(diferenca_covid)}')

elif maior == porcentagem_caxumba and maior != 0:
    print("    Você apresenta em maioria sintomas de Caxumba, é fundamental procurar a unidade de sáude mais próxima "
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_caxumba) != 0:
        print(f'\n    Você tambem possui outros sintomas que não são comuns a Caxumba, que são: {", ".join(diferenca_caxumba)}')

elif maior == porcentagem_chikungunya and maior != 0:
    print("    Você apresenta em maioria sintomas de Chikungunya, é fundamental procurar a unidade de sáude mais próxima"
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_chikungunya) != 0:
        print(f'\n    Você tambem possui outros sintomas que não são comuns a Chikungunya, que são: {", ".join(diferenca_chikungunya)}')

elif maior == porcentagem_gripe and porcentagem_covid < 40 and maior != 0:  # como a lista covid é maior que a da gripe e ambas
    # contem esses sintomas caso a covid_19 tenha mais que 40 % então significa que o pacinte tem mais chances de estar com covid
    print("    Você apresenta em maioria sintomas de Gripe(influenza), é fundamental procurar a unidade de sáude mais próxima "
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar "
          "o tratamento.")
    if len(diferenca_gripe) != 0:
        print(f'\n    Você tambem possui outros sintomas que não são comuns a gripes, que são: {", ".join(diferenca_gripe)}')


elif maior == porcentagem_dengue and maior != 0:
    print("    Você apresenta em maioria sintomas de Dengue, é fundamental procurar a unidade de sáude mais próxima"
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_dengue) != 0:
        print(f'\n    Você tambem possui outros sintomas que não são comuns a Dengue, que são: {", ".join(diferenca_dengue)}')

elif maior == porcentagem_tuberculose and maior != 0:
    print("    Você apresenta em maioria sintomas de Tuberculose, é fundamental procurar a unidade de sáude mais próxima"
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_tuberculose) != 0:
        print(f'Você tambem possui outros sintomas que não são comuns a Turbeculose, que são: {", ".join(diferenca_tuberculose)}')

elif maior == porcentagem_hipertensao and maior != 0:
    print("    Você apresenta em maioria sintomas de Hipertensão, é fundamental procurar a unidade de sáude mais próxima"
          "da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar"
          "o tratamento o mais rápido possivel e segui-lo até o final.")
    if len(diferenca_tuberculose) != 0:
        print(f'Você tambem possui outros sintomas que não são comuns a Hipertensão, que são: {", ".join(diferenca_hipertensao)}')

else: # caso não escolha nenhum sintoma
    print('    Aparentemente você não apresenta nenhum sintoma, porem existem pacientes que mesmo estando com alguma doença, '
          'não apresentam sintomas, como é o caso do Covid-19. Caso tenha tido contato com, nos ultimos 14 dias com um caso'
          'diagnosticado de Covid 19, é fundamental procurar a unidade de sáude mais próxima'
          'da sua residencia para avaliação e realização de exames. Se o resultado der positivo, deve-se iniciar'
          'o tratamento o mais rápido possivel e segui-lo até o final.')

print('\n Caso queira saber mais sobre alguma doença digite: Sim(S) ou Não(N)')
n = input('>>> ')

t = 'S'
if n == 's':
    for k in range(1, 8, 1):
        if t == 'S':
            print('\n1 - Asmas; \n'
                '2- Caxumba; \n'
                '3- Chikungunya; \n'
                '4- Covid_19;\n'
                '5- Dengue; \n'
                '6- Gripe(influenza) \n'
                '7- Hipertensao \n'
                '8- Tuberculose \n')
            num = int(input('Digite o número da doença \n>>>'))

            if num == 1:
                print('O que é asma? \n'
                    '\n    Asma é uma das doenças respiratórias crônicas mais comuns, juntamente com a rinite alérgica e a '
                    'doença pulmonar obstrutiva crônica. As principais características dessa doença pulmonar são dificuldade '
                    'de respirar, chiado e aperto no peito, respiração curta e rápida e ansiedade. Os sintomas pioram à noite e nas '
                    'primeiras horas da manhã ou em resposta à prática de exercícios físicos, à exposição a alérgenos, '
                    'à poluição ambiental e a mudanças climáticas.\n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/a/asma')
            elif num == 2:
                print('O que é caxumba?\n'
                    '\n    A caxumba é uma infecção viral aguda e contagiosa. Pode atingir qualquer tecido glandular e nervoso '
                    'do corpo humano, mas é mais comum afetar as glândulas parótidas, que produzem a saliva, ou as s'
                    'ubmandibulares e sublinguais, próximas ao ouvido. As principais caracteristicas dessa doença são Inchaço '
                    'e dor nas glândulas salivares, febre, dor de cabeça, fadiga, perda de apetite, dor ao mastigar e engolir.\n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/c/caxumba')
            elif num == 3:
                print('O que é chikungunya?\n'
                    '\n    A Febre pelo vírus Chikungunya é um arbovírus. Arbovírus são aqueles vírus transmitidos por picadas de'
                    ' insetos, especialmente mosquitos, mas tambem pode ser um carrapatos ou outros. O transmissor (vetor) do'
                    ' chikungunya é o mosquito Aedes aegypti, que precisa de água parada para proliferar, portanto, o período '
                    ' do ano com maior transmissão são os meses mais chuvosos de cada região. As principais caracteristicas '
                    'dessa doença são febre, dores intensas nas juntas, pele e olhos vermelhos, dores pelo corpo, dor de cabeça'
                    'nâuseas e vômitos.\n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/c/chikungunya')
            elif num == 4:
                print('O que é a Covid-19?\n'
                    '\n    A Covid-19 é uma infecção respiratória aguda causada pelo coronavírus SARS-CoV-2, potencialmente grave, '
                    'de elevada transmissibilidade e de distribuição global.\n'
                    '    O SARS-CoV-2 é um betacoronavírus descoberto em amostras de lavado broncoalveolar obtidas de pacientes '
                    'com pneumonia de causa desconhecida na cidade de Wuhan, província de Hubei, China, em dezembro de 2019. '
                    'Pertence ao subgênero Sarbecovírus da família Coronaviridae e é o sétimo coronavírus conhecido a infectar '
                    'seres humanos.\n'
                    'As principais caracteristicas dessa doença são tosse, dor de garganta ou coriza, seguido ou não de anosmia, '
                    'ageusia, diarreia, dor abdominal, febre, calafrios, mialgia, fadiga e/ou cefaleia.'
                    '\n Para mais informações acesse: https://coronavirus.saude.gov.br/')
            elif num == 5:
                print('O que é dengue?\n '
                    '\n    Dengue é uma doença febril grave causada por um arbovírus. Arbovírus são vírus transmitidos por picadas '
                    'de insetos, especialmente os mosquitos. Existem quatro tipos de vírus de dengue (sorotipos 1, 2, 3 e 4). '
                    'Cada pessoa pode ter os 4 sorotipos da doença, mas a infecção por um sorotipo gera imunidade permanente '
                    'para ele.\n'
                    '    Todas as faixas etárias são igualmente suscetíveis, porém as pessoas mais velhas têm maior risco de '
                    'desenvolver dengue grave e outras complicações que podem levar à morte. O risco de gravidade e morte '
                    'aumenta quando a pessoa tem alguma doença crônica, como diabetes e hipertensão, mesmo tratada.'
                    'As principais caracteristicas dessa doença são febre, dores musculares intensas, dor ao movimentar os olhos,'
                    'mal estar, perda de apetite, dor de cabeça, manchas vermelhas no corpo.\n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/d/dengue')
            elif num == 6:
                print('O que é gripe (influenza)?\n'
                    '\n    A gripe é uma infecção aguda do sistema respiratório, provocado pelo vírus da influenza, com grande '
                    'potencial de transmissão. O vírus da gripe (Influenza) propaga-se facilmente e é responsável por elevadas '
                    'taxas de hospitalização.Existem quatro tipos de vírus influenza/gripe: A, B, C e D.'
                    'As principais caracteristicas dessa doença são febre, dor de garganta, tosse, dor no corpo, dor de cabeça. \n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/g/gripe-influenza')
            elif num == 7:
                print('O que é hipertensão?\n'
                    '\n    A hipertensão arterial ou pressão alta é uma doença crônica caracterizada pelos níveis elevados da '
                    'pressão sanguínea nas artérias. Ela acontece quando os valores das pressões máxima e mínima são iguais ou '
                    'ultrapassam os 140/90 mmHg (ou 14 por 9). '
                    '    Os sintomas da hipertensão costumam aparecer somente quando a pressão sobe muito: podem ocorrer dores no '
                    'peito, dor de cabeça, tonturas, zumbido no ouvido, fraqueza, visão embaçada e sangramento nasal.\n'
                    '\n Para mais informações acesse: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z-1/h/hipertensao-pressao-alta')

            elif num == 8:
                print('O que é tuberculose?\n'
                    '\n    A tuberculose é uma doença infecciosa e transmissível que afeta prioritariamente os pulmões, embora possa '
                    'acometer outros órgãos e/ou sistemas. A doença é causada pelo Mycobacterium tuberculosis ou bacilo de Koch.'
                    'As principais caracteristicas dessa doença são febre, sudorese noturna, emagrecimento, fadiga. \n'
                    '\n Para mais informações acesse: http://antigo.saude.gov.br/saude-de-a-z/tuberculose')

            else:
                print('Numero invalido!!!')

            print('\n Gostaria de saber mais sobre alguma outra doença digite: Sim(S) ou Não(N)')
            t = input('>>> ')
            t = t.upper()
        else:
            print('\n Obrigado por utilziar nosso Pré-Diagnóstico de Doenças!')
            break
else:
    print('\n Obrigado por utilziar nosso Pré-Diagnóstico de Doenças!')
