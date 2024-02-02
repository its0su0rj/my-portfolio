import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set the page title and favicon
st.set_page_config(
    page_title="Coder Portfolio",
    page_icon="💻",
    layout="wide",
)

# Set the background image
st.markdown(
    """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1506744038136-4627b8c4857e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a sidebar with navigation links
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select a page",
    ["Home", "Projects", "About", "Contact"],
)

# Create the home page
if page == "Home":
    st.title("Welcome to my Portfolio!")
    st.write("I am a coder with a passion for building beautiful and innovative web applications.")
    st.write("I have experience in a variety of programming languages and technologies, including Python, JavaScript, and React.")
    st.write("I am also an active member of the open source community and have contributed to several popular projects.")

    # Create a grid of project cards
    projects = pd.DataFrame({
        "Title": ["Project 1", "Project 2", "Project 3"],
        "Description": ["A description of Project 1", "A description of Project 2", "A description of Project 3"],
        "Link": ["https://github.com/username/project1", "https://github.com/username/project2", "https://github.com/username/project3"],
    })

    col1, col2 = st.columns(2)
    with col1:
        st.write(projects.iloc[0])
    with col2:
        st.write(projects.iloc[1])

    col3, col4 = st.columns(2)
    with col3:
        st.write(projects.iloc[2])

# Create the projects page
elif page == "Projects":
    st.title("My Projects")
    st.write("Here are some of the projects I have worked on:")

    # Create a grid of project cards
    projects = pd.DataFrame({
        "Title": ["Project 1", "Project 2", "Project 3"],
        "Description": ["A description of Project 1", "A description of Project 2", "A description of Project 3"],
        "Link": ["https://github.com/username/project1", "https://github.com/username/project2", "https://github.com/username/project3"],
    })

    col1, col2 = st.columns(2)
    with col1:
        st.write(projects.iloc[0])
    with col2:
        st.write(projects.iloc[1])

    col3, col4 = st.columns(2)
    with col3:
        st.write(projects.iloc[2])

    # Create a graph for each project
    for project in projects["Title"]:
        data = pd.DataFrame({
            "Project": [project],
            "Visitors": [100, 200, 300]
        })

        fig = px.bar(data, x="Project", y="Visitors")
        st.plotly_chart(fig)

# Create the about page
elif page == "About":
    st.title("About Me")
    st.write("I am a passionate coder with a strong desire to create innovative and user-friendly web applications.")
    st.write("I have a background in computer science and have been working as a software engineer for the past 5 years.")
    st.write("I am proficient in a variety of programming languages and technologies, including Python, JavaScript, and React.")
    st.write("I am also an active member of the open source community and have contributed to several popular projects.")

# Create the contact page
elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out to me if you have any questions or would like to collaborate on a project.")

    # Create a contact form
    contact_form = st.form("Contact Form")
    name = contact_form.text_input("Your Name")
    email = contact_form.text_input("Your Email")
    message = contact_form.text_area("Your Message")
    submit_button = contact_form.form_submit_button("Send Message")

    if submit_button:
        st.write("Thank you for your message. I will get back to you as soon as possible.")


# Add a footer to the page
st.sidebar.title("Social Media")
st.sidebar.write("Follow me on social media:")
st.sidebar.write("[Github](https://github.com/username)")
st.sidebar.write("[Twitter](https://twitter.com/username)")
st.sidebar.write("[LinkedIn](https://linkedin.com/in/username)")

# Footer
st.markdown("Copyright © 2022 Coder Portfolio. All rights reserved.")
