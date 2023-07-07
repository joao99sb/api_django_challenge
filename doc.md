# Documentação da API

Esta é a documentação da API em Django. Aqui estão os detalhes sobre como usar a API e os endpoints disponíveis.

## Base URL

A URL base para todas as chamadas de API é: `https://api.django.seliga.shop/`

## Endpoints

### 1. Obter a lista de personagen

- **Endpoint**: `/character/<id>`
- **Método**: GET
- **Descrição**: Retorna uma lista de personagens disponíveis.
- **Parâmetros**:
  - `id` (opcional): Permite filtrar os resultados com base nos Ids passados e separados por &, caso não seja passado nenhum paramos, todos os personagens serão retornados.
- **Exemplo de Requisição**:

  - `https://api.django.seliga.shop/character/1319&339`

- **Exemplo de Resposta**:

```json
[
  {
    "_id": {
      "$oid": "64a70fae9235f321f02ca157"
    },
    "url": "https://anapioficeandfire.com/api/characters/1319",
    "name": "Nome do personagem 1",
    "gender": "Genero ",
    "culture": "cultura",
    "born": "detalhes do nascimento",
    "died": "detalhes do falecimento",
    "titles": ["lista de titulos"],
    "aliases": ["lista de apelidos"],
    "father": "pai",
    "mother": "mãe",
    "spouse": "https://anapioficeandfire.com/api/characters/1676",
    "allegiances": ["url com suas aliaças"],
    "povBooks": [
      {
        "id": 2,
        "name": "nome do livro que ele aparece"
      }
    ],
    "tvSeries": ["lista com as temporadas que ele participou"],
    "playedBy": ["ator"],
    "id": 1319
  },
  {
    "_id": {
      "$oid": "64a70fae9235f321f0223sdfs7"
    },
    "url": "https://anapioficeandfire.com/api/characters/1319",
    "name": "Nome do personagem 1",
    "gender": "Genero ",
    "culture": "cultura",
    "born": "detalhes do nascimento",
    "died": "detalhes do falecimento",
    "titles": ["lista de titulos"],
    "aliases": ["lista de apelidos"],
    "father": "pai",
    "mother": "mãe",
    "spouse": "https://anapioficeandfire.com/api/characters/1676",
    "allegiances": ["url com suas aliaças"],
    "povBooks": [
      {
        "id": 2,
        "name": "nome do livro que ele aparece"
      }
    ],
    "tvSeries": ["lista com as temporadas que ele participou"],
    "playedBy": ["ator"],
    "id": 339
  }
]
```

### 2. Obter a lista de livros relacionados a um personagem

- **Endpoint**: `/character/<id>/book/`
- **Método**: GET
- **Descrição**: Retorna os livros referentes ao personagem que teve o Id colocoado
- **Parâmetros**:
  - `id` (obrigatório): Permite filtrar os resultados com base no id passado.
- **Exemplo de Requisição**:

  - `https://api.django.seliga.shop/character/1319/book`

- **Exemplo de Resposta**:

```json
[
  {
    "_id": {
      "$oid": "64a70faf9235f321f02ca17d"
    },
    "url": "https://anapioficeandfire.com/api/books/8",
    "name": "Nome do livro",
    "isbn": "id da capa do livro",
    "authors": ["George R. R. Martin"],
    "numberOfPages": 1040,
    "publisher": "Bantam Books",
    "country": "United States",
    "mediaType": "Hardcover",
    "released": "2011-07-12T00:00:00",
    "povCharacters": [
      {
        "id": 148,
        "name": "Nome dos personagens principais"
      }
    ],
    "id": 8
  }
]
```

### 3. Obter uma lista de livros

- **Endpoint**: `/character/book/`
- **Método**: GET
- **Descrição**: Retorna uma lista de livros disponíveis.
- **Parâmetros**:
  - `id` (opcional): Permite filtrar os resultados com base nos Ids passados e separados por &, caso não seja passado nenhum paramos, todos os livros serão retornados.
- **Exemplo de Requisição**:

  - `https://api.django.seliga.shop/book/1&2`

- **Exemplo de Resposta**:

```json
[
   {
    "_id": {
      "$oid": "64a70faf9235f321f02ca17d"
    },
    "url": "https://anapioficeandfire.com/api/books/8",
    "name": "Nome do livro",
    "isbn": "id da capa do livro",
    "authors": ["George R. R. Martin"],
    "numberOfPages": 1040,
    "publisher": "Bantam Books",
    "country": "United States",
    "mediaType": "Hardcover",
    "released": "2011-07-12T00:00:00",
    "povCharacters": [
      {
        "id": 148,
        "name": "Nome dos personagens principais"
      }
    ],
    "id": 1
  }
  {
    "_id": {
      "$oid": "64a70faf9235f321f02ca17d"
    },
    "url": "https://anapioficeandfire.com/api/books/8",
    "name": "Nome do livro",
    "isbn": "id da capa do livro",
    "authors": ["George R. R. Martin"],
    "numberOfPages": 1040,
    "publisher": "Bantam Books",
    "country": "United States",
    "mediaType": "Hardcover",
    "released": "2011-07-12T00:00:00",
    "povCharacters": [
      {
        "id": 148,
        "name": "Nome dos personagens principais"
      }
    ],
    "id": 2
  }
]
```

### 4. Obter uma lista de capas

- **Endpoint**: `/character/book/cover`
- **Método**: GET
- **Descrição**: Retorna uma lista com todas as capas diponíveis.
- **Parâmetros**:
  - não possui parâmetros.
- **Exemplo de Requisição**:

  - `https://api.django.seliga.shop/book/cover`

- **Exemplo de Resposta**:

```json
[
  {
    "_id": {
      "$oid": "64a70faf9235f321f02ca180"
    },
    "id": 9780553103540,
    "bookId": "id do livro a que ele pertence",
    "content": "conteudo em base64 do binário da imagem"
  }
]
```

### 5. Obter uma lista de capas

- **Endpoint**: `/book/<id>/cover`
- **Método**: GET
- **Descrição**: Retorna a capa do livro.
- **Parâmetros**:
  - `id` (obrigatório): Permite filtrar os resultados com base nos id .
- **Exemplo de Requisição**:

  - `https://api.django.seliga.shop/book/2/cover`

- **Exemplo de Resposta**:

```json
{
  "_id": {
    "$oid": "64a70faf9235f321f02ca180"
  },
  "id": 9780553103540,
  "bookId": "id do livro a que ele pertence",
  "content": "conteudo em base64 do binário da imagem"
}
```
