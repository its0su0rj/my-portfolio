# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J_yWvXGV25yWK3djL9g9fMo6mhAoE_z6
"""

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

# Create a sidebar with navigation links
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page",
    ["Home", "Projects", "Blog", "Contact"],
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

# Create the blog page
elif page == "Blog":
    st.title("My Blog")
    st.write("Here are some of my recent blog posts:")

    # Create a list of blog posts
    blog_posts = pd.DataFrame({
        "Title": ["Blog Post 1", "Blog Post 2", "Blog Post 3"],
        "Date": ["2022-01-01", "2022-02-01", "2022-03-01"],
        "Link": ["https://blog.username.com/post1", "https://blog.username.com/post2", "https://blog.username.com/post3"],
    })
    st.write(blog_posts)

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