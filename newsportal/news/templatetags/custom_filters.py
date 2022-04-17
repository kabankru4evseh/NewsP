from django import template

register = template.Library()

# список слов, которые будем цензурировать
STRONG_WORDS = ["Ебанись", "Хуй", "Пизда", "Говно",]


@register.filter()
def censor(value):
   if not isinstance(value, str):
       raise ValueError('Нельзя цензурировать не строку')

   for word in STRONG_WORDS:
       value = value.replace(word[1:], '*' * (len(word)-1))

   return value