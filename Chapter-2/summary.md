# Camada de Transporte

<p> Fica em cima da camada de aplicação, então essa depende da de rede. Tem um internet protocol (IP) que faz melhor esforço para entregar.
Mas não garante entrega, ordem e integridade. Cada host tem um endereço de Ip </p>

<p> Função da camada de transporte é extender a camada de red (onde fica IP) e fazer comunicação entre processos que rodam em sistemas (sistema é pelo IP). UDP e TCP garantem a integridade dos dados </p> 

<p> TCP garante que os dados vão chegar e e em ordem através de técnicas. Além disso, para bem comum, faz serviço de congestão </p> 

## Multiplexacao e Demultiplexacao: Extensao do serviço de rede para entrega processo processo 

<p> Quando chega data da rede, a camada de transporte precisa saber para qual processo irá enviar. Para isso usa os socket, que fazem parte da aplicação e recebem a data.
O segmento da camada de transporte tem um identifacor para qual socket enviar. __Isso é demultiplexacao.__ </p> 

<br> </br>

<p> Quando sai da cmada de transporte ela coloca header para depois serem identificados. _Isso é multiplexação_  </p> 

<p> Analogia para colhedor de cartas. Chega múltiplas, entrego para um. Demultiplica. 

Junta para enviar manda todas. Multiplica. </p>

<p> Então segmentos precisam de um header com identificador de qual socket se direcionam. </p>

<br> </br>

<p> Isso é feita pela porta de saída e destino, que identificam o socket. Um número de 16 bits. e 2^10 são nuneros restritos. UDP examina esses para enviar para um socket</p>

<p> Quando a aplicação cria o socket, usa uma parta ainda não assinalada. O cliente tem porta associada automaticamente, o servidor não </p>

<p> Então funciona de forma lógica. processo A associa as portas em um segmento para procesos B, com data da cmamada de aplicação. Passa esse segmento para camada de rede que faz melhor esforço para entregar. Quando chega no Host B ele pega para a porta associada e demultiplexa para o processo B </p>

<p> UDP socket é identificado pelo IP e porta do destino. Então se tiver origens diferentes ele usará o mesmo socket como destino </p> 

<p> Daí quando envia de volta, a porta de origem como destino. O UDP usa o _recv_ para isso, nao armazena na tupla </p> 

<p> O TCP usa uma tupla com 4 valores para identificar: Destinos e origens.  
Entãp TCP faz da seguinte maneira. Tem um socket de entrada onde todos chegam. A paretrir disso o host cria um novo socket com a conexão. Assim, cria um socket com valores de destino e entrada, após a mensagem de boa vinda no socket de entrada. </p> 

<p> Esses campos são usados para multiplexaçã/demultiplexação. O servidor pode ter várias conexões </p>

<p> Interessante notar que reptições de valores individuais são permitidos, mas de tupla não </p> 

<p> Quando usa WEB, por exemplo, tanta as boas vindas quanto a saída usam a porta 80. Mas também pode criar novas threads dentro de um processo com várias conexões nele. Essas conexões podem ser persistentes ou não </p>

## UDP

<p> ele permite que checagem de erro e demux/mux função. 


# INSERIR PARTE REMOTA CASA

## Pipeline

<p> Wait and send é muito lento. Protocolos reais usam pipeline para preencher. Vai precisar de buffering e de maior sequencia. 

## GO-BACK-N 

Tem numero de base que avança conforme pacotes sao reconhecidos. Tem um limite N a partir da base para mandar pacoters nao reconhecidos. Senao manda tudo de novo. 

Pacote n de sequencia [0, 2^k-1] 


## Selective repeat

GBN tem um problema quando a janela é grande, um único erro pode causar engarrafamento. 

SR mantem o ACK dos enviados fora da ordem. O receptor então precisa manter buffered pacotes da sequencia fora da ordem. Daí quando recebe a base manda tudo de uma vez para camada superior. 

Cada pacote tem seu prório timeout para nao manter nao precisar manndar todos, apenas os nao reconhecidos. 

Há um problema para repetição quando o pode concidir numero de sequencia 


# TCP

TCP faz conexão, que intermediários nao veem. Só pode fazer um para um 

Primeiro precisa de um handshake! 

O cliente manda um segmento, servidor responde e clente termina as boas-vindas.

O cliente utiliza um buffer para enviar através do TCP data para o servidor. Utiliza o maior tamanho que o link no meio do caminho pode mandar (sem incluir o cabeçalho)

O servidor também armazena num buffer para passar à camada de aplicação através do socket. 

## Estrutura do segmento TCP

- Porta do destino e receptor

- Checksum field

- 32 bit campo para sequencia e ACK 

- 16 bit para janela de controle de flow

