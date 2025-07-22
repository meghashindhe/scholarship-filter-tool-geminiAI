# 🎓 Scholarship Filter Tool – Powered by Gemini AI

This project is a web-based scholarship and study program suggestion tool built using Google's Gemini AI and Streamlit.  
It helps students quickly filter relevant scholarships based on their preferences such as destination, degree level, field of study, funding needs, and more.

---

## Features

- Takes input such as:
  - Target study country
  - Applicant's home country
  - Degree level (UG, PG, PhD)
  - Field of study
  - Funding preference
  - Language of instruction
  - Additional filters
- Uses Gemini-Pro API to generate customized scholarship suggestions
- Simple and interactive UI built with Streamlit
- Free to use with Google API key (no billing required)

---

## Technologies Used

- Python  
- Streamlit  
- Google Generative AI (gemini-2.5-pro)

---

## How to Run Locally

1. Clone the repository
bash
git clone https://github.com/meghashindhe/scholarship-filter-tool-geminiAI.git
cd scholarship-filter-tool-geminiAI


2. Install packages
pip install -r requirements.txt

3. Add your Gemini API key
python
genai.configure(api_key="your-api-key-here")

4. Run the app
bash
streamlit run app.py


---


How to Get Gemini API Key?
Go to: https://makersuite.google.com/app/apikey
Sign in → Copy your key
Paste it in the app.py file

---

Live Demo
Example: Click to Try

---
Purpose
This tool was created to assist students in identifying suitable scholarships and programs without needing to manually search or use paid APIs.
It demonstrates how GenAI models can be integrated into simple real-world applications.

Contact
Megha Shindhe
www.linkedin.com/in/meghashindhe
