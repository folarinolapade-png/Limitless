import streamlit as st

st.set_page_config(
    page_title="MenuMind AI",
    page_icon="🍽️"
)

st.title("🍽️ MenuMind AI")
st.subheader("Smart Allergy & Nutrition Scanner")

st.write(
    "Upload a photo of a restaurant menu or food label "
    "and MenuMind will help identify possible allergens."
)

st.warning(
    "⚠️ AI cannot guarantee that food is allergen-free. "
    "Always check with the restaurant or food manufacturer."
)

st.divider()

allergy = st.selectbox(
    "What do you want MenuMind to check for?",
    [
        "Peanuts",
        "Tree nuts",
        "Dairy",
        "Gluten",
        "Eggs",
        "Soy"
    ]
)

uploaded_file = st.file_uploader(
    "📷 Upload a menu or food-label photo",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="Your uploaded image",
        use_container_width=True
    )

    st.info(
        "MenuMind is ready to check this image for possible "
        + allergy
        + " allergens."
    )

    if st.button("🔍 Scan with MenuMind AI"):
        st.success(
            "The scan button is working! "
            "Gemini AI will be connected next."
        )
else:
    st.info("👆 Upload a menu or food-label photo to get started.")

st.divider()

st.caption("MenuMind AI • Classroom MVP")
