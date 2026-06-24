from django import template
import re

BAD_WORDS = {'редиска', 'сука', 'блять', 'блядь', 'уебок', 'уёбок', 'пидор', 'хуевый'}

register = template.Library()

@register.filter
def censor(text):
    def word_refactor(match):
        word = match.group()

        censored = word[0] + '*' * (len(word) - 1)

        return censored

    for word in BAD_WORDS:
        pattern = r"\b" + re.escape(word) + r"\b"
        text = re.sub(pattern, word_refactor, text, flags=re.IGNORECASE)

    return text
