# EcommerceNLP

Simple NLP APIs to classify ecommerces.

Currently supported:
* ecommerce-detection
* ecommerce-category

Currently supported languages:
- English

## Requirement

Python3 or docker machine

## Run API

### Manual 

```bash
git clone git@github.com:digestoo/ecommerce-nlp.git
cd ecommerce-nlp
pip install -r requirements.txt
python api.py
```

### Docker

```bash
docker pull mdruzkowski/ecommerce-nlp
docker run -it -p 5005:5005 mdruzkowski/ecommerce-nlp
```

##  Details of supported endpoints

### ecommerce-detection

```bash
curl -XPOST -H "Content-Type: application/json"  -d '{"content":"simple text"}'  http://localhost:5005/ecommerce-detection
```

POST params:

- `content` - text in English

Results JSON:
- `score` - score from 0 to 100

### ecommerce-category

```bash
curl -XPOST -H 'Content-Type: appliction/json' -d '{"content":"simple text"}' http://localhost:5005/ecommerce-category
```

POST params:

- `content` - text in English

Results JSON:
- `category` - one of the Ecommerce's categories
