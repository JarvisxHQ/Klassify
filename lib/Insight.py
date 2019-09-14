from monkeylearn import MonkeyLearn
import json as js

def extract(result):
    for fields in result:
        for type in fields['extractions']:
            for sub in type['extractions']:
                if sub['tag_name'] == "KEYWORD":
                    print(str(sub['parsed_value']) + ' ' + str(sub['count']) + ' ' + str(sub['relevance']))
                else:
                    print(sub['parsed_value'])
                    print('\n')

def getInsight(data):
    ml = MonkeyLearn('1b7cc2a4cc60be4e78dc391133487d882a56cb39')
    model_id = 'ex_EjosnyKK'
    result = ml.extractors.extract(model_id, data)
    extract(result.body)