- 4 bit indicar tamanho do header (que tem 32 bits)

- Um campo para opções 

- Uma para flags como ACK, __PSH__ (enviar data imediatamente para a camada de aplicação), __URG__ 

- Por fim, claro, a data

## Sequencia

A sequencia está, para o Stream, nos bytes, não nos segmentos. Então o numero de sequencia para um segmento é o numero do 1o byte dele. A partir disso coloca a sequencia. 

## ACK

O numero do ACK é o próximo da sequencia esperada de vinda do outro 

Se recebe fora de ordem, normalmente armazena. 

Os números nao começam em zero, mas aleatórios. 

## Telnet 

Usado para login, mas nao encripta. 

O usuário digita algo, vai para servidor e depois vai volta para cliente. 

Se vai junto com data, ACK é piggyback

### RTT

Calculado quando sai segmento e quando é recebido ACK para esse. Ele só mantem um SampleRTT de cada vez, para determinar Timeout. 

O valor estimado e calculado junto com com o novo valor, qeue tem mais peso. A variância também 

TimeoutInterval = EstimatedRTT + 4 * DevRTT  para o valor do timeout 

O uso de sequuencial pode evitar pacotes repetidos. Por exemplo, se eu recebi o ACK do pacote posterior, nao preciso mandar o anterior mesmo sem ACK. 

### Doubling time interval

Quando ocorre um timeout, o tempo de timeout é dobrado, pois, como provavelmente foi gerado por congestão, tem que evitar piorar isso. Mas a patir que recebe ACK volta à fórmula anterior. 

Quando recebe fora de ordem, receptor manda dois ACK para indicar isso. 

Se recebe tres duplicados, manda antes do timeout, pois provavelmente esse segmento ACKado foi perdido.

## Flow Control 

Receptor tem buffer, mas é necessário cuidado para enviar data sem transbordá-lo, pois depende da velocidade que camada superior consome dados desse buffer. 

Cada parte da conexão TCP tem bit para window, para dizer se está com buffer cheio ou não. 

Mantém LastByteRead do buffer e LastByteRcvd do emissor. 

A diferença entre os dois deve ser menos que o Buffer

O receiver windows variable indica qual tamanho dispon´vel 

Quando o rnwd é 0, A continua mandando 1 byte para saber se já liberou espaço 

### Connection Management 

1 - cliente mandando um segmento com flag SYN para iniciar conexão  e um numero aleatório para começar sequencia

2 - SYNACK segment: servidor manda SYN de volta, aloca buffer e sua própria variável de sequência, além do ACK com o posterior do numerro de sequencia do cliente

3 - cliente aloca suas variáveis e buffers, além de mandar numero de seq + 1 para servidor. Pode enviar data dessa vez. SYN é setado para zero (conexão estabelecida)

4 - A conexão é encerrada com flag FIN do cliente. Daí o servidor manda ack. Após um tempo manda seu FIN e cliente manda ACK. depois de um tempo, temos o lindo fim para a conexão 

Quando o TCP cliente manda para uma porta nao aberta, o servidor indica isso. 

## Controle de Congestão 

Normalmente por overflow do buffer

### Causa e custos da congestão 

#### Cenário 1:

A e B tem hop entre eles.

Aplicacao em A manda para camada de transporte via socket LAMBDA bytes/sec e o mesmo para o roteador. B faz o mesmo. 
Ambos mandam por um link de capacidade R. O Roteador tem buffer infinito. 

Por dividir o link, eles nunca vão conseguir mandar a uma rate maior que R/2 o link,

Daí, porque o host A manda mais rápido que a capacidade dele para o link, acaba lotando o buffer e o delay se torna infimito.

#### Cenário 2

Agora o roteador tem buffer finito (o que implica que pacote cai quando ele lota) e a conexão é confiável, como TCP.

Como é confiável, tem duas rateS: Lambda é _sending rate_ e depois da retransmissão por timeout, LAMBDA' é _offered rate_

1) Assumindo que A não sabe quando buffer lota, lambda nunca passa de R/2 para não haver timeout. Tudo é recebido 

2) Assumindo que TEM CERTEZA que terá timeout para retransmitir. LAMBDA' = R/2  Recebida pela aplicacao em B é R/3 entao o buffer cheio faz parte da transmissão ser retransmission

3) Se acontecer timeout antes do ACK voltar, ele vai mandar mesmo sem precisar. Entao vai ter transmissão original, retransmissão necessária, retransmissão desnecessária
velocidade da aplicação vai pra R/4

#### Cenario 3

Todos com conexão confiável mesmo LAMBDA in e todos roteadores com capacidadde R

A -> R1 -> R2 -> C
D -> R4 -> R1 -> B

