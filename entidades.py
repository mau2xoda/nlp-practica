import spacy
nlp = spacy.load("es_core_news_sm")
doc = nlp("Microsoft es una empresa fundada por Bill Gates y tiene a google")
palabras_utiles = []
palabras_vacias = []
for token in doc:
    if not token.is_stop:
        palabras_utiles.append(token.text)
    else:
         palabras_vacias.append(token.text)
print(palabras_utiles)
print(palabras_vacias)
