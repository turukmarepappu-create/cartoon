import streamlit as st
import random

# Cartoon meanings dictionary (expand as you like)
cartoon_meanings = {
    "a": "Mickey Mouse – cheerful and always friendly!",
    "b": "Bugs Bunny – clever and witty.",
    "c": "Chhota Bheem – strong and kind-hearted.",
    "d": "Doraemon – helpful and futuristic.",
    "e": "Elsa – magical and graceful.",
    "r": "Road Runner – super fast and energetic.",
    "n": "Nobita – simple, sometimes lazy but loveable.",
    "s": "Shinchan – mischievous and funny!",
    "t": "Tom & Jerry – playful and full of chaos!",
}

st.title("🎉 Cartoon Name Meaning Generator 🎉")
st.write("Type your name and discover your cartoon meaning!")

# Input name
name = st.text_input("Enter your name:")

if name:
    first_letter = name[0].lower()
    meaning = cartoon_meanings.get(first_letter, "Scooby Doo – loyal, funny, and always hungry!")

    st.subheader(f"Hey {name}! 👋")
    st.write(f"✨ Your cartoon meaning: **{meaning}**")

    if st.button("Generate Again"):
        meaning = random.choice(list(cartoon_meanings.values()))
        st.write(f"🎲 Another fun match: **{meaning}**")
