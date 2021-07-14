# NETWORK LAYER

Uso de datagrama. O setor de data-plane envia pelos links, o controle faz a direção; 

Papel do NL enviar o pacote através de diferentes roteadores: dentro do roteador, rápido. de um link para outro

Rotear, determinar qual rota tomar. Feito pelo control plane. 

Roteadores têm tabela de forwading para comparar com header e saber para onde mandar. um algoritmo roda (control) intermamente 
e se comunica com outros roteadores  para saber para onde mandar. 

Esse algoritmo altera a tabela forwarding (control plane)

Outra maneira é __Software-defined networking__ em que as tabelas de forwarding são feitos por um computador remoto 

A camada de rede oferece apenas melhor esforço para entregar pacotes

Switch se baseia na camada enlace

Router na de rede

## Partes do Hardware

- Porta de input - faz terminação física do link de chegada, além da transição. Por último faz a validação 
, olhando para onde irá, para qual porta de output.

- Switching fabric: uma ligação para input para output

- Routing processing: faz a parte do data plane com forwading table ou se comunica com SDN

Todos são implementados a nível de Hardware pois é muito rápido 

Mas a parte de Control Plane, como executar protcolos, adm e comunicação com SDN são por software. 

### Funções: 

Destionation-based forwarding para entrada e saída NO FINAL

Generalized forwarding usa várias características que devem ser processadas ali 

Vários gargalos: input, output, capacidade total da switching fabric, processamento de informações pelo control plane 
e seu routing processor 

O routing processor envia a tabela de forwading para a s portas por um line card, então a decisaão de forward é local - impede um botlleneck 

### Input processing

Um IP de 32 bits não teria como ser calculado. Então roteador usa prefixos, uma porta default e o maior prefixo para determinar para qual porta enviar. 

O roteador faz um uso de match and action para sua tarefa. Match o prefixo, action para porta

O processo de switching dentro da switching fabric pode ser pela memória lê e depois encaminha

pode ser por um prefixo anterior, daí só passa para todas portas e elas decidem se ficam com pacote

outra tecnica é com intercruzamento que apenas intersseções são fechadas quando vários pacotes estão. 

### Output processing

Coloca as partes da camada de enlace e física. Estoca até chegar, faz scheduling. Essas queus sao onde os pacotes dropam 

### Exemplo de queieing

Pacotes chegam de forma síncrona, de mesmo tamanho e link de saída e entrada tem mesma velocidade Rline. N portas de saída e de entrada


Rswitch para velocidade da switching fabric. 

Se Rswitch >> Rline, não tem queing, pois sempre que chega um o Rswitch se livra fácil 

Se nao, tem queue quando a porta de saída é igual. E por consequência bloqueia as de trás nesse input de entrada, mesmo que nao vá para porta em comum 

Pode ocorrer também na saída quando a fábrica é mais rápido que a vazão dele e daí quando overflow a memória perde pacote. Por isso deve existir um mecanismo para decidir qual sai. 

### Tamanho do buffer

tem relação com a rede em si. A formula atual é __B= RTT * C/SQRT(n)__ (onde N é numero de independente TCP flow, C é capacidade a do link)

Não necessariamente mais buffer é melhor, pois como a relação mostra, mais BUFFER aumenta o RTT é portanto o delay.

É possível que isso gere um delay constante no router de saída. Ou seja, um __bufferbloat__

## Agendamento de pacote

### FIFO

Entra primeiro sai primeiro 

### Priority queuing

Alguns tipos (dependendo da porta) recebe prioridade por classe que pertence (Exemplo IPvoice sobre email) e daí vai para input port diferentes dentro do Router

Daí roteador manda sempre da primeira classe e dentro dela manda por FIFO.










