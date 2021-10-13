
from dnlp.languages import FASTTEXT_LANGUAGES


def remap_prediction(prediction):
    result = []
    if not prediction[0]:
        return result

    for index in range(len(prediction[0])):
        lang = prediction[0][index].replace('__label__', '')