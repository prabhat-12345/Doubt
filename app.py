import streamlit as st
import google.generativeai as genai
import os

# 1. Website ka layout aur naam set karna
st.set_page_config(page_title="MyAllie AI Doubt Solver", page_icon="🎓")
st.title("🎓 MyAllie: AI Doubt Solver Bot")
st.write("Apna Math ya Physics ka sawaal niche likhiye aur step-by-step solution paiye!")

try:
    # 2. API Key ko sahi tarike se system me set karna (New Method)
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
    genai.configure()

    # 3. User ke liye question input box
    user_question = st.text_area("Yahan apna sawaal type karein:", placeholder="Example: Solve x^2 - 5x + 6 = 0")

    if st.button("Solve My Doubt ✨"):
        if user_question:
            with st.spinner("🔄 MyAllie Aapka Answer Generate Kar Raha Hai..."):
                prompt = f"""
                Aap ek India ke top coaching institute (jaise Allen/IIT-JEE) ke expert teacher hain.
                Aapka naam 'MyAllie Bot' hai. User ke question ka answer in steps me dein:
                1. 🧠 **Concept Used**: Pehle batayein kaun sa formula ya concept lagega.
                2. 📝 **Step-by-Step Solution**: Poori calculation aasan shabdo me Hinglish me samjhayein.
                3. ✅ **Final Answer**: Last me answer ko ek box me ya bold karke dikhayein.

                Question: {user_question}
                """
                
                # Latest and standard model name for 2026
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                
                st.success("🎯 Solution Mil Gaya!")
                st.markdown(response.text)
        else:
            st.warning("⚠️ Kripya pehle box me koi sawaal toh likhiye!")

except Exception as e:
    st.error(f"🔒 App Setup me koi dikkat hai! Error details: {e}")
    
