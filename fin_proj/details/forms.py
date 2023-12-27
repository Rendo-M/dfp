from django import forms

class InputACLN(forms.Form):
    comment = forms.CharField()
    #figure = forms.ImageField(upload_to='fig/')
    #instrument_id = forms.ForeignKey(Instrument, on_delete=models.DO_NOTHING)
    speed =  forms.IntegerField()
    rpm =   forms.IntegerField()
    programm =  forms.CharField()  