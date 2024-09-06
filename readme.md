# Projeto: Mural de Cantadas

## Visão Geral
- Mural de cantadas com sistema de ranking
- Usuários podem criar cantadas e interagir com as de outros
- Sistema de likes e dislikes
- Ranking das melhores até as piores cantadas
- Tabela com as 10 melhores cantadas e seus autores

## Tecnologia Recomendada
- JavaScript com Next.js

## Razões para escolha do Next.js
1. Interatividade em tempo real
2. Renderização do lado do servidor (SSR)
3. API routes integradas
4. Fácil integração com bancos de dados modernos
5. Componentes reutilizáveis para UI

## Estrutura Básica do Projeto

### 1. Configuração Inicial
- bash
- npx create-next-app@latest mural-de-cantadas
- cd mural-de-cantadas

### 2. Dependências Adicionais
- bash
- npm install @prisma/client bcryptjs jsonwebtoken
- npm install -D prisma

### 4. Modelos de Dados (schema.prisma)
- User
- Cantada
- Like

### 5. Componentes React
- Mural
- Formulário de cantadas
- Sistema de likes

### 6. API Routes
- CRUD de cantadas
- Interações (likes/dislikes)

### 7. Página de Ranking
- Top 10 cantadas

## Próximos Passos
1. Implementar autenticação de usuários
2. Criar páginas para exibir o mural
3. Desenvolver formulários para criar cantadas
4. Implementar sistema de likes/dislikes
5. Criar página de ranking
6. Testar e refinar a aplicação

