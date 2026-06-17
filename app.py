import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DevOps Streamlit Dashboard v2",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("🚀 DevOps Streamlit Dashboard")
st.markdown("### End-to-End CI/CD Deployment using GitHub, Jenkins, Terraform, Ansible, Docker, DockerHub and AWS")

st.divider()

# Welcome Section
st.subheader("📌 Project Overview")

st.info("""
This project demonstrates a complete DevOps CI/CD pipeline.

GitHub → Jenkins → Terraform → AWS EC2 → Ansible → Docker → DockerHub → Streamlit
""")

# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Cloud", "AWS")

with col2:
    st.metric("Container", "Docker")

with col3:
    st.metric("Automation", "Ansible")

with col4:
    st.metric("CI/CD", "Jenkins")

st.divider()

# Pipeline Flow
st.subheader("⚙️ CI/CD Pipeline Flow")

pipeline = """
GitHub
   ↓
Jenkins
   ↓
Terraform
(Create AWS EC2)
   ↓
Ansible
(Install Docker)
   ↓
Docker Build
   ↓
DockerHub Push
   ↓
Ansible Deploy
   ↓
Streamlit Application Running
"""

st.code(pipeline)

st.divider()

# User Input Section
st.subheader("👤 DevOps Engineer Information")

name = st.text_input("Enter Your Name")

if name:
    st.success(f"Welcome {name} 🚀")

st.divider()

# Deployment Status
st.subheader("📊 Deployment Status")

status = st.selectbox(
    "Select Current Status",
    [
        "Code Committed",
        "Build Running",
        "Docker Image Created",
        "DockerHub Push Successful",
        "Application Deployed"
    ]
)

st.success(f"Current Status: {status}")

st.divider()

# Current Time
st.subheader("🕒 Deployment Time")

st.write(datetime.now())

st.divider()

# Footer
st.markdown(
    """
    ---
    ### ✅ Project Name: DevOps Streamlit Dashboard

    Built using:
    - Streamlit
    - Docker
    - Jenkins
    - Terraform
    - Ansible
    - AWS EC2
    - DockerHub
    """
)