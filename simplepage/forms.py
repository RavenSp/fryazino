from django import forms
from dal import autocomplete
from .models import Page
from documents.models import Documents

class DocsForm(forms.ModelForm):

	#docs = forms.ModelChoiceField(
	#	queryset = Documents.objects.all(),
	#	widget = autocomplete.ModelSelect2Multiple(url='doc-autocomplete'),
	#	label = 'Прикрепленные документы'
	#	) 

	class Meta:

		model = Page
		fields = ('__all__')
		widgets = {
			'docs':autocomplete.ModelSelect2Multiple(url='doc-autocomplete', attrs={
					'style':'max-width: 860px;',
					'class':'js-example-basic-multiple',
				})
		}