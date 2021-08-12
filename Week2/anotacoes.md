## UDP

<p> UDP faz checagem de erros usando checksum. 

Por exemplo, se temos tres mensagens de 16-bits, somamos todas, com excesso overflowado e dai tiramos o complemento dessa soma de tres. No recipiente somamos com o complemento e precisa ser 1111111111111111. Se tem 0 é erro.

Isso obedece principio de end-end. Só coloacar as funçoes no fim porque seria redundanete no meio (mesmo que provenha)

Importante notar que o UDP nao faz nada, no maximo avisa </p>

## Principios da transferencia segura

Sem dados corrompidos ou trocados ou perdidos.

Dificuldade:camadas anteriores podem nao ser confiaveis 

ARQ = Automatic Repeat reQuest -> manda OK quando certo, repete quando falsa


### Precisa 

1) Um campo para checksum 
2) Um valor de feedback (ACK/NAK)
3) Retransmissao

O remetente envia pacote e espera resposta sobre ser ACK ou NAK para tomar acao (reenviar ou esperar por mais da camada superior')

E se NAK ou ACK for corrompido no caminho?

Usar numero de sequencia, entao o NAK ou ACK especificará de qual pacote foi resposta.

