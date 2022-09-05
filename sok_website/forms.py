from cProfile import label
from django import forms



class UploadFileForm(forms.Form):
    file = forms.FileField(label="PDF tiedostot zip kansiossa")


class UploadPIMForm(forms.Form):
    file = forms.FileField(label="PIM .xlsx -tiedosto")


class checkBox(forms.ModelForm):
    box = forms.BooleanField()


# basically a file upload like the one on top
class uploadXLSX(forms.Form):
    file = forms.FileField()


class uploadToConverter(forms.Form):
    zipfile = forms.FileField(label="PDF tiedostot zip kansiossa")
    export_grid = forms.FileField(label="Uudelleennimeämistaulukko")
    # box = forms.BooleanField(label="Don't use new name grid",help_text="tick if you don't want to use")


class download_menu(forms.Form):
    def __init__(self, CHOICES, label):

        # call standard __init__
        super().__init__()
        # extend __init__
        # CHOICES = get_downloads("xlsx")
        self.fields["selection"] = forms.CharField(
            label=label, widget=forms.Select(choices=CHOICES)
        )

    # CHOICES = [("Debug","debug"),("Debug2","debug2"),("Debug3","debug3"),("Debug4","debug4")]

    selection = forms.CharField()


class download_menu2(forms.Form):
    selection = forms.CharField()

queryChannels=["Yleinen","Huolto","AsPa","Myynti"]
def getOptions(queryChannels=queryChannels):
    
    channels=[]
    for channel in queryChannels:
        channels.append((channel,channel))
    
    tupla = tuple(channels)
    
    return tupla
class uploadNote(forms.Form):
    nimi = forms.CharField(max_length=100)
    channel = forms.CharField(widget=forms.RadioSelect(choices=getOptions()))
    teksti = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'10', 'cols':'5'}))

class uploadPhotoNote(forms.Form):
    nimi = forms.CharField(max_length=100,required=False)
    channel = forms.CharField(widget=forms.RadioSelect(choices=getOptions()))
    kuva = forms.ImageField()

