from modeltranslation.translator import register, TranslationOptions
from .models import Blog, Comment

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # Add the fields you want to translate