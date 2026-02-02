import streamlit as st
import numpy as np
import pandas as pd
import io
from PyPDF2 import PdfReader

# Title of the app
st.title("Optimal Investment And Reinsurance Policies In Insurance Markets Under The Effects Of Inside Information")

# Collect basic information
name = "Manenzhe Lucky"
field = "Applied Mathematics"
institution = "University of Limpopo"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Image - consider using a relative path or uploading
# Option 1: Keep as is (but may not work in deployment)
try:
    st.image(
        "C:/Users/Lucky Manenzhe/Downloads/Streamlit_2026/Screenshot_20260131_213121_Google.jpg",
        caption="Business Insurance Platform for SMEs"
    )
except FileNotFoundError:
    st.warning("Image file not found. Please check the file path.")
    # Option: Add file uploader for image
    # uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    # if uploaded_image:
    #     st.image(uploaded_image, caption="Business Insurance Platform for SMEs")

# Add a section for publications
st.header("Publications")

# Upload a PDF file
uploaded_file = st.file_uploader("Upload a PDF of Publications", type="pdf")

if uploaded_file:
    try:
        pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
        num_pages = len(pdf_reader.pages)
        
        pdf_text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text() + "\n\n"
        
        st.text_area("PDF Content", pdf_text, height=400)
        st.write(f"Total pages: {num_pages}")
        st.write(f"File name: {uploaded_file.name}")
        
        keyword = st.text_input("Search in PDF", "")
        if keyword:
            if keyword.lower() in pdf_text.lower():
                st.success(f"Keyword '{keyword}' found in the PDF.")
                lines = pdf_text.split("\n")
                for line in lines:
                    if keyword.lower() in line.lower():
                        st.write(line)
            else:
                st.warning(f"Keyword '{keyword}' not found.")
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
else:
    st.write("Please upload a PDF file to view its content.")

# Add Research Data Section
st.header("Research Data Analysis")

research_data = pd.DataFrame({
    "Time t": [0, 1, 2, 3, 4],
    "Optimal Investment Proportion (γ = 0.5)": [0.54, 0.58, 0.61, 0.64, 0.67],
    "Optimal Investment Proportion (γ = 0.55)": [0.49, 0.52, 0.55, 0.58, 0.60],
    "Optimal Investment Proportion (γ = 0.6)": [0.46, 0.48, 0.50, 0.52, 0.54],
    "Optimal Reinsurance Proportion (γ = 0.5)": [0.44, 0.46, 0.48, 0.50, 0.52],
    "Optimal Reinsurance Proportion (γ = 0.55)": [0.42, 0.44, 0.46, 0.48, 0.50],
    "Optimal Reinsurance Proportion (γ = 0.6)": [0.40, 0.42, 0.44, 0.46, 0.48]
})

st.subheader("Optimal Investment and Reinsurance Strategies Over Time")
st.write("**Table: Effect of Risk Aversion (γ) on Optimal Strategies**")
st.dataframe(research_data)

# Add charts for better visualization
st.subheader("Visualization of Strategies")

# Investment chart
st.write("**Investment Proportions Over Time**")
investment_data = research_data[["Time t", 
                                 "Optimal Investment Proportion (γ = 0.5)",
                                 "Optimal Investment Proportion (γ = 0.55)",
                                 "Optimal Investment Proportion (γ = 0.6)"]]
st.line_chart(investment_data.set_index("Time t"))

# Reinsurance chart
st.write("**Reinsurance Proportions Over Time**")
reinsurance_data = research_data[["Time t",
                                  "Optimal Reinsurance Proportion (γ = 0.5)",
                                  "Optimal Reinsurance Proportion (γ = 0.55)",
                                  "Optimal Reinsurance Proportion (γ = 0.6)"]]
st.line_chart(reinsurance_data.set_index("Time t"))

# Add analysis section
st.subheader("Data Analysis")
st.write("""
**Key Observations:**

1. **Investment Strategies:**
   - Higher risk aversion (γ) leads to lower investment in risky assets
   - All strategies show increasing investment proportions over time
   - The gap between different γ values widens as time progresses

2. **Reinsurance Strategies:**
   - Higher risk aversion leads to higher reinsurance purchasing (lower proportion retained)
   - Similar to investment, reinsurance proportions increase over time
   - The relationship appears more linear than the investment strategies

3. **Risk Aversion Impact:**
   - A 10% increase in γ (from 0.5 to 0.55) reduces investment by approximately 5-7 percentage points
   - The same increase in γ increases reinsurance purchasing by 2-3 percentage points
""")

# Add a contact section
st.header("Contact Information")
email = "manenzhelucky2@gmail.com"
st.write(f"You can reach {name} at {email}.")

