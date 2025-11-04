from django import forms
from .models import Qeyd

class QeydFormu(forms.ModelForm):
    class Meta:
        # Hansı Model əsasında form yaratdığımızı deyirik
        model = Qeyd
        # Formda hansı sahələrin görünməsini istədiyimizi deyirik
        fields = ['basliq', 'mezmun']
        # İstəyə görə sahələrin görünüşünü tənzimləyə bilərik (məsələn, CSS sinifləri)
        widgets = {
            'basliq': forms.TextInput(attrs={'placeholder': 'Qeydin başlığını daxil edin'}),
            'mezmun': forms.Textarea(attrs={'placeholder': 'Qeydin məzmununu daxil edin', 'rows': 5}),
        }