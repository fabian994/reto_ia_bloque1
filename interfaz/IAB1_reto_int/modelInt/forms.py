from django import forms

class Prediction(forms.Form):
    ModelDate = forms.DateField(   
                                    required = True,
                                    label = "Fecha ",
                                    error_messages={
                                            "required": "No puede estar vacío",
                                        },
                                    widget=forms.DateInput(attrs={
                                        "class" : "form-control",
                                        "type": "date"
                                    })
                                    )
    
    ModelStore = forms.IntegerField(    max_value=999999,
                                        required = True, 
                                        label = "Inventario",
                                        error_messages={
                                            "required": "No puede estar vacío",
                                        },
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                            }
                                        ))
    ModelOnp = forms.IntegerField(    max_value=999999,
                                        required = True, 
                                        label = "Inventario",
                                        error_messages={
                                            "required": "No puede estar vacío",
                                        },
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                            }
                                        ))
    
    ModelFamily = forms.ChoiceField(required = True, 
                                        choices = (("", "---"),
                                                   ("3", "5 Días, Costo: $100"),
                                                   ("3",'AUTOMOTIVE'),
                                                   ("4",'BABY CARE'),
                                                   ("5",'BEAUTY'),
                                                   ("6",'BEVERAGES'),
                                                   ("7",'BOOKS'),
                                                   ("8",'BREAD/BAKERY'),
                                                   ("9",'CELEBRATION'),
                                                   ("10",'CLEANING'),
                                                   ("11",'DAIRY'),
                                                   ("12",'DELI'),
                                                   ("13",'EGGS'),
                                                   ("14", 'FROZEN FOODS'),
                                                   ("15",'GROCERY I'),
                                                   ("16", 'GROCERY II'),
                                                   ("17", 'HARDWARE'),
                                                   ("18",'HOME AND KITCHEN I'),
                                                   ("19",'HOME AND KITCHEN II'),
                                                   ("20",'HOME APPLIANCES'),
                                                   ("21",'HOME CARE'),
                                                   ("22",'LADIESWEAR'),
                                                   ("23",'LAWN AND GARDEN'),
                                                   ("24",'LINGERIE'),
                                                   ("25",'LIQUORWINEBEER'),
                                                   ("26",'MAGAZINES'),
                                                   ("27",'MEATS'),
                                                   ("28",'PERSONAL CARE')
                                                   ("29",'PET SUPPLIES'),
                                                   ("30",'PLAYERS AND ELECTRONICS'),
                                                   ("31",'POULTRY'),
                                                   ("32",'PREPARED FOODS'),
                                                   ("33",'PRODUCE')
                                                   ("34",'SCHOOL AND OFFICE SUPPLIES'),
                                                   ("35",'SEAFOOD'),
                                                    
                                        ), 
                                        label = "Duracion de Subasta",
                                        widget = forms.Select(attrs = {
                                                    "class": "form-control",
                                                },
                                        ))
    
    Holidays= forms.ChoiceField(required = True, 
                                        choices = (("", "---"),
                                                  ('36','Provincializacion de Cotopaxi'),
                                                    ('37', 'Provincializacion de Imbabura'),
                                                   ('38', 'Primer Grito de Independencia'),
                                                    ('39', 'Independencia de Guayaquil'),
                                                    ('40', 'Dia de Difuntos'),
                                                    ('41', 'Independencia de Cuenca'),
                                                   ('42','Provincializacion de Santo Domingo'),
                                                    ('43', 'Provincializacion Santa Elena'),
                                                    ('44', 'Navidad-1'),
                                                    ('45', 'Primer dia del ano'),
                                                    ('46', 'Carnaval'),
                                                    ('47', 'Viernes Santo'),
                                                    ('48', 'Dia del Trabajo'),
                                                    ('49', 'Dia de la Madre')
                                        ), 
                                        label = "Duracion de Subasta",
                                        widget = forms.Select(attrs = {
                                                    "class": "form-control",
                                                },
                                        ))