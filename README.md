# Trabalho1-ProgramaDeSockets-RedesDeComputadores
Trabalho introdutório à programação em sockets. Irá ser desenvolvido duas aplicações, uma sendo cliente que se conecta a um servidor e uma aplicação servidor.

# Descrição
## Cliente
1. O cliente irá se conectar ao servidor.
2. Gerar um número inteiro com até 30 casas.
3. Enviar para o servidor.
4. O cliente deve receber, imprimir no console e devolver o valor recebido do servidor + "FIM".
5. Fecha conexão.
Repete a cada 10 segundos
## Servidor
1. O servidor irá esperar a conexão do cliente.
2. Recebe o número.
3. Se esse número for maior que 10 casas, gera e envia uma string de mesmo tamanho para o cliente.
4. Se esse número for menor que 10 casas, verifica se é par ou ímpar e envia "PAR" ou "ÍMPAR" para o cliente.

# Funcionamento
O serviço de transporte usado para desenvolver essa aplicação foi de TCP, já que seu objetivo é transmitir dados.
## Cliente
Inicialmente foi feita a importação de socket, randint e time. Logo em seguida, foi definido o endereço IP do servidor e a porta a ser utilizada, também foi definido o tamanho do número de casas e tempo a ser executado. Conectamos o cliente ao servidor e geramos um número para o servidor. Recebemos a resposta dada pelo servidor e imprimimos a sua resposta. A cada 10 segundos se conecta novamente ao servidor.
## Servidor
Inicialmente foi feita a importação de socket, string e random. Logo em seguida, foi definido o endereço IP do servidor e a porta a ser utilizada, também foi definido o random_string para que seja retornado um número aleatório. Esperamos que uma conexão seja feita, após aceita recebe o número enviado pelo cliente e conecta. Verificamos o tamanho do número e retornamos a mensagem com a resposta e por fim, verificamos se o número é ímpar ou par.
