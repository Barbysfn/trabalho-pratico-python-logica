# 📘 README — Calculadora em Python 🧮

Este projeto consiste na implementação de uma **calculadora interativa em Python**, como parte de um Trabalho Prático da disciplina **"DGT2817 LÓGICA, ALGORITMOS E PROGRAMAÇÃO DE COMPUTADORES"**, seguindo os requisitos fornecidos na atividade.  
A aplicação realiza operações matemáticas básicas e permite que o usuário decida se deseja continuar utilizando o programa ou encerrá-lo.

---

# 📑 Descrição dos requisitos da Tarefa

a. Crie uma variável chamada saida e atribua a ela o valor ‘’;

b. Crie uma função chamada adicao . Tal função deverá receber dois parâmetros e retornar a soma entre ambos;

c. Crie uma função chamada subracao . Tal função deverá receber dois parâmetros e retornar a subtração entre ambos;

d. Crie uma função chamada multiplicacao . Tal função deverá receber dois parâmetros e retornar a multiplicação entre ambos;

e. Crie uma função chamada divisao. Tal função deverá receber dois parâmetros, verificar se um deles é igual a 0. Em caso positivo, deverá retornar a mensagem “Não foi possível realizar a divisão por 0”. Em caso negativo, deverá retornar a divisão entre ambos;

f. Crie uma função chamada calculadora. Tal função deverá receber três parâmetros, sendo eles: os dois números que serão usados para os cálculos e a operação matemática que se deseja realizar. Sobre esse último parâmetro, você poderá utilizar tanto o sinal da operação quanto o seu nome;

g. No corpo da função calculadora você deverá verificar qual a operação desejada pelo usuário, checando o valor do parâmetro correspondente. Utilize estruturas de condição para isso e, dependendo da operação desejada, você deverá chamar a função relativa a ela, passando as variáveis contendo os dois números para serem utilizados no cálculo. Armazene o resultado da chamada às funções de cálculo numa variável chamada resultado. Ao final da função calculadora você deverá retornar a variável resultado;

h. Crie um laço while e, como condição do mesmo, verifique se o valor da variável saída é diferente de n. Lembre-se de que o usuário poderá inserir tanto N quanto n;

i. No escopo do laço while peça ao usuário para digitar o primeiro número e armazene seu valor numa variável. Faça o mesmo para o segundo número e para a operação matemática. Passe essas três variáveis para o método calculadora, armazenando o retorno dessa chamada numa variável também chamada resultado. Imprima na tela o valor da variável resultado precedido pelo texto ‘Resultado da operação: ‘. Por fim, pergunte ao usuário se ele deseja continuar ou não executando o programa. Armazene tal input na variável saida;

j. Tome cuidado com a condição de verificação do laço for em relação à entrada do usuário armazenada na variável saida. Em outras palavras, deixe claro para o usuário as respostas possíveis para a pergunta se ele deseja sair. Use, por exemplo, S/N. Com isso você poderá considerar um desses dois valores na verificação do laço para saber se deve continuar executando o programa ou se deve encerrá-lo.

---

# 🧮 Funcionamento Geral

O programa segue os seguintes passos:

1. Solicita ao usuário:
   - o primeiro número  
   - a operação  
   - o segundo número  

2. Processa a operação dentro da função `calculadora()`  
3. Exibe o resultado formatado  
4. Pergunta se o usuário deseja continuar (S/N)  
5. Continua até que o usuário digite n ou N  
6. Ao encerrar, exibe:  
   **"Encerrando a calculadora. Até mais!"**
