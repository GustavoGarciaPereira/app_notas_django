# Notes App - Sistema de Notas Compartilhadas

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Um aplicativo web para criar, gerenciar e compartilhar notas temporárias, desenvolvido com Django.

![Screenshot da Listagem de Notas](screenshot.png) <!-- Adicione uma imagem real posteriormente -->

## ✨ Funcionalidades

- **Autenticação de Usuários**
  - Registro e login seguro
  - Logout automático
- **Gestão de Notas**
  - Criar, editar e excluir notas
  - Visualizar histórico de atualizações
- **Compartilhamento Temporário**
  - Compartilhar notas com outros usuários
  - Definir tempo de expiração (1 hora, 1 dia, 1 semana)
  - Exclusão automática após expiração
- **Interface Intuitiva**
  - Listagem de notas pessoais e compartilhadas
  - Contagem regressiva para expiração
  - Busca por título ou conteúdo

## 🛠️ Tecnologias

- **Backend**
  - Django 4.2
  - SQLite (desenvolvimento)
  - PostgreSQL (recomendado para produção)
- **Frontend**
  - Bootstrap 5
  - HTML/CSS
  - JavaScript (contagem regressiva)
- **Outras Ferramentas**
  - Django Auth System
  - Cron Jobs (para exclusão automática)

## 🚀 Instalação

1. **Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/notes-app.git
cd notes-app
```

2. **Criar ambiente virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instalar dependências**
```bash
pip install -r requirements.txt
```

4. **Configurar banco de dados**
```bash
python manage.py migrate
```

5. **Criar superusuário**
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor**
```bash
python manage.py runserver
```

Acesse http://localhost:8000 e faça login!

## 📋 Como Usar

1. **Criar uma conta**
   - Acesse `/signup` para criar uma nova conta
   
2. **Criar notas**
   - Clique em "Nova Nota" no menu principal
   - Adicione título e conteúdo
   
3. **Compartilhar notas**
   - Na lista de notas, clique em "Compartilhar"
   - Selecione o usuário e tempo de expiração
   
4. **Visualizar notas compartilhadas**
   - Acesse a seção "Shared Notes" no menu
   - Veja o tempo restante para expiração

5. **Buscar notas**
   - Use o campo de busca para filtrar por título ou conteúdo

## ⚙️ Configuração Avançada

**Exclusão Automática de Notas Expiradas**
```bash
# Configurar cron job para executar a cada hora
0 * * * * /caminho/para/venv/python manage.py delete_expired_notes
```

**Variáveis de Ambiente**
Crie um arquivo `.env` na raiz:
```ini
DEBUG=False
SECRET_KEY=sua_chave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:
1. Faça um Fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

**Desenvolvido por [Gustavo Garcia Pereira]** - [🔗 LinkedIn](https://linkedin.com/in/gustavo-garcia-pereira-078240143) | [🐱 GitHub](https://github.com/GustavoGarciaPereira)
### Recursos Adicionais:
1. Adicione um arquivo `LICENSE` com a licença MIT
2. Crie um `requirements.txt` com:
```txt
Django==4.2.7
python-dotenv==1.0.0
```
3. Adicione screenshots reais do projeto na pasta `docs/`

Este README fornece:
- Visão geral do projeto
- Instruções claras de instalação
- Guia de uso detalhado
- Informações para contribuição
- Badges de status
- Seção de configuração avançada

