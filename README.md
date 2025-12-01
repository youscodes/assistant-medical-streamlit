# assistant-medical-streamlit
Assistant Symptômes 
Application interactive permettant d’orienter l’utilisateur sur des symptômes courants (grippe, allergie, mal de gorge) grâce à une interface simple développée avec Streamlit.
📌 Objectif du projet
Ce projet a été réalisé dans le cadre d’un premier exercice pratique pour découvrir :
- la création d’une interface utilisateur simple,
- l’utilisation de Streamlit pour développer une application interactive en Python,
- la structuration d’un projet reproductible et partageable,
- la mise en ligne d’un mini outil pouvant être utilisé par d’autres utilisateurs.
L’application n’est pas un outil de diagnostic médical, mais une démonstration technique orientant l’utilisateur en fonction de symptômes selectionnés.

🛠️ Technologies utilisées
- Python 3.12.2
- Streamlit (framework pour applications web)
- VS Code (développement)
- Git / GitHub (versioning et partage)

  🖥️ Fonctionnalités principales
- Interface graphique simple et intuitive
- Sélection de symptômes via des checkbox
- Analyse de correspondance avec :
* symptômes de grippe
* symptômes d’allergies
* maux de gorge
- Affichage dynamique :
Résultats
Conseils basiques
Alerte sécurité

🔍 Logique (résumé)
L’application analyse les combinaisons de symptômes sélectionnés pour afficher des orientations générales.
Toux + fièvre → profil compatible grippe
Éternuements + yeux qui grattent → profil compatible allergie
Mal de gorge → irritation ou infection légère
