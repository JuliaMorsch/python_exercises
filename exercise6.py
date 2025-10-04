# A program that analyzes data from participants in a scientific event
import numpy as np

# participants data
participants = [
    {
        'nome': "Agatha",
        'localizacao':"Brasil",
        'afiliacao': "UFSC",
        'interesses': ['Física', 'Astronomia']
    },
    {
        'nome': "Hugo",
        'localizacao':"Mexico",
        'afiliacao': "Intituto A",
        'interesses': ['Gastrônomia', 'Astronomia']
    },
    {
        'nome': "Agatha",
        'localizacao':"Argentina",
        'afiliacao': "Instituto C",
        'interesses': ['Geografia', 'Engenharia']
    }
]

# identifying different regions of the 
regions = set(participant['localizacao'] for participant in participants)

# categorizing affiliations
affiliations = {}
for participant in participants:
    affil = participant['afiliacao']
    if affil not in affiliations:
        affiliations[affil] = []
    affiliations[affil].append(participant['nome'])

# Using NumPy to alaize interest of area
interest_areas = np.array([interest for participant in participants for interest in participant['interesses']])
unique_interests, counts = np.unique(interest_areas, return_counts=True)
popular_area = unique_interests[np.argmax(counts)]

#Results
print("Regions represented:", regions)
print("Affiliations categorized:", affiliations)
print("Most popular area of interest:", popular_area)