# LMQuestAI

LMQuestAI é uma API Flask que utiliza técnicas de Inteligência Artificial para responder perguntas com base em um documento de texto. O sistema usa TF-IDF e similaridade de cosseno para identificar e fornecer a resposta mais relevante a partir de um conjunto de sentenças.

## Funcionalidades

- Carrega um documento de texto (`internet.txt`) e divide o conteúdo em sentenças.
- Gera uma representação TF-IDF das sentenças.
- Calcula a similaridade de cosseno entre uma pergunta e as sentenças do documento para determinar a resposta mais relevante.

## Pré-requisitos

Para rodar este projeto localmente, você precisará ter:

- Python 3.x
- As seguintes bibliotecas Python:

  - `Flask`: para criar a API
  - `scikit-learn`: para o processamento de texto e cálculo de similaridade
  - `numpy`: para operações matemáticas
  - `re`: para manipulação de expressões regulares (integrada ao Python)

### Instalação de dependências

Use o `pip` para instalar as bibliotecas necessárias:

```bash
pip install Flask scikit-learn numpy
```

## Como executar o projeto

1. Clone este repositório.

2. Certifique-se de ter o arquivo `internet.txt` no diretório raiz do projeto. Este arquivo deve conter o texto que será analisado para responder às perguntas.

3. Execute o script `app.py`:

```bash
python app.py
```

4. A API estará disponível localmente em `http://127.0.0.1:5000`.

## Como usar

Para fazer uma pergunta à API, você deve enviar uma solicitação POST para o endpoint `/do_answer` com um corpo JSON contendo a pergunta. Exemplo:

### Exemplo de solicitação

```bash
curl -X POST http://127.0.0.1:5000/do_answer -H "Content-Type: application/json" -d '{"pergunta": "Qual é o propósito da internet?"}'
```

### Exemplo de resposta

```json
{
  "resposta": "A internet foi criada com o propósito de interligar redes."
}
```

Se a similaridade da pergunta com as sentenças não for suficientemente alta, a API retornará:

```json
{
  "resposta": "Desculpe, não consegui encontrar uma resposta adequada."
}
```

## Personalização

- **Arquivo de texto**: Para utilizar seu próprio documento, substitua o conteúdo do arquivo `internet.txt`.
- **Limite de similaridade**: O valor padrão de `threshold` é 0.2. Você pode ajustar esse valor na função `answer_question` para alterar a precisão das respostas.

## Estrutura do projeto

```bash
.
├── app.py               # Código principal da API
├── internet.txt         # Documento de texto utilizado para responder às perguntas
└── README.md            # Arquivo de documentação
```

## Tecnologias usadas

- Flask - para construção da API
- Scikit-learn - para a implementação do TF-IDF e cálculo da similaridade de cosseno
- NumPy - para operações matemáticas

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).