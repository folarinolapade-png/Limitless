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

Give your answer in this format:

🔴 POSSIBLE ALLERGEN
Explain what in the image may contain {allergy}.

🟢 NO OBVIOUS ALLERGEN FOUND
Explain if you do not see an obvious source of {allergy}.

🟡 UNCERTAIN
Explain anything that cannot be determined from the image.

IMPORTANT:
Do not claim that food is completely safe or allergen-free.
If the image is unclear, say that it is unclear.
Tell the user to verify ingredients with the restaurant or manufacturer.
"""

            with st.spinner("🤖 MenuMind is analyzing your image..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[prompt, image]
                )

            st.divider()
            st.subheader("🔎 MenuMind Results")

            st.write(response.text)

        except Exception as error:

            st.error(
                "MenuMind could not complete the scan."
            )

            st.caption(
                "Check that your Gemini API key and requirements.txt are set up correctly."
            )

else:

    st.info(
        "👆 Upload a menu or food-label photo to get started."
    )

st.divider()

st.caption("MenuMind AI • Classroom MVP")
