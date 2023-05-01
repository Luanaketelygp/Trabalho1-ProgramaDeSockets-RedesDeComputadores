# Trabalho1-ProgramaDeSockets-RedesDeComputadores
Trabalho introdutório à programação em sockets. Irá ser desenvolvido duas aplicações, uma sendo cliente que se conecta a um servidor e uma aplicação servidor.

# Descrição
  # Cliente
1. O cliente irá se conectar ao servidor.
2. Gerar um número inteiro com até 30 casas.
3. Enviar para o servidor.
4. O cliente deve receber, imprimir no console e devolver o valor recebido do servidor + "FIM".
5. Fecha conexão.
Repete a cada 10 segundos
  # Servidor
1. O servidor irá esperar a conexão do cliente.
2. Recebe o número.
3. Se esse número for maior que 10 casas, gera e envia uma string de mesmo tamanho para o cliente.
4. Se esse número for menor que 10 casas, verifica se é par ou ímpar e envia "PAR" ou "ÍMPAR" para o cliente.
