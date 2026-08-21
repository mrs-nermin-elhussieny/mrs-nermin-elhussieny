import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

st.title("🎉 Welcome to My App")
st.write("This is a simple Streamlit application")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("What's your name?", "Guest")

# Main content
st.write(f"Hello, {name}! 👋")

# Simple counter
if "counter" not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1
with col2:
    st.write(f"Count: {st.session_state.counter}")
with col3:
    if st.button("🔄 Reset"):
        st.session_state.counter = 0

# Footer
st.divider()
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
