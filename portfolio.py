import streamlit as st

# Create a sidebar button
if st.sidebar.button('Open Sidebar Menu'):
    st.sidebar.write('Sidebar Menu Opened!')

# Create main page layout
st.title('Hello again')
st.subheader('Tell me what’s on your mind or pick a suggestion.')

# Display the logo and make it clickable to open the sidebar
if st.image("grid.png", width=50, channels="BGR", use_column_width=False):
    st.sidebar.button('Open Sidebar Menu')
