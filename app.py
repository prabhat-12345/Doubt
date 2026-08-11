import streamlit as str
import os
from google import genai
from google.genai.errors import APIError

# पेज का टाइटल और सेटिंग सेट करें
st.set_page_config(page_title="MyAllie: AI Doubt Solver Bot", page_icon="🎓")

st.title("🎓 MyAllie: AI Doubt Solver Bot")
st.write("Apna Math ya Physics ka sawaal niche likhiye aur step-by-step solution paiye!")

# Streamlit Secrets या Environment Variable से API Key उठाएं
# नोट: स्थानीय परीक्षण के लिए आप सीधे स्ट्रिंग में अपनी Key भी डाल सकते हैं, जैसे: "AIzaSy..."
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

# यूजर इनपुट बॉक्स
user_query = st.text_area("Yahan apna sawaal type karein:", value="7+7")

# बटन क्लिक होने पर एक्शन
if st.button("Solve My Doubt ✨"):
    if not api_key:
        st.error("❌ API Key नहीं मिली! कृपया Streamlit Settings या Secrets में GEMINI_API_KEY सेट करें।")
    elif not user_query.strip():
        st.warning("⚠️ कृपया पहले कोई सवाल टाइप करें।")
    else:
        with st.spinner("Thinking..."):
            try:
                # नए SDK के अनुसार क्लाइंट इनिशियलाइज करें
                client = genai.Client(api_key=api_key)
                
                # सबसे तेज़ और सटीक मॉडल 'gemini-2.5-flash' का उपयोग करें
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_query
                )
                
                # रिस्पॉन्स को सफलतापूर्वक प्रदर्शित करें
                st.success("🤖 Solution:")
                st.write(response.text)
                
            except APIError as e:
                # Google API से आने वाले विशिष्ट एरर को हैंडल करें
                st.error(f"❌ Google API Error: {e.message}")
            except Exception as e:
                # अन्य किसी भी अज्ञात एरर को रोकने के लिए
                st.error(f"❌ एक अनपेक्षित एरer आया: {str(e)}")
                
