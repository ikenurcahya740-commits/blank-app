import streamlit as st

st.title("🎈 Cahya's gallery")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
) 
import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
import streamlit as st

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
