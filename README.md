# Python 3: Introdução à nova versão da linguagem

## Funções Built-in:

**→ print( ): esta é a função utilizada para a impressão de uma mensagem ou dado, basta passar a mensagem ou variável como parâmetro para a função.**

- Dentro da função print temos dois parâmetros que podem ser usados: o **sep** e o **end.**
- **Sep="":** com o sep podemos adicionar separadores entre as mensagens como uma vírgula, uma barra e um traço.
- **End="":** com o end podemos definir o que terá após uma mensagem, pode ser um ponto de exclamação, interrogação, \n pra pula de linha, um espaço em branco...

**→ type( ): esta função nos permite identificar qual o tipo da variável, basta apenas passarmos a variável como parâmetro que ela irá nos retornar seu tipo.**

**→ input( ):** essa é uma função que nos permite capturar a entrada do usuário, ela trava o programa até que o usuário digite algo e pressione enter. Ela recebe por parâmetro a mensagem que será exibida no console e nos retorna o que o usuário digitou. A função input retorna como default sempre uma string.

**→ int( ):** A função int nos permite mudar o tipo de uma variável para inteiro, podemos converter uma string, um float...

## Tipagem Dinâmica:

No python nos possuimos uma tipagem dinâmica ou seja não é necessário que definamos qual será o tipo que a variável irá aceitar na sua declaração, a linguagem dinâmicamente assimila o tipo de acordo com o valor que é atribuído a ela.

**obs (python):** uma variável só passa a existir assim que atribuímos um valor a ela, se não atribuirmos nenhum valor ela não é considerada como variável inicializada.

**obs2:** em algumas linguagens as variáveis existem mesmo se não inicializadas com valor, nas linguagens como **C, Java e C#**, nesse caso é chamada de **variável estática**, nela só passamos o tipo e nome da variável e ela já passa a existir.

## Estrutura Condicional:

Com a estrutura condicional podemos fazer comparações de valores e a partir dessas comparações definir qual caminho será seguido.

- **if():** pode ser usado com parenteses ou sem, essa estrutura condicional representa o **SE**.
- **==:** o igual em python é representado com dois iguais, pois um igual apenas quer dizer atribuição.
- **else:** é uma estrutura em oposição ao if, essa estrutura representa o **SENÃO.**

```python
if (condição):
 # executa código caso a condição seja verdadeira
else:
 # executa código caso a condição seja falsa.
```

## Diferenças entre Python 2 e Python 3

**obs: uma função no Python 3 deve sempre possuir parênteses.**

### A função print:

No Python 2 o uso dos parênteses são **opcionais,** já no Python 3 eles são obrigatórios, e no 3 o print possui os parâmetros **sep e end**, no 2 já não possuia esses parâmetros.

### A função input:

No Python 3 essa função sempre nos retorna uma string, já na versão 2 ele fazia conversão do tipo da variável automaticamente. Quando alguém não queria que fosse convertido o tipo da variável era necessário usar o **raw_input(),** algo que não existe na versão 3.
