MALE = 'M'
FEMALE = 'F'

GENDER_CHOICE = (
    (MALE, "Male"),
    (FEMALE, "Female"),
)
REQUEST_FROM_ACCOUNT = (
    ("Main", "Main"),
    ("Wallet", "Wallet"),
)

DEPOSIT = 1
WITHDRAWAL = 2
INTEREST = 3

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Deposit'),
    (WITHDRAWAL, 'Withdrawal'),
    (INTEREST, 'Interest'),
)

End_of_the_Year_Contribution=1
Sallah_Contribution=2
Hajj_or_Umrah_Pilgrimage=3
Jerusalem_Pilgrimage=4
Car_Facility=5
Mortgage_Facilty=6

CONTRIBUTION_TYPES_CHOICES = (
(End_of_the_Year_Contribution,"End of the Year Contribution"),
(Sallah_Contribution,"Sallah Contribution"),
(Hajj_or_Umrah_Pilgrimage,"Hajj/Umrah Pilgrimage"),
(Jerusalem_Pilgrimage,"Jerusalem Pilgrimage"),
(Car_Facility,"Car Facility"),
(Mortgage_Facilty,"Mortgage Facilty")
)