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
    json_list = HistoryModel.list_as_json()
    languages_list = json.loads(json_list)

    for translation in languages_list:
        translation.pop("_id", None)

    assert languages_list == expected
