from django import forms


class createOrganisationFormModal(forms.Form):
    organisation_name = forms.CharField(label="Название Организации",
                                        widget=forms.TextInput(attrs={'placeholder': 'Введите название организации'}))
    organisation_adress = forms.CharField(label="Адрес регистрации Организации",
                                          widget=forms.TextInput(attrs={'placeholder': 'Введите адрес организации'}))
    organisation_inn = forms.CharField(label="ИНН",
                                       widget=forms.TextInput(attrs={'placeholder': 'Введите ИНН организации'}))
    organisation_okved = forms.CharField(label="Вид деятельности (ОКВЭД)",
                                         widget=forms.TextInput(attrs={'placeholder': 'ОКВЭД'}))
