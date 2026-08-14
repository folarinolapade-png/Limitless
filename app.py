import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(
    page_title="MenuMind AI",
    page_icon="🍽️"
)

st.title("🍽️ MenuMind AI")
st.subheader("Smart Allergy & Nutrition Scanner")

st.write(
    "Upload a photo of a restaurant menu or food label "
    "and MenuMind AI will look for possible allergens."
)

st.warning(
    "⚠️ MenuMind AI cannot guarantee that food is allergen-free. "
    "Always verify ingredients with the restaurant or manufacturer."
)

st.divider()

allergy = st.selectbox(
    "What should MenuMind check for?",
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

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Your uploaded image",
        use_container_width=True
    )

    if st.button("🔍 Scan with MenuMind AI"):

        try:
            api_key = st.secrets["GEMINI_API_KEY"]

            client = genai.Client(api_key=api_key)

            prompt = f"""
You are MenuMind AI, a food-allergen information assistant.

Look carefully at the uploaded image.

The user wants to check for:
{allergy}

Analyze visible food, menu text, or ingredient-label text.

Explain:
1. Possible sources of {allergy}
2. Anything that is uncertain
3. Whether the image is clear enough to make a useful assessment

Never claim that food is completely safe or allergen-free.
Tell the user to verify ingredients with the restaurant or manufacturer.
"""

            with st.spinner("🤖 MenuMind is analyzing your image..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=[prompt, image]
                )

            st.divider()
            st.subheader("🔎 MenuMind Results")
            st.write(response.text)

        except Exception as error:

            st.error("MenuMind could not complete the scan.")
            st.exception(error)

else:

    st.info(
        "👆 Upload a menu or food-label photo to get started."
    )

st.divider()

st.caption("MenuMind AI • Classroom MVP")
