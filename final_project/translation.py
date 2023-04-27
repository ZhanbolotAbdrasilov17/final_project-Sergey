from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Worker)
class WorkerTranslation(TranslationOptions):
    fields = ('full_name', 'position')
