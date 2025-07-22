import streamlit as st
import google.generativeai as genai

#Setting Gemini API key here

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Title
st.title("🎓 Scholarship Filter Tool ")

# Input Fields
home_country = st.text_input("You're Applying From (e.g., India, Bangladesh)")
country = st.text_input("Preferred Countries (e.g., Germany, Taiwan, UK)")
degree = st.selectbox("Degree Level", ["Undergraduate", "Postgraduate", "PhD"])
field = st.text_input("Field of Study (e.g., Microbiology)")
funding = st.radio("Funding Preference", ["Self-funded", "Need Scholarship"])
language = st.text_input("Language of Instruction (e.g., English)")
other = st.text_area("Any other preferences?")

# ✨ Generate Scholarships
if st.button("Find Scholarships ✨"):
    with st.spinner("Thinking..."):
        prompt = f"""
Suggest scholarships or study programs based on the following preferences:
- Country: {country}
- Applying from : {home_country}
- Degree: {degree}
- Field: {field}
- Funding: {funding}
- Language: {language}
- Other preferences: {other}
"""

        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)

        st.markdown("🎓 Suggested Scholarships / Programs")
        st.write(response.text)

       

