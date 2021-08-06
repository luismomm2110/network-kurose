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

### Round Robin

Faz por classe e daí vai rodando de classe...  como scheduler

Agora por __WEIGTHTED FAIR QUEUING (WFD)__ cada classe tem peso e recebe tempos diferentes de serviço 

Recebe porcentagem de tempo pela porcentagem de peso que ela tem, NO MÍNIMO

## ip

### Formato do datagrama 

- Version number
- Header lengh: pode mudar, então tem que especificar para saber onde começa data propriamente dita
- Tipo de serviço: Se é real time ou não
- tamanho total: data + header, limitando pelo frame do ethernet. 
- identificador de fragmentações de vários datagramas ip, quando é IPv4 e separado em vários pelo tamanho
- TEMPO DE VID - decai cada vez que processado pelo roteador. quando chega a 0 é dropado. para não ficar para sempre. 
- campo para protocolo da camada de transporte. 
- Checksum, que atua independente do checksum do tcp/udp
- Endereço IP de destino e origem. Origem pode ser chego pelo DNS
- Data(payload): segmento TCP/UDP ou outros

## IPv4 adressing

__INTERFACE__ : Ligação entre link e host/roteador. Roteador tem interface de saída e outra de entrada. Cada interface tem IP endereço, então roteador pode ter 2+ IP endereços. 

Cada interface deve ter seu IP único, que depende da subrede. 

223.1.1.0/24 indica que a máscara da subrede usa os 24 bits (3 primeiras """casas""" do endereço IP)

Essa subnet pode ser conectada a respectiva interface do roteador por segmento de Ethernet 

A subnet não precisa incluir apenas hosts, pode ser de interface de router com interface de router. Sempre isolar do respectivo roteador e ver a parte final em comum 

### Classless interdomain routing

forma: __a.b.c.d/x__ x representa o prefixo da rede. Todos dela têm em comum. Os restantes serve, para identificar unicamente o host ou até mesmo uma subrede. 

255.225.255.255 é usada para broadcast dentro da subrede 

### Como endereços são alocados

- Primeiro cada ISP tem sua própria subrede e aloca porcões __DENTRO__ dela para organizações e instituição ICANN aloca para administradores regionais que alocam para ISP

### Dynamic Host Configuration Protocol 

O adm da rede determina se um host ganha IP permamente ou temporário, de forma automática, quando se conecta à rede. 

Além disso manda máscara de subrede, o gateway default (primeiro roteador acima dele) e servidor DNS local. Tudo isso facilita o host!

Cada subnet pode ter seu DHCS server ou o roteador encaminha para ele 

### Processo de obtenção de IP pelo DHCS

Novo Host manda pacote UDP para camada de rede pela porta 67 e faz broadcast para 255.255.255.255 com source  0.0.0.0 

DCHS server então responde esse pedido com uma oferta de IP, com tempo de vida desse endereço e IP do servidor DHCS, também através de broacast 255.255.255.255

Cliente responde confirmando os parâmetros através de broadcast

DHCS confirma com ACK

Mas isso tem problemas de como manter uma conexão quando um celular se move entre subredes! (cenas para os próximos capítulos)

### Network Adress Translation

E se quisermos alocar enderçeços novos quando cresce minha pequena rede, ou mesmo gerenciar quais endereços há nela? Como ISP lida?

Usa-se um roteador NAT. Ele esconde uma subrede em que todos têm endereço 10.0.0.0/24 e se comporta com uma única saída e entrada para o mundo de fora. Quando um pacote sai ou é destinado a essa subrede, é para o IP do NAT na rede do ISP, daí ele direciona internamente. 

E como NAT router sabe para qual mandar? 

Ele dá uma porta para cada porta e IP interno, quando volta ele cruza esses com o destino do datagrama chegando e modifica esse datagrama pro host interno. 

## IPv6

Problema de poucos endereços IPv4 provocou mudança aproveitando para usar experiÊncia de melhorias no IPv4

### Vantagens

- Mais endereços
- Selecionar um individuo de um grupo 
- Header de 40 bytes obrigatório (mais rápido processar)
- Campo para flow
- Traffic Class
- Next header (header do segmento dentro)
- Hop limite de nós que pode passar

O IPv6 não permite mais fragmentação, agora apenas o endpoint pode fazer, pois processo era lento. Checksum a mesma coisa

### Transição 

A transmissão é por tunneling, encapsulado dentro de um IPv4, que o IPv6 retira essa capsula em algum momento. 

## General Forwarding

Match and action com tabela nos switchs de pacote

Usando OpenFlow, usando uma Flow Table. 

- Contém um set de headers para dar match 
- Um contador para atualizar numero de matches
- set de ações a serem tomadas

### Match 

Checa os valores em uma longa tabela com campos da camada de enlace, de rede e transporte. 

Como pode ter vários campos, eles podem ter prioridade e wildcards

### Ação 

Cada entrada na flow table entry tem ação associada 

- Forwarding : mandar para uma porta, dropar, broadcast, atualizar no controlador

- Modificar para mudar rumo. 

-  Ele verifica na tabela de match o pacote de chegada, vê se encaixa e toma a ação ligada 

- Grande maleabilidade 

#### Middleboxes

- equipamentos que fazem funções fora do normal de roteador entre destino e origem 

ex: NAT, Firewall, Load balancingy 

Também pode ser feito com software em equipamentos comuns (network function virtualizaton)

Funcionam como uma expansão do narrow waist da internet, que é o IP: único protocolo de rede em uma longa variedade de outros protolocos nas diferentes camadas


