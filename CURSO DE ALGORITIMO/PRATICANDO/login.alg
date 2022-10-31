algoritmo "login"
// Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja
//diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a
//mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se
//esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a
//senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.

var
 codigo, digcod, digs, senha: Inteiro
inicio
 codigo <- 1234
 senha <- 9999
 Escreva(" Digite o codigo de usuario : ")
 Leia(digcod)
 Escreva(" Digite a senha: ")
 Leia (digs)
 Se (digcod <> codigo) xou (digs <> senha) entao
    EscrevaL(" Usuario ou senha incorreto ")
 Senao
   se (digcod = codigo) e (digs = senha) entao
 Escreval(" Acesso permitido ")
   fimse
 FimSe
fimalgoritmo
