# Aula 2 

## Gerenciamento da tabela de símbolos

- Essa atividade registra os identificadores do programa alvo e identifica seus diversos atributos. 
- Exemplos de possíveis atributos de um identificador: nome, tipo, memória e escopo. 
- Caso o identificador se refira a um procedimento, dentre seus atributos devem constar a quantidade de seus parâmetros e respectivos tipos, modos de passagem (cópia ou referência) e o tipo do retorno, se houve.
- Os identificadores e seus respectivos atributos são armazenados em uma estrutura denominada tabela de símbolo. 
- A cada fase da compilação podem acontecer um ou mais erros.
- Após a identificação do erro, o compilador deve tratá-lo de alguma maneira e, se possível, continubar o processo em busca de outros erros. 
- Abortar a compilação logo no primeiro erro pode diminuir a utilidade do compilador. 
- As análise sintática e semântica podem identificar uma parcela considerável dos erros no programa fonte. 



Exemplo de erro semântico: 
`
if (x=5){
    ...
}
`

### Exemplo da parte da análise do programa fonte

`celsius = 1.8 * fahrenheit + 32` -> Analisador léxico -> `id1 = 1.8 * id2 + 32` -> análise sintática -> árvore sintática

<!-- @TODO: inserir imagens -->

### Geração de código intermédiário

A utilização do código intermediário visa aumentar o reaproveitamento do compilador para outras linguagens. 

> 




