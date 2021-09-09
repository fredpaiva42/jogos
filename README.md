# Python 3: Introdução à nova versão da linguagem

## Funções Built-in

**→ print( ): esta é a função utilizada para a impressão de uma mensagem ou dado, basta passar a mensagem ou variável como parâmetro para a função.**

- Dentro da função print temos dois parâmetros que podem ser usados: o **sep** e o **end.**
- **Sep="":** com o sep podemos adicionar separadores entre as mensagens como uma vírgula, uma barra e um traço.
- **End="":** com o end podemos definir o que terá após uma mensagem, pode ser um ponto de exclamação, interrogação, \n pra pula de linha, um espaço em branco...

```python
print("Hello World")
# Hello World
print("Hello", "World", sep='-')
# Hello-World
print("Hello World", end='!')
# Hello World!
```

**→ type( ): esta função nos permite identificar qual o tipo da variável, basta apenas passarmos a variável como parâmetro que ela irá nos retornar seu tipo.**

```python
number = 5
print(type(number))
# <class 'int'>
```

**→ input( ):** essa é uma função que nos permite capturar a entrada do usuário, ela trava o programa até que o usuário digite algo e pressione enter. Ela recebe por parâmetro a mensagem que será exibida no console e nos retorna o que o usuário digitou. A função input retorna como default sempre uma string.

```python
entrada = input("Digite um número: ")
```

**→ int( ):** A função int nos permite mudar o tipo de uma variável para inteiro, podemos converter uma string, um float

```python
entrada = input("Digite um número: ") # retorna uma string
number = int(entrada) # converte a string recebida em entrada em um número inteiro.
```

**→ format( ):** essa função nos permite realizar aquilo que é chamado de **interpolação de strings**, com ela nos conseguimos formatar as strings, basta fazer o uso das **{}** na string e passar o nome da variável como parâmetro da função e pronto está funcionado.

```python
dia = 23
mes = 06
ano = 2000

print("Eu nasci em {} do {} de {}".format(dia, mes, ano))
```

## Tipagem Dinâmica

No python nos possuímos uma tipagem dinâmica ou seja não é necessário que definamos qual será o tipo que a variável irá aceitar na sua declaração, a linguagem dinamicamente assimila o tipo de acordo com o valor que é atribuído a ela.

**obs (python):** uma variável só passa a existir assim que atribuímos um valor a ela, se não atribuirmos nenhum valor ela não é considerada como variável inicializada.

**obs2:** em algumas linguagens as variáveis existem mesmo se não inicializadas com valor, nas linguagens como **C, Java e C#**, nesse caso é chamada de **variável estática**, nela só passamos o tipo e nome da variável e ela já passa a existir.

## Estrutura Condicional

Com a estrutura condicional podemos fazer comparações de valores e a partir dessas comparações definir qual caminho será seguido.

- **if():** pode ser usado com parênteses ou sem, essa estrutura condicional representa o **SE**.
- **==:** o igual em python é representado com dois iguais, pois um igual apenas quer dizer atribuição.
- **else:** é uma estrutura em oposição ao if, essa estrutura representa o **SENÃO.**

```python
if (condição):
 # executa código caso a condição seja verdadeira
else:
 # executa código caso a condição seja falsa.
```

- **elif( ):** o elif é basicamente um else, mas com uma condição de entrada, essa estrutura representa um **SENÃO SE**.

```python
if (condição == True):
 # executa esse bloco de código
elif (essa condição == True):
 # esse bloco vai ser executado
else:
 # se nenhuma das outras duas condições forem válidas esse bloco é executado.
```

## Estrutura de Repetição

Com as estruturas de repetições podemos repetir a execução de um bloco de código sem precisar copia-lo várias vezes. Isso é mais prático e torna o código mais legível.

- Quando não sabemos quantas vezes queremos que aquele código se repita então nós podemos usar o **ENQUANTO,** em inglês **While,** o while é bem parecido com o if, ele executa aquele bloco de código quando a condição é verdadeira, a única diferença é que o while vai executar aquele bloco enquanto a condição for verdadeira.

```python
while (condição):
 # executa esse bloco de código até a condição ser falsa.
```

## Diferenças entre Python 2 e Python 3

**obs: uma função no Python 3 deve sempre possuir parênteses.**

### A função print

No Python 2 o uso dos parênteses são **opcionais,** já no Python 3 eles são obrigatórios, e no 3 o print possui os parâmetros **sep e end**, no 2 já não possuía esses parâmetros.

### A função input

No Python 3 essa função sempre nos retorna uma string, já na versão 2 ele fazia conversão do tipo da variável automaticamente. Quando alguém não queria que fosse convertido o tipo da variável era necessário usar o **raw_input(),** algo que não existe na versão 3.
