import re


BAD_WORDS = {'редиска', 'сука', 'блять', 'блядь', 'уебок', 'уёбок', 'пидор', 'хуевый'}


def censor(text, bad_words):
    def replace_word(match):
        word = match.group()

        censored = word[0] + "*" * (len(word) - 1)
        return censored

    for word in bad_words:
        pattern = r"\b" + re.escape(word) + r"\b"
        text = re.sub(pattern, replace_word, text, flags=re.IGNORECASE)

    return text

