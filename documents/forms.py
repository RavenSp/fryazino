from django import forms
from .models import DocsAuthor, DocType, DocCategory, Documents

class DocFilter(forms.Form):

	number = forms.CharField(label='Номер документа', required=False)
	author = forms.ModelChoiceField(label='Орган, принявший документ', queryset=DocsAuthor.objects.all(), required=False)
	typedoc = forms.ModelChoiceField(label='Тип документа', queryset=DocType.objects.all(), required=False)
	category = forms.ModelChoiceField(label='Категория документа', queryset=DocCategory.objects.filter(active=True), required=False)
	dateStart = forms.DateField(label='Дата начала', required=False)
	dateEnd = forms.DateField(label='Дата окончания', required=False)
	search = forms.CharField(label='Документ содержит', required=False)

	class Meta:

		pass