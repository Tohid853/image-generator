import streamlit as st
import requests

key="sk_Ilv4XFZicRFa4DjIo1daXut9LZcGrC6E"

st.title("Image Generator")

prompt = st.text_input("Enter Your Prompt")

if st.button("Generate"):
        if prompt:
               with st.spinner("Generate Image"):
                       try:
                               url=(
                                       "https://gen.pollinations.ai/image/"+requests.utils.quote(prompt)
                               )
                               r = requests.get(url,
                                                headers={
                                                        "Authorization":f"Bearer {key}"
                                                } , timeout=180)
                               r.raise_for_status()
                               st.image(r.content)
                       except Exception as e:
                               st.error(e)
                        