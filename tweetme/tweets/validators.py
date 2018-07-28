from django.core.exceptions import ValidationError
def restrictmodel(data):
    if data=="abcd":
        raise ValidationError("dont enter abcd")
    return data
