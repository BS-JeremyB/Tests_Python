## Exercice 1 :
### Énoncé
Vous allez créer une fonction qui envoie un e-mail, puis utiliser un mock pour simuler cet envoi dans un test.

### Instructions
1. Créez une fonction `send_email` dans un fichier nommé `email_service.py`.
2. La fonction doit prendre un sujet, un destinataire et un corps de texte comme paramètres.
3. Utilisez `print()` pour simuler l’envoi dans la fonction `send_email`.
4. Dans un fichier `test_email_service.py`, créez un test en utilisant `unittest.mock` pour simuler l'envoi d'un e-mail.

## Exercice 2 :
### Énoncé
Créez une vue Django pour ajouter et afficher des produits, et testez-la en utilisant `pytest-django`.

### Instructions
1. Dans un projet Django, créez un modèle `Product` avec des champs `name` et `price` dans un fichier `models.py`.
2. Ajoutez une vue `product_list` pour afficher les produits et une vue `add_product` pour ajouter un produit.
3. Créez un fichier `test_views.py` pour tester ces vues en utilisant `pytest-django`.
