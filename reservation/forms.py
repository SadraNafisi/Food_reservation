from django import forms
from .models import SubOrder
class SubOrderForm(forms.ModelForm):
    class Meta:
        model = SubOrder
        fields = ['amount']
        widgets = {
            "quantity":forms.NumberInput(attrs={"min":0})
        }

SubOrderformset = forms.formset_factory(SubOrderForm,extra=0)