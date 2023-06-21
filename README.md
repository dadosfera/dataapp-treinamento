Este é um projeto de Demonstração de Fluxo de Caixa que utiliza Docker e um arquivo .env para gerenciar variáveis de ambiente.

## Pré-requisitos

Antes de executar este projeto, você precisará ter os seguintes softwares instalados em sua máquina:

- Docker
- docker-compose

## Configuração do arquivo .env

Para configurar o arquivo .env, siga os seguintes passos:

1. Crie uma cópia do arquivo .env.example e renomeie-a para .env.

2. Abra o arquivo .env em um editor de texto e preencha os valores das variáveis de ambiente de acordo com a sua configuração. Certifique-se de que todas as variáveis estejam preenchidas corretamente.

## Executando o projeto

Para executar o projeto, siga os seguintes passos:

1. Abra o terminal na pasta raiz do projeto.

2. Execute o seguinte comando para construir as imagens Docker:

```
docker-compose up
```
4. O projeto estará disponível em http://localhost:8051.

## Encerrando o projeto

Para encerrar o projeto, pressione CTRL+C no terminal para parar os containers. Em seguida, execute o seguinte comando para remover os containers:

```
docker-compose down
```

## Considerações finais

Certifique-se de que todos os pré-requisitos foram instalados corretamente antes de executar o projeto. Em caso de dúvidas ou problemas, consulte a documentação oficial do Docker e do docker-compose.