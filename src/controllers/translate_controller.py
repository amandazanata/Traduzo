from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    to_translate = ""
    translated_from = "pt"
    translate_to = "en"
    translated = "Tradução"
    translation = ""
    if request.method == "POST":
        to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translation = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(
            to_translate
        )
        history = HistoryModel(
            {
                "text_to_translate": to_translate,
                "translate_from": translate_from,
                "translated_text": translation,
            }
        )
        history.save()

    return render_template(
        "index.html",
        text_to_translate=to_translate,
        translate_from=translated_from,
        translate_to=translate_to,
        translated=translation or translated,  # type: ignore
        languages=languages,
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translate_to, translate_from = translate_from, translate_to
    translation = GoogleTranslator(
        source=translate_to, target=translate_from
    ).translate(
        to_translate
    )
    history = HistoryModel(
        {
            "text_to_translate": to_translate,
            "translate_from": translate_from,
            "translated_text": translation,
        }
    )
    history.save()

    return render_template(
        "index.html",
        text_to_translate=to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translation,
        languages=LanguageModel.list_dicts(),
    )
