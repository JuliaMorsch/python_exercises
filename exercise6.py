# A program that analyzes data from participants in a scientific event
import numpy as np

# participants data
participants = [
    {
        'nome': "Agatha",
        'localizacao':"Brasil"
        'afiliacao': "UFSC",
        'interesses': ['Física', 'Astronomia']
    }
    {
        'nome': "Hugo",
        'localizacao':"Mexico"
        'afiliacao': "Intituto A",
        'interesses': ['Gastrônomia', 'Astronomia']
    }
    {
        'nome': "Agatha",
        'localizacao':"Argentina"
        'afiliacao': "Instituto C",
        'interesses': ['Geografia', 'Engenharia']
    }
]

# identifying different regions of the 
regions = set(participant['localizacao'] for participant in participants)
