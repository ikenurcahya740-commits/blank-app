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
import streamlit as st

st.toast("Your edited image was saved!", icon="🙌🏻")
import time
import streamlit as st

if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    import streamlit as st

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
    st.toast("Hooray!", icon="🎉")
    import time
import streamlit as st

def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🫕")

if st.button("Cook breakfast"):
    cook_breakfast()
