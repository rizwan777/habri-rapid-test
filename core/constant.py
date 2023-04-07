# profile type
FATHER = "FATHER"
MOTHER = "MOTHER"
ADOPTED = "ADOPTED"
OTHER = "OTHER"
ROLES_CHOICES = [
    (FATHER, 'FATHER'),
    (MOTHER, 'MOTHER'),
    (ADOPTED, 'ADOPTED'),
    (OTHER, 'OTHER'),
]

# gender types
MALE = "MALE"
FEMALE = "FEMALE"
OTHER = "OTHER"

GENDER_CHOICES =[
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER"),
]

# document types
AADHAR_CARD ="AADHAR_CARD"
POA ="POA"
POI = "POI"
TC = "TC"
OTHER = "OTHER"

DOCUMENT_CHOICES =[
    (AADHAR_CARD, "AADHAR_CARD"),
    (POA, "POA"),
    (POI,"POI"),
    (TC,"TC"),
    (OTHER, "OTHER"),
]