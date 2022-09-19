## PI: Sistemas Distribuidos

Esse é um sistema feito para a cadeira de PI: Sistemas Distribuídos do curso de <a href="https://unifapce.edu.br/cursos/sistemas-de-informacao/">Sistemas e Informação</a> e <a href="https://unifapce.edu.br/cursos/analise-e-desenvolvimento-de-sistemas/">Análise e Desenvolvimento de Sistemas</a> da <a href="https://unifapce.edu.br/">UNIFAP-CE</a>.

##### ToP - Treatments of Package

ToP é um projeto feito para auxiliar na entrega de pacotes para pequenas empresas, com a manipulação de dados, frotas e pedidos. ToP vai conseguir levar pequenas encomendas a grandes encomendas aos pequenos comerciantes de localidade pequenas tanto de capital, quanto de interior. 

<!-- COLOCAR O LINK DO GITHUB TEAM AQUI -->
<strong>Veja os membros da nossa <a href="https://github.com/orgs/ToP-Projeto-Integrador/people">equipe</a></strong>.

### Tecnologias

- [DOCKER](https://www.docker.com/)
- [PYTHON](https://www.python.org/)
- [DJANGO](https://www.djangoproject.com/)

<!-- COMPLETAR RESPONSAVEL PELO FRONT
- [BOOTSTRAP](https://getbootstrap.com/) 

-->

<!-- COMPLETAR RESPONSAVEL PELO BANCO
- [comment]: <> ([BANCO](https://www.postgresql.org/)

-->

<strong>A base para a contrução do sistema é o docker com o intuito de agilizar e ter todos os desenvolvedores na mesma versão de todas as dependecncias, evitando assim bugs e erros.</strong>

### Separando as coisas

Vamos utilizar o modulo de ambiente virtual do python para separar as libs do sistema de outras libs que você utiliza normalmente no seu computador, para isso:

Utilize os comandos abaixo:
- ```pip install virtualenv```


Criar um virtualenv chamado venv.
- ```python3 -m venv venv``` 

Ao utilizar o virtualenv vc separa os ambientes, a ideia é que cada membro da equipe crie o seu proprio venv para o desenvolvimento.

### Trabalhando com docker

O docker vai separar na sua maquina um ambiente virtual somente com o minimo necessario para rodar o projeto, alem de deixar todos os desenvolvedores na mesma versão.

Ele foi criado para descomplicar, não deixar as coisas mais dificeis, ao montar o docker-file e o docker-compose deixei tudo preparado para que não de nenhum trabalho na instalação e que você consiga iniciar o ambiente da maneira mais rapida e pratica possivel.


Baixando dependencias do docker:
- ```docker-compose build```

Iniciando o container:
- ```docker-compose up```

O projeto django já esta aberto na sua maquina <a href="0.0.0.0:80" target="_blank">clique aqui</a>, bem facil né?
