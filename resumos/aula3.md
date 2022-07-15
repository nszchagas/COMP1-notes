# Aula 3 - Análise Léxica

## Analisador léxico

Recebe como entrada o programa fonte e gera como saída uma sequência de tokens.

Uma das formas de construir um analisador léxico é escrever um diagrama que ilustre a estrutura dos tokens da linguagem fonte e o traduzir manualmente com um programa que os identifica.

- Pode realizar também tarefas secundárias a nível de interface com o usuário, como a remoção de espaços e comentários por exemplo.

### Interação entre o analisador léxico e o parser

<!-- @TODO: inserir imagem -->

### Tokens, padrões e lexemas

- Tokens são símbolos terminais da linguagem fonte (por exemplo if, else, dígitos, caracteres, operadores, etc.);
- Lexema são conjuntos de caracteres que são reconhecidos como um token.
- Um padrão descreve o conjunto de lexemas que podem representar um token em particular (quando há mais de um lexema possível para gerar um token).

### Atributos para tokens

- Quando um token pode estar associado a dois ou mais lexemas, o analisador léxico deve prover atributos para os tokens para as fases subsequentes, para que ela possa distingui-los.

Exemplos:
- Em tokens numéricos, o valor do número representado pelo lexema pode ser o atributo do token.
- Para identificadores, o próximo lexema pode ser o atributo do token (`int numero`).

### Erros léxicos

Determinados erros não podem ser detectados em nível léxico, como por exemplo o erro abaixo.

```c 
    fi (a==f(x)) {
        ...
    }
```

Os erros léxicos mais comuns são aqueles onde o analisador léxico não consegue associar o prefixo lido a nenhum dos padrões associados aos tokens da linguagem. Nesse ponto, o analisador pode abortar a leitura, emitindo uma mensagem de erro, ou tratar o erro de alguma maneira.

Há quatro ações que configuram tentativas de recuperação de erros léxicos:

- Remover um caractere estranho da entrada;
- Inserir um caractere ausente;
- Substituir um dos caracteres incorretos por um caractere correto;
- Transpor dois caracteres adjacentes.

> Se uma ou mais das ações acima conseguir tornar o prefixo em um token válido, o analisador pode indicar ao usuário a sequência de ações como sugestão de correção do programa fonte, ou mesmo prosseguir assumindo esta correção.

### Buferização

- O acesso à entrada pode ser o gargalo, em termos de performance, do compilador.
- A buferização consiste no uso de um ou mais vetores auxiliares (buffers) que permitem a leitura da entrada em blocos, de moto que o analisador léxico leia os caracteres a partir destes buffers, os quais são atualizados e preenchidos à medida do necessário, o que reduz o acesso ao disco.

### Estratégias para implementação de analisadores léxicos

### Pares de buffers



