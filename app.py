from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = Flask(__name__)

# Função para dividir o texto em sentenças
def split_into_sentences(text):
    sentencas = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [s.strip() for s in sentencas if s.strip()]

# Carregar o documento de texto
with open('internet.txt', 'r', encoding='utf-8') as file:
    document = file.read()

# Dividir o documento em sentenças
sentencas = split_into_sentences(document)

# Criar o vetor TF-IDF para as sentenças
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentencas)

def answer_question(question, threshold=0.2):
    # Pré-processar a pergunta
    question = question.lower().strip()
    
    # Converter a pergunta para o formato TF-IDF
    question_tfidf = vectorizer.transform([question])
    
    # Calcular similaridade de cosseno entre a pergunta e as sentenças do documento
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)
    
    # Encontrar a sentença mais similar
    most_similar_index = np.argmax(similarity)
    
    # Verificar se a similaridade é alta o suficiente
    if similarity[0, most_similar_index] >= threshold:
        return sentencas[most_similar_index]
    else:
        return "Desculpe, não consegui encontrar uma resposta adequada."

@app.route('/do_answer', methods=['POST'])
def do_answer():
    data = request.json
    question = data.get('pergunta', '')
    answer = answer_question(question)
    return jsonify({'resposta': answer})

if __name__ == '__main__':
    app.run(debug=True)
