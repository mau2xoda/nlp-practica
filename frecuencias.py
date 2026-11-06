import spacy

nlp = spacy.load("es_core_news_sm")

resenas = [
    "La entrega fue rápida y el precio es excelente",
    "El precio es alto pero la calidad es buena",
    "La entrega tardó demasiado, mala experiencia",
]

frecuencias = {}

for resena in resenas:
    doc = nlp(resena)
    for token in doc:
        if not token.is_stop and not token.is_punct:
            if token.text in frecuencias:
                frecuencias[token.text] += 1
            else:
                frecuencias[token.text] = 1

print(frecuencias)
