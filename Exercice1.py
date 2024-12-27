Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n1 = char(input("Veullez saisir votre prenom")); n2 =char( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('Bienvenue');
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    n1 = char(input("Veullez saisir votre prenom")); n2 =char( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('Bienvenue');
NameError: name 'char' is not defined. Did you mean: 'chr'?
>>> n1 = chr(input("Veullez saisir votre prenom")); n2 =chr( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('\nBienvenue');
Veullez saisir votre prenomMamadou Bailo
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    n1 = chr(input("Veullez saisir votre prenom")); n2 =chr( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('\nBienvenue');
TypeError: 'str' object cannot be interpreted as an integer
>>> n1 = chr(input("Veullez saisir votre prenom")); n2 =chr( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('\nBienvenue');
Veullez saisir votre prenommamadou
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    n1 = chr(input("Veullez saisir votre prenom")); n2 =chr( input("Veuillez saisir votre nom"));print ("\nBonjour " +str(n1)+ " " +str(n2));print('\nBienvenue');
TypeError: 'str' object cannot be interpreted as an integer
>>> prenom = input("Veuillez saisir votre prenom"); nom = input ("Veuillez saisir votre nom");print("Bonjour" +str(prenom)+ " " +str(nom));
Veuillez saisir votre prenomMamadou
Veuillez saisir votre nomDiallo
BonjourMamadou Diallo
>>> prenom = input("Veuillez saisir votre prenom"); nom = input ("Veuillez saisir votre nom");print("\nBonjour " +str(prenom)+ " " +str(nom));print("\nBienvenue");
Veuillez saisir votre prenomMamadou
Veuillez saisir votre nomDiallo

Bonjour Mamadou Diallo

Bienvenue
