from django import forms


class FileForm(forms.Form):
    CSV_FILES = forms.FilePathField(path="file_lib/")