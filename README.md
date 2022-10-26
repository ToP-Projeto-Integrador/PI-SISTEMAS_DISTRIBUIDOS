## PI: Sistemas Distribuidos

Esse é um sistema feito para a cadeira de PI: Sistemas Distribuídos do curso de <a href="https://unifapce.edu.br/cursos/sistemas-de-informacao/">Sistemas e Informação</a> e <a href="https://unifapce.edu.br/cursos/analise-e-desenvolvimento-de-sistemas/">Análise e Desenvolvimento de Sistemas</a> da <a href="https://unifapce.edu.br/">UNIFAP-CE</a>.

#### ToP - Treatments of Package

ToP é um projeto feito para auxiliar na organização de estoques de pequenas empresas, em localidades diversas. Muitos negócios se encontram em bagunça, falta de organização, pois ainda trabalham com papel e documentação física, fazendo com que muitos problemas apareçam. Com um sistema acessível para todos os empresários e donos de pequenos negócios, a ToP vem para ajudar a organizar e levar seu negócio ao futuro 🚀.

<strong>Veja os membros da nossa <a href="https://github.com/orgs/ToP-Projeto-Integrador/people">equipe</a></strong>.

### Tecnologias

- [DOCKER](https://www.docker.com/)
- [PYTHON](https://www.python.org/)
- [DJANGO](https://www.djangoproject.com/)

<!-- COMPLETAR RESPONSAVEL PELO FRONT
- [BOOTSTRAP](https://getbootstrap.com/) 

-->

<!-- COMPLETAR RESPONSAVEL PELO BANCO
- [BANCO](https://www.postgresql.org/)

-->

<strong>A base para a construção do sistema é o docker com o intuito de agilizar e ter todos os desenvolvedores na mesma versão de todas as dependências, evitando assim bugs e erros.</strong>

### Instalação

Para começar certifique-se de ter todas as dependências do projeto instaladas. A baixo os links de programas que você vai precisar:

- [DOCKER ENGINE](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- [DOCKER DESKTOP](https://docs.docker.com/desktop/install/ubuntu/#install-docker-desktop)
- [PYTHON](https://www.python.org/downloads/)


### Separando as coisas

Vamos utilizar o modulo de ambiente virtual do python para separar as libs do sistema de outras libs que você utiliza normalmente no seu computador, para isso:

Utilize os comandos abaixo:
- ```pip install virtualenv```


Criar um virtualenv chamado venv.
- ```python3 -m venv venv``` 

Ao utilizar o virtualenv você separa os ambientes, a ideia é que cada membro da equipe crie o seu proprio venv para o desenvolvimento.

### Trabalhando com docker

O docker vai separar na sua maquina um ambiente virtual somente com o mínimo necessário para rodar o projeto, além de deixar todos os desenvolvedores na mesma versão.

Ele foi criado para descomplicar, não deixar as coisas mais dificeis, ao montar o docker-file e o docker-compose deixei tudo preparado para que não de nenhum trabalho na instalação e que você consiga iniciar o ambiente da maneira mais rápida e prática possível.


Baixando dependências do docker:
- ```docker-compose build```

Iniciando o container:
- ```docker-compose up```

O projeto django já está aberto na sua máquina, bem fácil né?
