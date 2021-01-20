from django import forms


class DetailForm(forms.Form):
    Fullname = forms.CharField(label='FullName', max_length=40,widget=forms.TextInput(attrs={'placeholder':'fullname'}))
    Bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'something about you'
                                                                     '....preferred development language etc. '}))
    pic = forms.ImageField(allow_empty_file=True)
    Phone = forms.IntegerField(label='Phone',max_value=1000000000000,widget=forms.NumberInput(
        attrs={'placeholder':'Phone'}))
    Email = forms.EmailField(label='Email',max_length=40,widget=forms.EmailInput(attrs={'placeholder':'Email'}))


class CertificationForm(forms.Form):
    certification = forms.FileField(label='certification',allow_empty_file=False)
    reference = forms.EmailField(label='Email of reference')

