from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class ListTextWidget(forms.Textarea):
    def __init__(self, separator=",", *args, **kwargs):
        self.separator = separator
        super().__init__(*args, **kwargs)

    def format_value(self, value):
        if isinstance(value, list):
            return self.separator.join(value)
        return value


class ListField(models.JSONField):
    description = _("List of values")

    def __init__(self, *args, **kwargs):
        kwargs["blank"] = True
        kwargs["null"] = True
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if value and not isinstance(value, list):
            raise ValidationError("Value must be a list.")

    def formfield(self, **kwargs):
        kwargs["widget"] = ListTextWidget
        return super().formfield(**kwargs)
