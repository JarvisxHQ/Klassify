from monkeylearn import MonkeyLearn
import json as js

def extract(result):
    for fields in result:
        for type in fields['extractions']:
            summary = type['parsed_value']
    return summary

def getSummary(data):
    ml = MonkeyLearn('1b7cc2a4cc60be4e78dc391133487d882a56cb39')
    model_id = 'ex_94WD2XxD'
    result = ml.extractors.extract(model_id, data)
    return extract(result.body)