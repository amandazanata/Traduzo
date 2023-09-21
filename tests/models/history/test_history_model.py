import json
from src.models.history_model import HistoryModel

expected = [
    {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    },
    {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    },
]

# Req. 7


def test_request_history():
    list_json = HistoryModel.list_as_json()
    list_languages = json.loads(list_json)

    for translation in list_languages:
        translation.pop("_id", None)

    assert list_languages == expected
