import streamlit as st
import requests

# 1. Page Config aur Title Set Karna
st.set_page_config(page_title="MyAllie AI Doubt Solver", page_icon="🎓")
st.title("🎓 MyAllie: AI Doubt Solver Bot")
st.write("Apna Math ya Physics ka sawaal niche likhiye aur step-by-step solution paiye!")

try:
    # Secrets se key nikalna
    api_key = st.secrets["GEMINI_API_KEY"]

    user_question = st.text_area("Yahan apna sawaal type karein:", placeholder="Example: 4+5")

    if st.button("Solve My Doubt ✨"):
        if user_question:
            with st.spinner("🔄 MyAllie Answer Generate Kar Raha Hai..."):
                prompt_text = f"""
                Aap ek India ke top coaching institute (jaise Allen/IIT-JEE) ke expert teacher hain.
                Aapka naam 'MyAllie Bot' hai. User ke question ka answer in steps me dein:
                1. 🧠 **Concept Used**: Pehle batayein kaun sa formula ya concept lagega.
                2. 📝 **Step-by-Step Solution**: Poori calculation aasan shabdo me Hinglish me samjhayein.
                3. ✅ **Final Answer**: Last me answer ko ek box me ya bold karke dikhayein.

                Question: {user_question}
                """
                
                # Direct Google API Endpoint for 2026 models
                url = f"https://googleapis.com{api_key}"
                
                # Sateek headers jo AQ. key format ko accept karwate hain
                headers = {'Content-Type': 'application/json'}
                
                # Data payload structure
                data = {
                    "contents": [{
                        "parts": [{"text": prompt_text}]
                    }]
                }
                
                # Direct API Call
                response = requests.post(url, headers=headers, json=data)
                result_json = response.json()
                
                # Check performance and show output
                if response.status_code == 200:
                    answer = result_json['candidates'][0]['content']['parts'][0]['text']
                    st.success("🎯 Solution Mil Gaya!")
                    st.markdown(answer)
                else:
                    # Agar abhi bhi koi error aaye toh detail me print karein
                    st.error(f"Google Server Error ({response.status_code}): {result_json.get('error', {}).get('message', 'Unknown Error')}")
        else:
            st.warning("⚠️ Kripya pehle box me koi sawaal toh likhiye!")

except Exception as e:
    st.error(f"🔒 Setup Error: {e}")
    
