from monkeylearn import MonkeyLearn
import json as js

def extract(result):
    for fields in result:
        for type in fields['classifications']:
            sentiment = type['tag_name']
    return sentiment

def getSentiment(data):
    ml = MonkeyLearn('1b7cc2a4cc60be4e78dc391133487d882a56cb39')
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, data)
    return extract(result.body)