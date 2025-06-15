import streamlit as st

# Title
st.title("🛡️ AutoShield - Real-Time Disclaimer Injector")

# Subtitle
st.markdown("Protect yourself with automatic legal disclaimers for advisory content.")

# Text input
user_input = st.text_area("✍️ Enter your advisory message below:", height=200)

# Profession choice
context = st.selectbox("Choose your profession:", ["General", "Medical", "Legal", "Financial", "Mental Health"])

# Disclaimer based on profession
disclaimers = {
    "General": "Disclaimer: This is not formal advice. Please consult a qualified professional before taking action.",
    "Medical": "Disclaimer: This is not medical advice. Please consult your doctor before making health decisions.",
    "Legal": "Disclaimer: This does not constitute legal advice. Please consult a licensed attorney.",
    "Financial": "Disclaimer: This is not financial advice. Please consult a certified financial advisor.",
    "Mental Health": "Disclaimer: This is not a substitute for professional mental health support."
}

# Button and output
if st.button("🛡️ Inject Disclaimer"):
    if user_input.strip():
        result = f"{user_input}\n\n[{disclaimers[context]}]"
        st.success("✅ Disclaimer Injected Below:")
        st.text_area("Result:", result, height=200)
    else:
        st.warning("Please enter some text first.")
