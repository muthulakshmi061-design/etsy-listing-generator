import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

st.set_page_config(page_title="Etsy SEO Listing Generator", layout="wide")

st.title("🛍️ Fast Etsy SEO Listing Generator")

# Sidebar - API Key and Inputs
with st.sidebar:
    st.header("📋 Product Details & Inputs")
    
    api_key = st.text_input("Gemini API Key", type="password")
    if api_key:
        genai.configure(api_key=api_key)
    elif "GEMINI_API_KEY" in os.environ:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        # Compress image for faster API response
        image.thumbnail((800, 800))
        st.image(image, caption="Uploaded Image Preview", use_container_width=True)

    product_name = st.text_input("Product Name", "Football Theme Birthday Invitation")
    niche_theme = st.text_input("Niche / Theme / Occasion", "Football Birthday Party")
    editing_platform = st.selectbox("Editing Platform", ["Canva", "Corjl", "Templett", "Photoshop", "PDF/Non-editable"])
    dimensions = st.text_input("Dimensions / Sizes", "5x7 inches, 1080x1920px")
    recipient_age = st.text_input("Target Audience / Age", "Kids, Boys, Parents")
    included_items = st.text_area("Included Items", "Editable 5x7 Template, Evite, PDF Guide")
    
    generate_btn = st.button("✨ Generate Listing Instantly")

# Main Content Area
if generate_btn:
    if not uploaded_file and not product_name:
        st.error("Please upload an image or fill in product details.")
    else:
        # Prompt engineered for fast execution
        prompt = f"""
        Act as an expert Etsy SEO copywriter. Generate a detailed, high-converting listing based on these details:
        - Name: {product_name}
        - Theme/Occasion: {niche_theme}
        - Platform: {editing_platform}
        - Dimensions: {dimensions}
        - Target Audience/Age: {recipient_age}
        - Included: {included_items}

        Generate the following sections with clear bold headers and bullet points:
        1. OPTIMIZED TITLE (Under 140 chars)
        2. 13 ETSY SEO TAGS (Comma-separated, under 20 chars each)
        3. DETAILED DESCRIPTION:
           - 🎉 Product Overview & Occasion/Theme
           - 📐 Dimensions, Formats & Usage
           - 📦 Included Items
           - 🎨 Editable Elements (Text, Fonts, Photos) vs. Fixed Elements (Graphics, Background)
           - 💻 Platform ({editing_platform}) & Device Compatibility
           - ⏳ Access Duration & Personal Use License
           - 🖨️ Recommended Paper & Printing Tips (Cardstock, Home/Shop printing)
           - 🚀 How It Works (Step-by-Step 1-5)
           - ⚠️ Terms of Use & Digital Refund Policy
        4. NOTE TO BUYERS (Digital Delivery Instructions)
        """

        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # Using st.write_stream for instant streaming output
            st.subheader("📝 Generated Listing Result:")
            
            if uploaded_file:
                response = model.generate_content([prompt, image], stream=True)
            else:
                response = model.generate_content(prompt, stream=True)
            
            def stream_data():
                for chunk in response:
                    yield chunk.text

            st.write_stream(stream_data)

        except Exception as e:
            st.error(f"Error: {e}")