Para valores pequenos de output, nao sobrecarrega o buffer. Aumento de LAMBDA in aumenta de LAMBDA out

Agora considere o caso que Lambda In e LAMNDA' in é bastante grande. 

A chegada em R2 é no máximo R, a transmissao entre R1 e R2. Mas B-D usa R2 diretamente, se ele mandar mto, A-C não vai ter espaço em R2. Lambda out vai para zero

Isso significa que o trabalho de R1 PARA R2 foi desperdiçado 

## Maneiras de controle de congestão 

Controle por end-to-end: TCP sem apoio do IP. Com timeout ou recepção de tres ACK

Com assitencia da rede indicando tráfego para um link ou congestao. Pode mandar um pacote ou mais tipicamente colocando um campo no segmento para o recpetor perceber
a congestão e mandar pro enviante 

## TCP controle de congestão 

### Classico 

Limitar ou aumentar conforme tráfego na rede 

Como limita? 

_LastByteSent - LastByteACK <= min(cwd, rwnmd)_ __congestion and receive window__

Primeiro imagine que rwnd é infinito, buffer infitino de recepção, sem perda de pacote... então só cwnd faz diferença 

Vamos imaginar um envio: ele está no LastByteAck 2... se cwd é 5, ele só pode mandar 3 ... ele manda 3, recebe 3 ack no fim em RTT segundos, logo a velocidade dele 
é __cwnd/RTT__

Como TCP percebe a perda de pacote: timeout ou 3 ACK... isso ocorre, por exemplo, quando há overflow em algum buffer do roteador

TCP usa então um relógio para perceber se o tempo entre ACK é lento, isso determina o cwdn 

Então como determinar? as questões principais são: nao pode sobrecarregar nem subutilizar. 

	- uma maneira de detectar é com segmento perdido como nas partes acima. timeout ou 4 ack. Dái ele ajuda a janela de congestão e portanto a taxa

	- quando recebe, indica que tá tudo bem. CWND pode aumentar 

	- Estratégia do TCP: aumenta a cada ACK mas quando tem um drop ele volta pra velocidade inicial 

#### Mecanismos 

1) Slow start: Começa com 1 MSS (__maximo segumento suportado pélo sender__), então a taxa inicial é MSS/RTT; Cada ACK recebido aumenta em um MSS a mais no CWND, 
então cresce exponencialmente. Acava quando tem uma perda (timeout ou 3 ACK) daí seta cwnd para 1 para recomeçar slow star. E seta nova variável (ssthresh slow start threshold) que chega é metade da cwnd quando teve congestão. depois do timeout, quando cwnd alcanda ssthresh começa modo de congestão e aceleração é menor. 

2) Congestion avoidance: quando está nesse modo, aumenta apenas 1 MSS por RTT. E quando acaba? Cwnd começar sempre em 1 MSS e o valor de sshresth também é metade do cwnd. Quanmdo há tres ACK duplicados TCP faz cwnd pela metade e sshtresh pela metade do cwnd quando teve tres ACK. Entra em fast recovery. 

3) Fast recovery: valor do CWND é incrementado em 1 MMS para cada ACK duplicado do segmento que causou o TCP entrar em fast recovery. Se ocorre timeout, volta para Slow Start. 

Isso mostra como TCP vai testando a banda. Primeiro cresce até ser limitada por ela e retorna crescimento e assim por diante. 

#### TCP Cubic

Esse algoritmo anterior pode ser mto conservador. Por isso, TCP Cubic usa Congestion avoidance diferente

 - Wmax indica tamanho da janela de congestão quando teve perda, K éo  tempo que irá alcançar 

 - A janela de congestão cresce ao cubo da distância entre tempo atual e K. Ou seja cresce rápido longe e lento perto

 ### Análise 

 A velocidade varia de W/RTT (alcance máximo) para W/2*RTT quando tem timneout 

 velocidade média então é 0.75W/RTT

 ## Congestão com auxílio da Rede e baseada em Delay

 ### ECN : Explicit congestion notification

 Usa dois bits no datagrama
  - Um para indicar que tem congestão, daí o receptor envia ao emitente (por isso precisa ser antes do timeout)
  - outro para indicar que essa conexão permite ECN

 O ACK do receptor manda esse arquivo de congestão, o que permite o rementente simular um timeout e cortar cwnd no meio 

 ### Delay based congestion control 

 O ideal é ocorrer antes do timeout para não haver perda de pacote no buffer (desperdíco)

 TCL Vegas usa vendo o RTT do maus rápido pacote. Se há outro com velocidade mto menor que a dessa ele já percebe o delay 

 ## Fairness

 Uma conexão é fair quando velocidade de cada conexão é R/K sendo R a taxa de transmissão do bottleneck e K n de conexões
 
   


