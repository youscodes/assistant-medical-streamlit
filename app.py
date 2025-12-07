import streamlit as st

st.set_page_config(
    page_title="Assistant Symptômes",
    page_icon="🩺",
    layout="centered"
)

# ----- HEADER -----
st.title("🩺 Assistant Symptômes Courants")
st.markdown("""
Cet assistant vous aide à identifier des **symptômes courants** liés :
- à la grippe  
- aux allergies  
- au mal de gorge  

Il ne remplace pas un avis médical professionnel.
""")

st.divider()

# ----- SYMPTÔMES SECTION -----
st.header("Décrivez vos symptômes")

col1, col2 = st.columns(2)

with col1:
    fievre = st.checkbox("Fièvre")
    frissons = st.checkbox("Frissons")
    toux = st.checkbox("Toux")
    toux_seche = st.checkbox("Toux sèche")
    nez_coule = st.checkbox("Nez qui coule")
    fatigue = st.checkbox("Fatigue")

with col2:
    maux_gorge = st.checkbox("Mal de gorge")
    eternuements = st.checkbox("Éternuements")
    yeux_rouges = st.checkbox("Yeux rouges / qui grattent")
    demangeaisons = st.checkbox("Démangeaisons du nez")
    maux_tete = st.checkbox("Maux de tête")

temperature = st.slider("Température corporelle (°C)", 35.0, 41.0, 37.0)

autres = st.text_area("Autres symptômes (optionnel)", "")

st.divider()

# ----- LOGIQUE -----
def analyser_symptomes():
    possible = []
    conseils = []

    # Grippe
    if (fievre or frissons) and (toux or fatigue or maux_tete):
        possible.append("🟧 Symptômes compatibles avec une **grippe légère**.")

    # Allergie
    if eternuements or yeux_rouges or demangeaisons:
        possible.append("🟦 Symptômes compatibles avec une **allergie** (poussière, pollen, etc.).")

    # Mal de gorge
    if maux_gorge:
        possible.append("🟨 Symptômes compatibles avec un **mal de gorge**.")

    # Température
    if temperature >= 38.5:
        possible.append(f"🌡️ Température élevée : **{temperature}°C**")

    # Conseils généraux
    if fievre or frissons:
        conseils.append("Buvez beaucoup d'eau et reposez-vous.")
    if maux_gorge:
        conseils.append("Évitez le froid et privilégiez les boissons chaudes.")
    if eternuements or yeux_rouges:
        conseils.append("Aérez la pièce et évitez les allergènes si possible.")
    if fatigue:
        conseils.append("Dormez suffisamment pour soutenir votre récupération.")

    if not possible:
        possible.append("Aucun regroupement clair. Vos symptômes sont trop généraux.")

    if not conseils:
        conseils.append("Si les symptômes persistent, consultez un médecin.")

    return possible, conseils


# ----- BOUTON -----
if st.button("Analyser"):
    resultats, conseils = analyser_symptomes()

    st.subheader("Résultats")
    with st.container():
        st.markdown(
            """
            <div style="padding: 15px; border-radius: 10px; background-color: #f8f9fa;">
            """,
            unsafe_allow_html=True
        )
        for r in resultats:
            st.write(r)
        st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Conseils")
    with st.container():
        st.markdown(
            """
            <div style="padding: 15px; border-radius: 10px; background-color: #eef7ff;">
            """,
            unsafe_allow_html=True
        )
        for c in conseils:
            st.write("• " + c)
        st.markdown("</div>", unsafe_allow_html=True)
@app.route('/rendez-vous')
def rendez_vous():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rendez-vous - Mon Cabinet</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin:0; padding:20px; background:#f8f9fa; }}
            .formulaire {{ max-width:900px; margin:40px auto; background:white; padding:40px; border-radius:20px; box-shadow:0 10px 40px rgba(0,0,0,0.1); text-align:center; }}
            iframe {{ width:100%; height:1000px; border:none; border-radius:16px; }}
        </style>
    </head>
    <body>
        <!-- ICI TU PEUX GARDER TON MENU / HEADER EXISTANT SI TU VEUX -->
        
        <div class="formulaire">
            <h1>Prenez rendez-vous en 30 secondes</h1>
            <p>Notre IA analyse vos symptômes et réserve automatiquement si nécessaire</p>
            
            <iframe src="https://yastene44.app.n8n.cloud/form/1878a2aa-d70e-425e-af4b-08e604abef4f" allowfullscreen></iframe>
        </div>
    </body>
    </html>
    """

