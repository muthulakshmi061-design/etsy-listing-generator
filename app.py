import streamlit as st

st.set_page_config(page_title="Etsy SEO Generator with Image Upload", page_icon="🛍️", layout="wide")

st.title("🛍️ Etsy SEO Listing Generator with Image Analysis")
st.markdown("Etsy-யின் புதிய விதிகள் மற்றும் கட்டுப்பாடுகளுக்கு ஏற்ப, உங்கள் தயாரிப்புப் படத்தை பதிவேற்றம் செய்து SEO-Optimized லிஸ்டிங் தரவுகளை உருவாக்கவும்.")

# Sidebar Inputs
st.sidebar.header("📸 Product Details & Image / உள்ளீடுகள்")

# Image Upload Option
uploaded_file = st.sidebar.file_uploader("Upload Product Image / தயாரிப்புப் படத்தை பதிவேற்றவும்", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.sidebar.image(uploaded_file, caption="Uploaded Image Preview", use_container_width=True)

product_name = st.sidebar.text_input("Product Name / பொருளின் பெயர்", "Floral Kids Birthday Invitation")
niche = st.sidebar.text_input("Niche / Theme", "Boho Floral Girl Birthday")
editing_platform = st.sidebar.selectbox("Editing Platform", ["Canva", "Corjl", "Templett", "Photoshop", "PDF / Printable"])
included_items = st.sidebar.text_area("Included Items & Sizes", "5x7 inch Invitation Template, Access Guide PDF")
target_audience = st.sidebar.text_input("Target Audience / Recipient", "Parents, Moms, Party Planner")

generate_btn = st.sidebar.button("✨ Generate Etsy Listing", type="primary")

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
    desc_first_lines = f"Create a stunning, fully customizable {p_name.lower()} in minutes! Perfect for {p_niche.lower()} celebrations."
    
    desc_body = f"""
✨ WHAT IS INCLUDED ✨
- {p_items}
- High-resolution digital files

✨ HOW IT WORKS ✨
1. Purchase the listing on Etsy.
2. Download the instructions file containing your edit link.
3. Edit your design in {p_platform} using your tablet, phone, or computer.
4. Download as PDF or JPG and print at home or via professional print shop!

✨ TERMS OF USE ✨
- For personal use only. Redistribution or resale of digital files is strictly prohibited.
    """
    
    full_description = desc_first_lines + "\n" + desc_body

    # Note to Buyer
    note_to_buyer = f"Thank you for your purchase! Access your file guide link to edit your {p_name} in {p_platform}. Feel free to message us via Etsy if you need assistance!"

    return title, final_tags, full_description, note_to_buyer

if generate_btn:
    title, tags, description, note = generate_etsy_data(product_name, niche, editing_platform, included_items, target_audience)

    st.subheader("1. Optimized Title (Max 140 Characters)")
    st.code(title, language=None)
    st.caption(f"Character Count: {len(title)} / 140")

    st.subheader("2. Etsy SEO Tags (13 Tags, Max 20 Chars Each)")
    st.write(", ".join([f"`{t}`" for t in tags]))

    st.subheader("3. Listing Description")
    st.text_area("Copy Description Below", value=description, height=300)

    st.subheader("4. Note to Buyers (Digital Delivery)")
    st.info(note)
