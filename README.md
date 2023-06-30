# PraticalLLMs

# Qual tarefa é usada por este modelo?
## **Processamento de linguagem natural**
**API_URL2**
***Modelo recomendado : bert-base-uncased (é um modelo simples, mas divertido de usar).***
Tarefa de máscara de preenchimento - Tenta preencher um buraco com uma palavra que falta (token para ser preciso). Essa é a tarefa básica dos modelos BERT. 
Valores retornados
seqüência | A sequência real de tokens executados no modelo (pode conter tokens especiais)
score | A probabilidade para este token.
símbolo | O id do token
token_str | A representação de string do token.

**API_URL3**
***Modelo recomendado : facebook/bart-large-cnn .***
Tarefa de resumo
Essa tarefa é conhecida por resumir textos mais longos em textos mais curtos. Tenha cuidado, alguns modelos têm um comprimento máximo de entrada. Isso significa que o resumo não pode lidar com livros completos, por exemplo. Cuidado ao escolher seu modelo. Se você quiser discutir suas necessidades de resumo, entre em contato conosco: <api-enterprise@huggingface.co>

**API_URL4**
***Modelo recomendado : deepset/roberta-base-squad2 .***
Tarefa de resposta a perguntas
Quer ter um bom bot sabe-tudo que pode responder a qualquer pergunta?