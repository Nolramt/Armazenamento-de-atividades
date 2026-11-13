# Armazenamento de Atividades

Aplicação web desenvolvida com **Python e Django** para organizar e armazenar atividades e trabalhos acadêmicos. O sistema permite organizar arquivos por período e matéria, facilitando o gerenciamento e o acesso aos documentos da faculdade.

## Sobre o projeto

O Armazenamento de Atividades surgiu com o objetivo de centralizar os arquivos acadêmicos em um único lugar, evitando que atividades e trabalhos fiquem dispersos em diferentes pastas do computador.

A aplicação utiliza uma estrutura hierárquica na qual os períodos contêm matérias, e cada matéria pode possuir atividades e trabalhos com seus respectivos arquivos anexados.

## Funcionalidades

- **Gerenciamento de períodos:** criação, edição, listagem e exclusão de períodos acadêmicos.
- **Gerenciamento de matérias:** organização das matérias dentro de cada período.
- **Gerenciamento de atividades:** cadastro, edição, exclusão e organização de atividades por matéria.
- **Gerenciamento de trabalhos:** cadastro, edição, exclusão e organização de trabalhos por matéria.
- **Upload de arquivos:** envio e armazenamento de arquivos associados às atividades e aos trabalhos.
- **Visualização de arquivos:** acesso aos documentos armazenados.
- **Validação de formulários:** verificação dos dados enviados pelos formulários.
- **Tratamento de erros:** página personalizada para situações como páginas não encontradas (erro 404).

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Django:** framework utilizado no desenvolvimento Back-End.
- **SQLite:** banco de dados utilizado para armazenar as informações.
- **HTML5:** estruturação das páginas.
- **CSS3:** estilização e organização visual da interface.
- **JavaScript:** implementação de funcionalidades no lado do cliente.

## Estrutura do projeto

```text
Armazenamento-de-atividades/
│
├── app/
│   ├── migrations/
│   ├── static/
│   │   └── app/
│   │       ├── css/
│   │       └── js/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/              # Criada durante a utilização
├── requirements.txt
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md
```

*Observação: a estrutura acima é resumida e apresenta apenas os principais diretórios e arquivos do projeto. A pasta `media/` não é versionada no Git.*

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Nolramt/Armazenamento-de-atividades.git
```

Entre na pasta do projeto:

```bash
cd Armazenamento-de-atividades
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows (PowerShell):

```powershell
.\venv\Scripts\Activate
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

Esse comando instala as bibliotecas e versões de dependências registradas no arquivo `requirements.txt`.

### 5. Aplicar as migrações

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver --insecure
```

Após iniciar o servidor, acesse:

```text
http://127.0.0.1:8000/
```

## Armazenamento de arquivos

Os arquivos enviados pela aplicação são armazenados localmente na pasta `media/`, configurada por meio das opções `MEDIA_ROOT` e `MEDIA_URL` do Django.

Essa pasta não é incluída no controle de versão do Git, pois contém documentos enviados durante a utilização do sistema.

Ao executar o projeto em outro computador, os arquivos anteriormente enviados não estarão disponíveis automaticamente. A pasta será criada conforme novos arquivos forem enviados.

## Banco de dados

O projeto utiliza SQLite para armazenar os registros da aplicação, incluindo períodos, matérias, atividades e trabalhos.

As migrações do Django são utilizadas para criar e atualizar a estrutura do banco de dados.

## Objetivo de aprendizagem

Este projeto também foi desenvolvido como parte do meu processo de aprendizagem em desenvolvimento Back-End, permitindo colocar em prática conhecimentos de:

- Desenvolvimento de aplicações com Django.
- Criação e relacionamento de modelos.
- Operações CRUD (Create, Read, Update e Delete).
- Utilização de formulários e validações.
- Manipulação e armazenamento de arquivos.
- Criação e organização de rotas e views.
- Integração entre Back-End e Front-End.
- Estilização de interfaces com CSS.
- Versionamento de código utilizando Git e GitHub.

## Autor

Desenvolvido como projeto pessoal de estudo, com foco no aprimoramento de conhecimentos em desenvolvimento Back-End utilizando Python e Django.