<div align="center">

# 🐍 Python 3 — Mundo 1 
**Curso em Vídeo & Estudonauta**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Concluído-4CAF50?style=for-the-badge)
![Carga Horária](https://img.shields.io/badge/Carga_Horária-40h-FF9800?style=for-the-badge&logo=clockify&logoColor=white)
![Plataforma](https://img.shields.io/badge/Curso_em_Vídeo-Estudonauta-151515?style=for-the-badge&logo=youtube&logoColor=red)
![Licença](https://img.shields.io/badge/Licença-MIT-1081c2?style=for-the-badge)

---
*Repositório contendo a resolução prática e documentada dos **35 exercícios** propostos no módulo **Mundo 1** do curso de Python 3, ministrado pelo professor **Gustavo Guanabara**.*
</div>

<br>

## 📚 Sobre o Módulo 1

O **Mundo 1** compreende a fase introdutória e de fundamentação lógica na linguagem Python. Ao longo de 40 horas de carga horária, o treinamento aborda a sintaxe essencial, manipulação de tipos nativos, modularização e estruturas de controle de fluxo básicas.

### 🎯 Tópicos Abordados por Fases:
* **Fases 01 a 04 — Primeiros Passos e Tipos Primitivos:** Configuração de ambiente, entrada e saída de dados (`input` e `print`), interpolação de strings (`.format()` e *f-strings*), tipagem primitiva (`int`, `float`, `bool`, `str`) e validações de tipos com métodos de introspecção.
* **Fases 05 e 07 — Operadores Aritméticos:** Operadores fundamentais (`+`, `-`, `*`, `/`, `//`, `%`, `**`), precedência matemática e formatação numérica.
* **Fase 08 — Utilizando Módulos:** Importação de bibliotecas padrão (`math`, `random`) e pacotes externos via gerenciador de dependências (`pygame` para reprodução de mídia).
* **Fase 09 — Manipulando Texto:** Fatiamento de strings, métodos de transformação, análise de caracteres e divisão/junção (`.split()`, `.join()`).
* **Fase 10 — Condições (Parte 1):** Estruturas condicionais simples e compostas (`if` e `else`), operadores relacionais e lógica booleana.

---

## 🗂️ Lista Detalhada de Exercícios (001 a 035)

| Desafio | Título do Exercício | Descrição do Problema | Funções & Recursos Principais |
| :---: | :--- | :--- | :--- |
| **001** | Deixando tudo pronto | Imprimir uma mensagem clássica de boas-vindas na tela. | `print()` |
| **002** | Respondendo ao Usuário | Ler o nome do usuário e exibir uma mensagem interativa formatada. | `input()`, *f-strings* |
| **003** | Somando dois números | Coletar dois números pelo teclado, realizar a conversão de tipo e exibir a soma. | `int()`, coerção de tipos |
| **004** | Dissecando uma Variável | Analisar o dado digitado exibindo tipo primitivo e validações booleanas. | `.isnumeric()`, `.isalpha()`, `.isspace()` |
| **005** | Antecessor e Sucessor | Calcular e exibir o número antecessor e o sucessor de um valor informado. | Operadores aritméticos (`+`, `-`) |
| **006** | Dobro, Triplo e Raiz Quadrada | Determinar as três métricas matemáticas de um número de entrada. | Operador `**`, radiciação |
| **007** | Média Aritmética | Calcular a média aritmética entre duas notas de um aluno. | Precedência de operadores `()` |
| **008** | Conversor de Medidas | Converter uma distância em metros para centímetros, milímetros, km, etc. | Operadores de multiplicação e divisão |
| **009** | Tabuada v1.0 | Exibir a tabuada completa de multiplicação (1 a 10) de um número inteiro. | Formatação de saída em tabela |
| **010** | Conversor de Moedas | Calcular a quantidade de dólares que uma quantia em reais (BRL) pode comprar. | Divisão real e formatação de casas decimais |
| **011** | Pintando Parede | Calcular a área de uma parede e o total de tinta necessária (1L cobre 2m²). | Cálculos geométricos simples |
| **012** | Calculando Descontos | Aplicar uma taxa percentual de desconto (5%) sobre o preço de um produto. | Cálculo de porcentagem (`preço * 0.95`) |
| **013** | Reajuste Salarial | Calcular o novo salário de um funcionário após um reajuste de 15%. | Cálculo de acréscimo percentual |
| **014** | Conversor de Temperaturas | Converter temperaturas lidas de graus Celsius (°C) para Fahrenheit (°F). | Fórmula de conversão de escala |
| **015** | Aluguel de Carros | Calcular o preço total a pagar com base nos dias alugados e km rodados. | Acúmulo de valores monetários |
| **016** | Quebrando um número | Ler um número real e exibir apenas a sua porção inteira. | `math.trunc()` ou cast para `int()` |
| **017** | Catetos e Hipotenusa | Calcular o comprimento da hipotenusa a partir dos catetos oposto e adjacente. | `math.hypot()` |
| **018** | Seno, Cosseno e Tangente | Calcular seno, cosseno e tangente com base em um ângulo informado em graus. | `math.sin()`, `math.cos()`, `math.radians()` |
| **019** | Sorteando um item na lista | Escolher aleatoriamente um entre quatro alunos informados. | `random.choice()` |
| **020** | Sorteando uma ordem na lista | Embaralhar e definir a ordem de apresentação de trabalhos de quatro alunos. | `random.shuffle()` |
| **021** | Tocando um MP3 | Inicializar o mixer de áudio e executar a reprodução de um arquivo `.mp3`. | Biblioteca `pygame.mixer` |
| **022** | Analisador de Textos | Tratar nome completo: maiúsculas, minúsculas, tamanho sem espaços e primeiro nome. | `.upper()`, `.lower()`, `.strip()`, `len()` |
| **023** | Separando dígitos de um número | Extrair matematicamente unidade, dezena, centena e milhar de um número. | Operadores `//` e `%` |
| **024** | Verificando as primeiras letras | Checar se o nome de uma cidade começa com a palavra `"SANTO"`. | `.strip()`, `.upper()`, fatiamento `[:5]` |
| **025** | Procurando string em outra | Identificar se a string informada contém o sobrenome `"SILVA"`. | Operador de pertencimento `in` |
| **026** | Primeira e última ocorrência | Contar vezes que `"A"` aparece e posições da primeira e última ocorrência. | `.count()`, `.find()`, `.rfind()` |
| **027** | Primeiro e último nome | Dividir uma string de nome completo e isolar o primeiro e o último elemento. | `.split()`, indexação `[0]` e `[-1]` |
| **028** | Jogo da Adivinhação v1.0 | Computador sorteia um número de 0 a 5 e valida o palpite do jogador. | `random.randint()`, `if/else` |
| **029** | Radar Eletrônico | Ler velocidade; se ultrapassar 80 km/h, aplica multa calculada por excesso. | Condicional simples |
| **030** | Par ou Ímpar? | Identificar e classificar um número inteiro como par ou ímpar. | Operador módulo (`% 2 == 0`) |
| **031** | Custo da Viagem | Calcular preço da passagem: tarifa padrão (até 200 km) ou tarifa reduzida. | Estruturas condicionais (`if/else`) |
| **032** | Ano Bissexto | Verificar se determinado ano informado (ou o atual) é bissexto. | Lógica booleana (`and`/`or`) |
| **033** | Maior e Menor Valores | Identificar o maior e o menor valor entre três números fornecidos. | Condicionais encadeadas |
| **034** | Aumentos Múltiplos | Calcular reajustes percentuais com base na faixa salarial do colaborador. | Condições compostas |
| **035** | Analisando Triângulo v1.0 | Avaliar três retas e determinar se elas podem formar um triângulo. | Desigualdade triangular |

---

## 🚀 Como Executar os Projetos

### Pré-requisitos
* **Python 3.8+** instalado no ambiente de desenvolvimento.
* Gerenciador de pacotes **pip** configurado.

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/python3-mundo1.git](https://github.com/seu-usuario/python3-mundo1.git)
cd python3-mundo1
```
### 👨‍💻 Autor
Desenvolvido por **Vinícius Esteves**.
