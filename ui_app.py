import streamlit as st
from openai import OpenAI
from docx import Document

client = OpenAI(
    api_key="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",
    base_url="https://integrate.api.nvidia.com/v1"
)

st.title("AI Defect Resolution Generator")

defect = st.text_area("Enter Defect Details")
fix = st.text_area("Enter Fix Applied")

if st.button("Generate Report"):

    prompt = f"""
    Act as a senior hardware validation engineer.

    Defect: {defect}
    Fix: {fix}

    Generate detailed RCA report.
    """

    response = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    st.write(output)

    # 📄 Create Word file
    doc = Document()
    doc.add_heading('Defect Resolution Report', 0)
    doc.add_paragraph(output)
    doc.save("report.docx")

    # 📥 Download button
    with open("report.docx", "rb") as file:
        st.download_button(
            label="Download Report (Word)",
            data=file,
            file_name="defect_report.docx"
        )