import json
import requests

def sentiment_analyzer(text_to_analyse) -> str:
    url= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj= { "raw_document": { "text": text_to_analyse } }
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response= requests.post(url= url, json= myobj, headers= headers)
    formatted_response= json.loads(response.text)
    print(formatted_response)
    label= formatted_response['documentSentiment']['label']
    score= formatted_response['documentSentiment']['score']
    return {'label': label, 'score': score}