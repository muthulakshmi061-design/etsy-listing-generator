import streamlit as st

st.set_page_config(page_title="Etsy Digital Product Listing Generator", page_icon="🛍️", layout="wide")

st.title("🛍️ Etsy SEO Listing Generator (Digital Products)")
st.markdown("Etsy-யின் புதிய அல்காரிதம் மற்றும் கட்டுப்பாடுகளுக்கு (Rules & Limits) ஏற்ப SEO-Optimized லிஸ்டிங் தரவுகளைத் தானாக உருவாக்கவும்.")

# Sidebar Inputs
st.sidebar.header("⚙️ Product Details / உள்ளீடுகள்")

product_name = st.sidebar.text_input("Product Name / பொருளின் பெயர்", "Floral Kids Birthday Invitation")
niche = st.sidebar.text_input("Niche / Theme", "Boho Floral Girl Birthday")
editing_platform = st.sidebar.selectbox("Editing Platform", ["Canva", "Corjl", "Templett", "Photoshop", "PDF / Printable"])
included_items = st.sidebar.text_area("Included Items & Sizes", "5x7 inch Invitation Template, Access Guide PDF")
target_audience = st.sidebar.text_input("Target Audience / Recipient", "Parents, Moms, Party Planner")

generate_btn = st.sidebar.button("🚀 Generate Etsy Listing", type="primary")

def generate_etsy_data(p_name, p_niche, p_platform, p_items, p_audience):
    # Title Rule: Max 140 chars
    title_raw = f"Editable {p_name}, {p_niche} Party Invite, Printable {p_audience} Download, {p_platform} Template"
    title = title_raw[:140]
        
    # Tags Rule: Exactly 13 tags, each <= 20 chars
    tags_pool = [
        f"{p_platform.lower()} template"[:20],
        f"editable {p_name.split()[0].lower()}"[:20],
        "digital download",
        "instant download",
        "printable invite",
        "birthday invite",
        f"{p_niche.split()[0].lower()} birthday"[:20],
        "party template",
        "custom invitation",
        "diy invitation",
        "event template",
        "digital invite",
        "stationery template"
    ]
    
    final_tags = []
    for tag in tags_pool:
        clean_tag = tag.strip()[:20]
        if clean_tag not in final_tags:
            final_tags.append(clean_tag)
    while len(final_tags) < 13:
        final_tags.append("printable card"[:20])
    
    # Description
    desc_first_lines = f"Create a stunning, fully customizable {p_name.lower()} in minutes! Perfect for {p_niche.lower()} celebrations using {p_platform}.\n\n"
    
    desc_body = f"""✨ WHAT IS INCLUDED ✨
- {p_items}
- High-resolution digital files

🛠️ HOW IT WORKS 🛠️
1. Purchase the listing on Etsy.
2. Download the attached PDF/Instructions file.
3. Access your template via {p_platform} and edit text, colors, or fonts!
4. Save, download as PDF/JPG, and print at home or at a local shop.

✏️ EDITABLE ELEMENTS ✏️
- All wording, font style, font color, and layout placement are editable.

⚠️ IMPORTANT NOTES ⚠️
- This is a DIGITAL DOWNLOAD item. No physical item will be shipped.
- For personal use only. Commercial resale is strictly prohibited.
"""
    full_description = desc_first_lines + desc_body
    
    # Note to buyers
    note_to_buyers = f"Thank you so much for your purchase! Your digital {p_name.lower()} files and access links are ready to download. Open the PDF file attached to access your {p_platform} template links and editing guide."

    return title, final_tags, full_description, note_to_buyers

if generate_btn:
    title, tags, description, note_to_buyers = generate_etsy_data(
        product_name, niche, editing_platform, included_items, target_audience
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📌 Title (1-140 Chars)")
        st.code(title, language=None)
        st.caption(f"Character Count: {len(title)} / 140")

        st.subheader("🏷️ 13 Etsy Tags (Strictly Max 20 Chars Each)")
        tag_str = "\n".join([f"{i+1}. {tag} ({len(tag)} chars)" for i, tag in enumerate(tags)])
        st.code(tag_str, language=None)

        st.subheader("📩 Note to Buyers (Digital Files)")
        st.code(note_to_buyers, language=None)

    with col2:
        st.subheader("📝 Description (SEO First 2 Lines Optimized)")
        st.code(description, language=None)
