from django import template
import re

BAD_WORDS = {'редиска', 'сука', 'блять', 'блядь', 'уебок', 'уёбок', 'пидор', 'хуевый'}

register = template.Library()

@register.filter
def censor(text):
    def word_refactor(word):
        word[0] + '*' * (len(word) - 1)
