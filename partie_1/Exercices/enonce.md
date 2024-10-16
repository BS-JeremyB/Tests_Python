## Exercice 1 :

### Énoncé
Vous allez créer une fonction qui convertit une température de Celsius en Fahrenheit. Écrivez des tests unitaires pour vérifier le bon fonctionnement de cette fonction sans utiliser Pytest ou Unittest.

### Instructions
1. Créez une fonction `celsius_to_fahrenheit` dans un fichier nommé `temperature.py`.
2. La fonction doit prendre une température en Celsius et la convertir en Fahrenheit.
3. Créez un fichier de test `test_temperature.py`.
4. Écrivez des tests simples en utilisant `assert` pour vérifier que `celsius_to_fahrenheit(0)` retourne `32`, et que `celsius_to_fahrenheit(100)` retourne `212`.

## Exercice 2 :
### Énoncé
Vous allez créer une fonction `calculate_average` qui calcule la moyenne d'une liste de notes. Écrivez un test pour cette fonction en utilisant Unittest.

### Instructions
1. Créez une fonction `calculate_average` dans un fichier nommé `grades.py`.
2. La fonction doit prendre une liste de notes (entiers) et retourner la moyenne.
3. Créez un fichier de test `test_grades.py`.
4. Écrivez des tests avec `unittest` pour vérifier que `calculate_average([10, 20, 30])` retourne `20`, et que la fonction retourne `0` pour une liste vide.


## Exercice 3 :
### Énoncé
Vous allez installer `pytest` et utiliser une fonction de validation d'e-mails pour tester cette installation.

### Instructions
1. Installez `pytest` en exécutant `pip install pytest` dans le terminal.
2. Créez une fonction `is_valid_email` dans `email_utils.py` qui vérifie si une chaîne contient "@" et un domaine (comme ".com" ou ".org").
3. Créez un fichier de test `test_email_utils.py` pour vérifier la validité d'un e-mail en utilisant `pytest`.

