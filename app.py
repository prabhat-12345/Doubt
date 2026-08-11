import streamlit as st
import requests

# 1. Page Configuration aur Title
st.set_page_config(page_title="MyAllie AI Doubt Solver", page_icon="🎓")
st.title("🎓 MyAllie: AI Doubt Solver Bot")
st.write("Apna Math ya Physics ka sawaal niche likhiye aur step-by-step solution paiye!")

try:
    # Streamlit Secrets se aapki AQ. wali key uthana
    api_key = st.secrets["GEMINI_API_KEY"]

    user_question = st.text_area("Yahan apna sawaal type karein:", placeholder="Example: 6+6")

    if st.button("Solve My Doubt ✨"):
        if user_question:
            with st.spinner("🔄 MyAllie Answer Generate Kar Raha Hai..."):
                prompt_text = f"""
                Aap ek India ke top coaching institute (jaise Allen/IIT-JEE) ke expert teacher hain.
                Aapka naam 'MyAllie Bot' hai. User ke question ka answer in steps me dein:
                1. 🧠 **Concept Used**: Pehle batayein kaun sa formula ya concept lega.
                2. 📝 **Step-by-Step Solution**: Poori calculation aasan shabdo me Hinglish me samjhayein.
                3. ✅ **Final Answer**: Last me answer ko ek box me ya bold karke dikhayein.

                Question: {user_question}
                """
                
                # --- EK DUM SAHI V1 API PATH ---
                url = "https://googleapis.com"
                
                query_params = {'key': api_key}
                headers = {'Content-Type': 'application/json'}
                
                data = {
                    "contents": [{
                        "parts": [{"text": prompt_text}]
                    }]
                }
                
                # Direct HTTP Post Request
                response = requests.post(url, headers=headers, json=data, params=query_params)
                
                # Connection success check
                if response.status_code == 200:
                    result_json = response.json()
                    answer = result_json['candidates'][0]['content']['parts'][0]['text']
                    st.success("🎯 Solution Mil Gaya!")
                    st.markdown(answer)
                else:
                    st.error(f"Google Server Error ({response.status_code}): {response.text}")
        else:
            st.warning("⚠️ Kripya pehle box me koi sawaal toh likhiye!")

except Exception as e:
    st.error(f"🔒 App Setup Error: {e}")
    
