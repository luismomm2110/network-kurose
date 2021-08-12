# Network Layer: Control Plane 

- Destination forwarding é ligação entre controle e data 
	- tabelas na data
	- algoritmos no controle

Pode ser por roteador, com algoritmos ou por centralizador 

Por centralizador ele fica responsável por tudo, roteador só se comunica. Cada vez mais frequente

## Algoritmos 

Normalmente usa menor custo, mas problemas comerciais, por exemplo, entram em jogo 

Representada por um edge, que tem seu custo envolvido. 

Esse custo pode ser distância, pecuniário ou velocidade

O custo pode ser calculado centralizado, com informação sobre toda a rede, inclusive no CDN ou router. Chamado de Link state.

Ou iterativamente, com distance vector atualizado por cada roteador 

Também pode ser estático, que é de pouco em pouco, ou pode ser dinamico, em tempo real mas mais suscetível a erro 

Também pode ter custo associado ao tráfico ou não (hoje em dia maioria não é)

### Link State 

Nesse caso, roteadores têm conhecimento completo da rede. Isso é alcançado por broadcast. 

Depois da kth iteração, os caminhos de menores custos são conhecidos para k nós de destinos e esses k paths terão os k menores custos. 

D(v): cysto do least-cost da fonte para destino v nessa iteração do algoritmo 

p(v): última no antes de v no caminho mais barato da fonte para v 

N': subset de nós. v tá em N' se o menor custo da fonte para v é conhecido.

Começa por inicialização e loops para todos os nós da rede. No fim calcula todos menores caminhos. 

Ele começa pela origem rs no set N'

calcula custos para todos vizinhos

daí vai para o menor caminho da origem e adiciona em N' 

calcula de novos os custos para novos vizinhos (incluindo já em N') e adiciona na tabela, adicionanbdo custo e trocando se houver e foi necessário

vai sucessivamente até N=N'

Complexidade O(n**2)

### Patologia

Quando link load é diferente em sentidos opostos. 

Vai contranbalançeando de um lado pro outro. A solução é calcular em momentos opostos e saber aonde o outro mandou. 

## Distance Vector Routing Algo 

- Distribuido: recebe informação dos nós diretamente ligados, calcula e distribui 
- Iterativo: até não receber mais informação dos outros
- Assíncrono: pode ir por conta própria

dx(Y) é o custo do caminho mais barato entre x e y 

dx(y) = min v {c(x, v) + dv(y)}

Então o custo menor de x para y é o minimo entre a soma c(x, v) e dv(y) entre todos vizinhos de v

Dá as informações para a tabela de encaminhamento 

Como: por exemplo, v* é o nó minimo? então ele estará na tabela de ancaminhamento x quando precisar mandar para mínimo 

X mantém uma tabela Dx com custo para todos vizinhos 

X mantém informação c(x,v) para vizinho direto v 
Dx com estimativas de custos
Dv distancia dos vizinhos para y 

De tempo em tempo, eles mandam seus vetores de distancia para seus vizinhos. Se mudar o vetor Dx com isso, pela equação de bellman-ford, X também atualiza seus vizinhos. No longo prazo converge para o tamanho dx(y) real

dx muda quando custa para vizinhos diretos muda ou vizinhos atualizam suas tabelas. 

Existem linhas para cada nó e eles vão atualizando conforme recebem informações, vendo se não há caminho mais baratos que os que ele já possui 

Às vezes pode entrar em loop até chegar no valor real pois vai atualizando de iteração em iteração, o que é lento

#### Solução Poisoned Reverse

Z diz que custo de z -> x é infinito para y, então y não vai usar z

Algoritmos são completementares em velocidade, robustez e complexidade

## Intra-AS routing in the internt

Routers não são homogêneos. A presença de roteadores maiores reduz o tamanho e complexidade da rede

E também alguns possuem autonomia administrativa

Isso forma __Autonomous Systems__  na rede

Cada Router em uma AS roda o mesmo procologo e têm informações sobre outros. 

Cada AS tem seu próprio ASN, pode ser quebrado conforme ISP decide 

### Open Shortest Path First 

Open de open source 

Link state protocol que flooda o sistema e roda Dijstrak menor custo 

Cada roteador faz mapa do sistema e Djistrak shortest path algo para todas subnetes, com ele como root

Os custos de cada link são decididos pelo administrador da rede (por exemplo por trafégo ou para assumir que o LS algo faz o caminho que ele desejar)

As atualizações são para todos roteadores, a cada mudança no sistema e também de forma periódica

- OSPF usa autentição para garantir que pacotes intrusos não interfiram na configuração da rede
- Suporta unicast ou multicast
- Permite que multiplos caminhos sejam usados
- permite hierarquia, com sub AS rodando dentro da AS geral 

## Border Gateway Procotol (BGP)

AS precisam se comunicar entre si, por isso existe um protocolo para se comunicar entre elas 

Roteador tem um número CIDR para destino de forma (x, l), x sendo o prefixo CIDR para a subrede e l o número de interface de um roteador dessa subrede de destino

BGP fornece: 

- 1) meio de um roteador conhecer todas as subredes existentes.  
- 2) Determinar melhor rota para os prefixos

### Como fornece serviços:

Um roteador pode ser interno ou gateway (se comunica com outra AS) 

O prefixo para ser alcançado manda uma mensagem para a subrede mais próxima. Essa manda para as outras até chegarem em todas 

Mas quem manda são roteadores!! Como? Por conexões TCP através da porta 179 (mensagens BGP), dividas em interna e externa 

