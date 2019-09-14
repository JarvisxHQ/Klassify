from monkeylearn import MonkeyLearn
import json as js

def extract(result):
    for fields in result:
        for type in fields['classifications']:
            topic = type['tag_name']
    return topic

def getEmailTopic(data):
    ml = MonkeyLearn('1b7cc2a4cc60be4e78dc391133487d882a56cb39')
    model_id = 'cl_oPySQ2sC'
    result = ml.classifiers.classify(model_id, data)
    return extract(result.body)