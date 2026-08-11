import streamlit as st
from google import genai
import os

# 1. Page Config aur Title Set Karna
st.set_page_config(page_title="MyAllie AI Doubt Solver", page_icon="🎓")
st.title("🎓 MyAllie: AI Doubt Solver Bot")
st.write("Apna Math ya Physics ka sawaal niche likhiye aur step-by-step solution paiye!")

try:
    # 2. Naye tareeqe se key ko test karke client banana
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    user_question = st.text_area("Yahan apna sawaal type karein:", placeholder="Example: 3+4")

    if st.button("Solve My Doubt ✨"):
        if user_question:
            with st.spinner("🔄 MyAllie Answer Generate Kar Raha Hai..."):
                prompt = f"""
                Aap ek India ke top coaching institute (jaise Allen/IIT-JEE) ke expert teacher hain.
                Aapka naam 'MyAllie Bot' hai. User ke question ka answer in steps me dein:
                1. 🧠 **Concept Used**: Pehle batayein kaun sa formula ya concept lagega.
                2. 📝 **Step-by-Step Solution**: Poori calculation aasan shabdo me Hinglish me samjhayein.
                3. ✅ **Final Answer**: Last me answer ko ek box me ya bold karke dikhayein.

                Question: {user_question}
                """
                
                # Naye system ka ekdum tested and accurate model code
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("🎯 Solution Mil Gaya!")
                st.markdown(response.text)
        else:
            st.warning("⚠️ Kripya pehle box me koi sawaal toh likhiye!")

except Exception as e:
    st.error(f"🔒 Setup Error: {e}")
    
