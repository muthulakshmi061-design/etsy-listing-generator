import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Etsy SEO Generator", layout="wide")

st.title("🛍️ Fast Etsy SEO Listing Generator")

# Sidebar Configuration
with st.sidebar:
    st.header("Product Details & Inputs")
    api_key = st.text_input("Gemini API Key", type="password")
    uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])
    
    product_name = st.text_input("Product Name", "Football Theme Birthday Invitation")
    niche = st.text_input("Niche / Theme", "Football Birthday Party")
    platform = st.selectbox("Editing Platform", ["Canva", "Photoshop", "Illustrator", "Other"])
    dimensions = st.text_input("Dimensions / Sizes", "5x7 Inches, 1080x1920px")
    target_audience = st.text_input("Target Audience", "Kids, Boys, Parents")
    included_items = st.text_input("Included Items", "Editable 5x7 Template, Evite, PDF Guide")

    generate_btn = st.button("✨ Generate Listing Instantly")

# Main Page Processing
if generate_btn:
    if not api_key:
        st.error("⚠️ Please enter a valid Gemini API Key first!")
    elif not uploaded_file:
        st.warning("⚠️ Please upload a product image.")
    else:
        try:
            # Configure Gemini API
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            image = Image.open(uploaded_file)
            
            # Prompt Engineering for High Converting Etsy Listing
            prompt = f"""
            You are an expert Etsy SEO Specialist. Analyze this product image and generate a complete listing based on the details below:
            - Product Name: {product_name}
            - Niche/Theme: {niche}
            - Platform: {platform}
            - Dimensions: {dimensions}
            - Target Audience: {target_audience}
            - Included Items: {included_items}

            Provide the output in the following structure:
            1. **Optimized Etsy Title** (Max 140 chars, high search volume keywords)
            2. **13 High-Traffic Tags** (Comma-separated)
            3. **Engaging Product Description** (Including features, how it works, and usage details)
            4. **Suggested Price Range ($)**
            """

            with st.spinner("Analyzing image and generating Etsy SEO data..."):
                response = model.generate_content([prompt, image])
                
            st.success("✅ Listing Generated Successfully!")
            st.markdown("### 📝 Generated Listing Result")
            st.write(response.text)

        except Exception as e:
            st.error(f"🚨 An error occurred: {str(e)}")
