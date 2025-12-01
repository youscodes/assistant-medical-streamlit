import streamlit as st

st.set_page_config(page_title="Assistant Médical", page_icon="🩺")

st.title("Assistant Médical Simple")
st.write("Cet outil est uniquement éducatif et ne remplace **pas** un avis médical.")

questions = {
    "fièvre": "Avez-vous de la fièvre ?",
    "toux": "Avez-vous une toux ?",
    "tête": "Avez-vous mal à la tête ?",
    "fatigue": "Vous sentez-vous fatigué(e) ?",
    "gorge": "Avez-vous mal à la gorge ?",
    "difficulté_respirer": "Avez-vous une difficulté à respirer ?",
    "douleur_poitrine": "Ressentez-vous une douleur dans la poitrine ?",
    "nausée": "Avez-vous des nausées ?",
    "étourdissement": "Avez-vous des étourdissements ?",
    "douleur_abdomen": "Avez-vous des douleurs abdominales ?",
    "nez_coule": "Avez-vous le nez qui coule ?",
    "allergie_connue": "Souffrez-vous d'allergies connues ?",
    "maux_muscles": "Avez-vous des douleurs musculaires ?",
    "problème_sommeil": "Avez-vous des difficultés à dormir ?",
    "perte_appétit": "Avez-vous une perte d'appétit ?"
}

st.write("### Répondez aux questions")

symptomes = {}
cols = st.columns(2)

i = 0
for key, text in questions.items():
    with cols[i % 2]:
        symptomes[key] = st.radio(text, ["Oui", "Non"], horizontal=True) == "Oui"
    i += 1

st.write("---")

if st.button("Analyser mes symptômes"):
    st.subheader("Résultat :")

    if symptomes["fièvre"] and symptomes["toux"] and symptomes["fatigue"]:
        st.error("Vous présentez des signes d'une infection respiratoire courante.")
    elif symptomes["douleur_poitrine"]:
        st.error("Douleur thoracique — symptôme important.")
    elif symptomes["difficulté_respirer"]:
        st.error("Difficulté respiratoire — nécessite une attention rapide.")
    elif symptomes["maux_muscles"] and symptomes["fatigue"]:
        st.warning("Fatigue accompagnée de douleurs musculaires.")
    elif symptomes["nausée"] and symptomes["douleur_abdomen"]:
        st.warning("Vous semblez avoir des troubles digestifs.")
    else:
        st.info("Les symptômes ne correspondent pas à un schéma clair.")

    st.write("### Ce résultat n'est pas un diagnostic médical.")
