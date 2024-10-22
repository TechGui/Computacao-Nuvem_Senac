## Descrição

### O que foi feito?

- Criação de um projeto Flask
- Renderização de frases motivacionais aleatórias ao acessar a rota principal
- Rodar a aplicação em um container Docker

## Etapas:

#### 1. Configuração Inicial

Foi criado o diretório do projeto e criado uma aplicação web básica utilizando Flask.
<img width="1080" alt="etapa1" src="/flask_motivacao_app/source/etapa1.png">

#### 2. Criação do Dockerfile

Foi criado um arquivo Dockerfile para configurar a imagem do container, com dependências necessárias e a configuração das portas a serem utilizadas.
<img width="1080" alt="etapa2" src="/flask_motivacao_app/source/etapa2.png">

Aqui está o comando para criar a imagem após a criação do Dockerfile
<img width="1080" alt="etapa2" src="/flask_motivacao_app/source/etapa2.1.png">

E aqui está o comando para rodar o container
<img width="1080" alt="etapa2" src="/flask_motivacao_app/source/etapa2.2.png">

#### 3. Teste da aplicação

A aplicação foi testada acessando a rota principal do projeto, que renderiza frases motivacionais aleatórias. Fiz alguns testes para mostrar que está 100% funcional e estou cada vez melhor na gestão do tempo necessário para criar containers Docker. Aqui estão alguns exemplos, onde a frase e a cor muda ao reiniciar a página do navegador, pois está acessando a rota principal, a que renderiza as frases.
<img width="1080" alt="etapa3" src="/flask_motivacao_app/source/etapa3.png">

<img width="1080" alt="etapa3" src="/flask_motivacao_app/source/etapa3.1.png">

<img width="1080" alt="etapa3" src="/flask_motivacao_app/source/etapa3.2.png">

<img width="1080" alt="etapa3" src="/flask_motivacao_app/source/etapa3.3.png">
