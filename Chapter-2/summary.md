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


