from django.forms.models import BaseModelFormSet

class BootstrapModelFormSet(BaseModelFormSet):
    
    def __init__(self, *args, **kwargs):
        super(BootstrapModelFormSet, self).__init__(*args, **kwargs)
           
    def as_div(self):
        "Returns this formset rendered as HTML <p>s."
        forms = u' '.join([form.as_div() for form in self])
        return mark_safe(u'\n'.join([unicode(self.management_form), forms]))