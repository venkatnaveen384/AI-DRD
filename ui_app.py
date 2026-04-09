import streamlit as st
from openai import OpenAI

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

    Generate structured RCA report.
    """

    response = client.chat.completions.create(
        model="meta/llama3-70b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)