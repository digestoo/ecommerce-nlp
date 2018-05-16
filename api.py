# #!/usr/bin/python3

from klein import run, route, Klein
import json
import os
import pickle

app = Klein()

# nlp = spacy.load('en_core_web_sm')
# def tokeni(sentence):
#     return list([str(x) for x in nlp.tokenizer(sentence)])

def load_model(filename):
    with open(filename, 'rb') as f:
        model_struct = pickle.load(f)
        clf = model_struct['model']
    return clf

def predict_class_from_text(clf,text):
    predicted = clf.predict([text])[0]
    return predicted

def predict_proba_from_text(clf,text):
    proba = clf.predict_proba([text])[0][1]
    return int(proba*100)

@app.route("/ecommerce-category", methods=['POST'])
def get_category(request):
    content = json.loads(request.content.read())
    text = content['content']
    category = predict_class_from_text(category_clf,text)
    response = json.dumps({'category':category})
    return response


@app.route("/ecommerce-detection", methods=['POST'])
def get_isecommerce(request):
    content = json.loads(request.content.read())
    text = content['content']
    ecommerce_score = predict_proba_from_text(isecommerce_clf,text)
    response = json.dumps({'score':ecommerce_score})
    return response


ecommerce_model_path = os.path.join(os.path.dirname(__file__),'models','detector.bin')
isecommerce_clf = load_model(ecommerce_model_path)
category_model_path = os.path.join(os.path.dirname(__file__),'models','category.bin')
category_clf = load_model(category_model_path)

resource = app.resource

app.run("0.0.0.0", 5005)
