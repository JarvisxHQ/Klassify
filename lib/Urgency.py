from monkeylearn import MonkeyLearn
import json as js

def extract(result):
    for fields in result:
        for type in fields['classifications']:
            urgency = type['tag_name']
    return urgency

def getUrgency(data):
    ml = MonkeyLearn('1b7cc2a4cc60be4e78dc391133487d882a56cb39')
    model_id = 'cl_Aiu8dfYF'
    result = ml.classifiers.classify(model_id, data)
    return extract(result.body)
