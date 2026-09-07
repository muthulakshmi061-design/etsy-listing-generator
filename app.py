import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Page Config
st.set_page_config(page_title="Etsy SEO Listing Generator", layout="wide")

st.title("🛍️ Etsy SEO Listing Generator with Image Analysis")
st.write("Etsy-யின் புதிய விதிகள் மற்றும் கட்டுப்பாடுகளுக்கு ஏற்ப SEO-Optimized லிஸ்டிங் தரவுகளை உருவாக்கவும்.")

# Sidebar - API Key and Inputs
with st.sidebar:
    st.header("📋 Product Details & Image / உள்ளீடுகள்")
    
    api_key = st.text_input("Gemini API Key (Optional if set in environment)", type="password")
    if api_key:
        genai.configure(api_key=api_key)
    elif "GEMINI_API_KEY" in os.environ:
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    uploaded_file = st.file_uploader("Upload Product Image / தயாரிப்புப் படத்தை பதிவேற்றவும்", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image Preview", use_container_width=True)

    product_name = st.text_input("Product Name / பொருளின் பெயர்", "Football Theme Birthday Invitation")
    niche_theme = st.text_input("Niche / Theme / Occasion", "Football / Soccer Theme Birthday Party")
    editing_platform = st.selectbox("Editing Platform", ["Canva", "Corjl", "Templett", "Photoshop", "PDF/Non-editable"])
    dimensions = st.text_input("Dimensions / Sizes", "5x7 inches (Invitation), 1080x1920px (Mobile Evite)")
    recipient_age = st.text_input("Target Audience / Recipient / Age", "Kids, Boys, Toddlers, Parents, Party Planners")
    included_items = st.text_area("Included Items", "Editable 5x7 Invitation Template, Mobile Electronic Evite, Canva Access PDF Guide")
    
    generate_btn = st.button("✨ Generate Detailed Etsy Listing")

# Main Content Area
if generate_btn:
    if not uploaded_file and not product_name:
        st.error("Please upload an image or fill in the product details.")
    else:
        with st.spinner("Analyzing image and generating ultra-detailed Etsy listing..."):

            # Highly detailed prompt covering every single requirement
            prompt = f"""
            You are an expert Etsy SEO and Digital Product Copywriter. 
            Create an extremely detailed, highly structured, professional, and conversion-focused Etsy Listing Description based on the provided image and inputs.

            PRODUCT INPUT DETAILS:
            - Product Name: {product_name}
            - Niche / Theme / Occasion: {niche_theme}
            - Editing Platform: {editing_platform}
            - Dimensions / Size: {dimensions}
            - Target Audience / Recipient / Age Group: {recipient_age}
            - Included Items: {included_items}

            OUTPUT REQUIREMENTS:

            1. OPTIMIZED TITLE (Strictly under 140 characters):
               High-search-volume keywords separated by commas or vertical bars.

            2. ETSY SEO TAGS:
               Exactly 13 tags, each strictly under 20 characters, comma-separated.

            3. ULTRA-DETAILED LISTING DESCRIPTION:
               Structure the description using bold headings, clean bullet points, and clear sections as follows:

               - 🎉 PRODUCT OVERVIEW & OCCASION / THEME:
                 Highlight the event/occasion, design style, and ideal recipient/age group.

               - 📐 DIMENSIONS & FORMAT:
                 Specify precise template dimensions, file formats (PDF, JPG, PNG), and digital download delivery type.

               - 📦 WHAT IS INCLUDED:
                 Itemize every template, size, mobile/digital version, and instruction PDF included in the purchase.

               - 🎨 EDITABLE vs. FIXED ELEMENTS:
                 - What CAN be edited: (e.g., text, font style, font size, text color, background color, photo placement if applicable).
                 - What CANNOT be edited: (e.g., fixed graphics, artwork, overall layout size/orientation).

               - 💻 EDITING PLATFORM & DEVICE COMPATIBILITY:
                 Detail the software required ({editing_platform}), account type needed (e.g., Free or Pro), and supported devices (Computer/Laptop recommended, Tablet/Mobile capability).

               - ⏳ ACCESS DURATION & USAGE:
                 Lifetime access, unlimited edits and downloads for personal use.

               - 🖨️ RECOMMENDED PAPER & PRINTING TIPS:
                 Best paper type (e.g., Heavyweight Cardstock 100lb+, Glossy/Matte finishes), printing options (Home printer, Local print shop, Online printing services).

               - 🚀 HOW IT WORKS (STEP-BY-STEP):
                 1. Purchase & Instant Access
                 2. Open PDF Guide with Template Links
                 3. Edit in {editing_platform}
                 4. Save/Download (PDF for print, JPG/PNG for digital sending)
                 5. Print or send digitally!

               - ⚠️ TERMS OF USE & REFUND POLICY:
                 Personal use only, no resale/redistribution, digital nature policy (no physical item shipped, no returns/refunds).

            4. NOTE TO BUYERS (Digital Delivery Instructions).
            """

            try:
                # Using Gemini Vision model
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                if uploaded_file:
                    response = model.generate_content([prompt, image])
                else:
                    response = model.generate_content(prompt)
                    
                st.markdown(response.text)

            except Exception as e:
                st.error(f"Error generating listing: {e}")
