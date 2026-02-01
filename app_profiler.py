import streamlit as st
import pandas as pd
import numpy as np
#import io
import matplotlib.pyplot as plt
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

st.image(
    "C:/Users/Lucky Manenzhe/Downloads/Screenshot_20260131_213121_Google.jpg",
    caption="Business Insurance Platform for SMEs"
)

# Add a section for publications
st.header("Publications")

# Upload a PDF file
uploaded_file = st.file_uploader("Upload a PDF of Publications", type="pdf")

if uploaded_file:
    # Read PDF content
    pdf_reader = pdf_reader(io.BytesIO(uploaded_file.read()))
    num_pages = len(pdf_reader.pages)
    
    # Extract text from each page
    pdf_text = ""
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text() + "\n\n"
    
    # Display PDF text in a scrollable box
    st.text_area("PDF Content", pdf_text, height=400)
    
    # Optionally display metadata or a preview
    st.write(f"Total pages: {num_pages}")
    st.write(f"File name: {uploaded_file.name}")
    
    # Option: Allow keyword search within the PDF text
    keyword = st.text_input("Search in PDF", "")
    if keyword:
        if keyword.lower() in pdf_text.lower():
            st.success(f"Keyword '{keyword}' found in the PDF.")
            # Highlight or show context around keyword
            lines = pdf_text.split("\n")
            for line in lines:
                if keyword.lower() in line.lower():
                    st.write(line)
        else:
            st.warning(f"Keyword '{keyword}' not found.")
else:
    st.write("Please upload a PDF file to view its content.")
# Add Research Data Section
st.header("Research Data Analysis")

# Create the dataframe from your table data
research_data = pd.DataFrame({
    "Time t": [0, 1, 2, 3, 4],
    "Optimal Investment Proportion (γ = 0.5)": [0.54, 0.58, 0.61, 0.64, 0.67],
    "Optimal Investment Proportion (γ = 0.55)": [0.49, 0.52, 0.55, 0.58, 0.60],
    "Optimal Investment Proportion (γ = 0.6)": [0.46, 0.48, 0.50, 0.52, 0.54],
    "Optimal Reinsurance Proportion (γ = 0.5)": [0.44, 0.46, 0.48, 0.50, 0.52],
    "Optimal Reinsurance Proportion (γ = 0.55)": [0.42, 0.44, 0.46, 0.48, 0.50],
    "Optimal Reinsurance Proportion (γ = 0.6)": [0.40, 0.42, 0.44, 0.46, 0.48]
})

# Display the data table
st.subheader("Optimal Investment and Reinsurance Strategies Over Time")
st.write("**Table: Effect of Risk Aversion (γ) on Optimal Strategies**")
st.dataframe(research_data)

# Create two columns for the plots
col1, col2 = st.columns(2)

# Plot 1: Optimal Investment Proportions
with col1:
    st.subheader("Optimal Investment Proportions")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    
    # Plot lines for different gamma values
    ax1.plot(research_data["Time t"], research_data["Optimal Investment Proportion (γ = 0.5)"], 
             marker='o', label='γ = 0.5', linewidth=2)
    ax1.plot(research_data["Time t"], research_data["Optimal Investment Proportion (γ = 0.55)"], 
             marker='s', label='γ = 0.55', linewidth=2)
    ax1.plot(research_data["Time t"], research_data["Optimal Investment Proportion (γ = 0.6)"], 
             marker='^', label='γ = 0.6', linewidth=2)
    
    ax1.set_xlabel('Time (t)', fontsize=12)
    ax1.set_ylabel('Investment Proportion', fontsize=12)
    ax1.set_title('Optimal Investment Strategy by Risk Aversion', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim([0.4, 0.7])
    
    st.pyplot(fig1)

# Plot 2: Optimal Reinsurance Proportions
with col2:
    st.subheader("Optimal Reinsurance Proportions")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    
    # Plot lines for different gamma values
    ax2.plot(research_data["Time t"], research_data["Optimal Reinsurance Proportion (γ = 0.5)"], 
             marker='o', label='γ = 0.5', linewidth=2)
    ax2.plot(research_data["Time t"], research_data["Optimal Reinsurance Proportion (γ = 0.55)"], 
             marker='s', label='γ = 0.55', linewidth=2)
    ax2.plot(research_data["Time t"], research_data["Optimal Reinsurance Proportion (γ = 0.6)"], 
             marker='^', label='γ = 0.6', linewidth=2)
    
    ax2.set_xlabel('Time (t)', fontsize=12)
    ax2.set_ylabel('Reinsurance Proportion', fontsize=12)
    ax2.set_title('Optimal Reinsurance Strategy by Risk Aversion', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim([0.35, 0.55])
    
    st.pyplot(fig2)

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

# Add interactive controls for data exploration
st.subheader("Interactive Data Exploration")

# Select which γ value to focus on
gamma_option = st.selectbox(
    "Select Risk Aversion Level (γ) for detailed view:",
    ["γ = 0.5", "γ = 0.55", "γ = 0.6"]
)

# Filter data for selected gamma
gamma_suffix = gamma_option.split("= ")[1]
investment_col = f"Optimal Investment Proportion (γ = {gamma_suffix})"
reinsurance_col = f"Optimal Reinsurance Proportion (γ = {gamma_suffix})"

# Create comparison plot
fig3, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 4))

# Investment plot
ax3.plot(research_data["Time t"], research_data[investment_col], 
         marker='o', color='blue', linewidth=2)
ax3.set_xlabel('Time (t)')
ax3.set_ylabel('Investment Proportion')
ax3.set_title(f'Investment Strategy: {gamma_option}')
ax3.grid(True, alpha=0.3)
ax3.set_ylim([0.4, 0.7])

# Reinsurance plot
ax4.plot(research_data["Time t"], research_data[reinsurance_col], 
         marker='s', color='red', linewidth=2)
ax4.set_xlabel('Time (t)')
ax4.set_ylabel('Reinsurance Proportion')
ax4.set_title(f'Reinsurance Strategy: {gamma_option}')
ax4.grid(True, alpha=0.3)
ax4.set_ylim([0.35, 0.55])

st.pyplot(fig3)

# Add a contact section
st.header("Contact Information")
email = "manenzhelucky2@gmail.com"
st.write(f"You can reach {name} at {email}.")
