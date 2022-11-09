# Subindo o kafka

```
docker-compose up -d
```

# Configurando o kafka

Após subir os containers com um broker e um zookeeper, vamos acessar o broker:

```
docker exec -it broker bash
```

Para listar os tópicos criados:

```
kafka-topics --list --bootstrap-server localhost:29092
```

# Criando um tópico

Para criar um tópico simples:

```
kafka-topics --create --bootstrap-server localhost:29092 --topic ola-mundo
```

Criando um tópico com 3 partições:

```
kafka-topics --bootstrap-server 127.0.0.1:9092 --topic novo_topico --create --partitions 3 --replication-factor 1
```

Alterando o número de partições:

```
kafka-topics --bootstrap-server 127.0.0.1:9092 --topic novotopico --alter --partitions 4
```

Deletando um tópico:

```
kafka-topics --bootstrap-server 127.0.0.1:9092 --topic novotopico --delete
```

# Criando um produtor

Criando um produtor:

```
kafka-console-producer --bootstrap-server 127.0.0.1:9092 --topic mensagens
```

**Obs.:** Se uma mensagem for enviada para um tópico que não existe, o kafka criará um tópico com o nome to tópico inexistente.

# Criando um consumidor

Criando um consumidor que irá ler todas as mensagens enviadas em um tópico

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --from-beginning
```

Criando um consumidor que irá ler as mensagens enviadas em um tópico a partir do momento que o consumidor foi criado

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens
```

Lendo mensagens de uma partição específica:

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partition 1
```

Lendo mensagens de uma partição específica e a partir de um offset:

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partition 1 --offset 2
```

Determinando um número máximo de mensagens lidas:

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --partition 2 --offset 1 --max-messages 1
```

## Grupo de consumidores

Quando criamos um grupo de consumidores, podemos criar n consumidores que farão parte deste grupo. No entanto, ao enviar uma mensagem para o tópico, somente um consumidor do crupo irá receber a mensagem. Essa é uma forma para escalar o processamento de mensagens.

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```

Podemos criar n grupos de consumidores para um tópico:

```
kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic mensagens --group consumidores
```

Listar grupo de consumidores:

```
kafka-consumer-groups --bootstrap-server localhost:9092 --list
```
