from django import forms 

from .models import Asignacion, Alumnos, Cursos

class AsignacionForm(forms.ModelForm):
    alum = forms.ModelChoiceField(
        queryset = Alumnos.objects.all()
        .order_by('nombre')
    )
    cur = forms.ModelChoiceField(
        queryset = Cursos.objects.all()
        .order_by('nombre')
    )
    class Meta:
        model = Asignacion
        fields = ['alum', 'cur', 'fecha_asignacion']
        labels = {'fecha_asignacion':"fecha_asignacion"}
        widget = {'fecha_asignacion': forms.TextInput}

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['alum'].empty_label = "Seleccione Alumno"
        self.fields['cur'].empty_label = "Seleccione Curso"
        