Lembrar que não é igual conexão física (p ex. posso ter apenas ligação física entre A-B-C nessa ordem, mas existe iBGP entre A e C porque elas se ligam fisicamente através de B)

### Determinando melhores caminhos 

Normalmente há muitos caminhos até cada roteador

#### ATRIBUTOS 

__ROTA__ = prefixos + atributos 

- AS-PATH: vai inidicando por quais AS passa, inclusive vendo loop caso passe por ela mesmo e dai impede essa Rota 
- NEXT-HOP: endereço IP da interface do roteador que começa o AS-PATH, ou seja, a interface do roteador da AS mais perto 

Por tanto BGP é prescrito por NEXT-HOP;AS-PATH;destination prefix 

### HOT POTATO ROUTING 

Acha o custo DENTRO da AS para o prefixo destinado para sair logo dela e o custo ser de outra AS (coloca na sua tabela de forward para o Next Hop quando destino for x). Por isso pode mudar de roteador para roteador dentro da mesma AS. 

### Route-selection 

Usado na prática. Se há mais de um caminho: 

1) Na rota possui uma __preferêncial local__ com decisão pelo administrador AS. Selecionados os com maiores valores.

2) Desses escolhe com menor número de AS no caminho. 

3) Dentre essas, escolhe com menor custo dentro da AS (hot potato)

### IP-ANYCAST

Também usado para distribuir caches, por exemplo para CND ou DNS, para locais mais próximos do cliente

O servidor tem mesmo endereço IP e adverte para rede toda. Os roteadores entendem que é o mesmo endereço, mas escolhe o mais próximo (por menor número de AS no caminho)

### Routing Policy

Para evitar redundadância, a política de AS pode ser implementada de forma que nunca passa por uma AS desnecessária, atribuindo ponto para ela

Além disso provedores também pode não querer serem usados como intermediários, por isso exigem que apenas seus cosnumidores e destinos passem por ele 

### Obtendo presença na internet 

Através do BGP para as diversas ISPs

## SDN control plane 

Como funciona o packet switch na forwarding table?

- Flow based: Pode ser em qualquer header (transporte, rede, enlace), não só IP
- Separacao do plano de controle e data: server e software controlam switches flow tables, não apenas hardaware 
- Monitoramento constante 
- Configurável por programação para load balance por exemplo 

### Divisão por controlador e aplicações de controle de rede 

#### Controlador 

Layers: 
- Southbound interface para se comunicar com os dispositivos controlados, para ver se liunk caiu, se é operacional. Controlado por OpenFlow protocol 
- Camada de gerenciamento da rede com informações sobre as tabelas de estado do switch 
- Northbound API Rest para comunicar com as apçlicaoes que calculam as rotas 

Esse serviço é distribuído, pois vários componentes e servidores oferecem esse serviço de comunicação registro e aplicação 

### OpenFlow Protocol 

Opera entre dispositivos e SDN controlador por conexao TCP porta 6653

- Configuration: get e set configuração de um switch 
- Modifiy-state: muda flow table e seta propriedades do switch 
- Read-state: estaticas do switch 
- send-packet: manda um pacote por uma porta escolhida pelo controlador 

Do controlado pro controlador: 

- Flow-removed: alguma entrada na flow table foi removida por timeout ou ordem de um controlador 
- Port status 
- Packet in : manda mensagem escolhida para processamento posterior no controlador 

### Dijstrka com SDN

O algoritmo é rodado separado 
Os updates são mandados para o SDN 

Switch se comunica com port-status para OpenFlow quando há mudança 
O controlador de SDN recebe mensagem OpenFlow e notifica o gerenciador do estado de links, que atualiza a database de link
A notificação é mandada para a aplicação de de controle de rede 
Essa aplicação se comunica com o gerenciador de estado de link para calcular novos menores custos 
Daí manda para gerenciador de flow tables, que manda para switches 

## ICMP Internet control message protocol 

Comunicação de mensagens do host e routers 

Vai dentro de uma mensagem IP, asssim como TCP e UDP

Contém o header do datagrama que causou o erro e código de mensagem 

Ex: Ping 

## Gerenciamnto de REDE 

### Framework 

Servidor de genreciamento - servidor principal centro de operacoes da rede (NOC) 

Dispositivo gerenciado - qualquer peça com seus parametros de configurações 

Data - configuração, operacional (dos viozinhos, por exemplo, que ele adquire enquanto importa) e estatisicas. Gerenciador tem cópia de tudo isso. 

Agente do gerencidador - software que se comunica com o gerenciador a partir do dispositivo 

Protocolo - determina capacidades para o gerenciador (monitorar, testar, analisar etc)

Comando via CLI ou HTTP

Management information Base e Simple Network Management Procotol são usados para determinar e questionar dados e serem controlados por CLI

NETCONF/yang - YANG é modelo de dado para visão holística e NETCONF usa Yang para gerenciar rede 

### SMTP 

Usado para o gerenciador de rede pegar informações MIB ou o dispositivo enviar trap message (nao solicitada pelo gerenciador, quando há alguma mudança)

SNMP tem vários tipos de mensagens __PDU__ para comunicão

### MIB

Módulos que contém informações como quantos datagramas foram descartados, software DNS etc

### NETCONF e YANG

Pega, seta e recebe notifações dos dispositivos da rede usando remote procedure call para configurar arquivos XML

### Yang 

Define como as mensagens NETCONF são configuradas 



