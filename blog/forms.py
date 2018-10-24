from django.contrib.auth.models import User


class articleForm(forms.ModelForm):
    class Meta:
        model = Article

    def clean_author(self):
        if not self.cleaned_data['author']:
            return User()
        return self.cleaned_data['author']

    def clean_last_modified_by(self):
        if not self.cleaned_data['updated_by']:
            return User()
        return self.cleaned_data['updated_by']
