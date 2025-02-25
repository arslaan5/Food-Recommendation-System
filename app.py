from src.main import recommend_dishes
import streamlit as st


# Heading
st.title("Food Recommender System:curry:")

# Description
st.header("Get recommendations for food dishes around your input.", divider='blue')

# Feature
st.markdown("### Multiple Searching Options.")
st.markdown("1. Search by **cuisine**. (e.g. 'Indian', 'American', 'Pakistani' etc.)")
st.markdown("2. Search by **course**. (e.g. 'Main Course', 'Dessert', 'Breakfast' etc.)")
st.markdown("3. Search by **food dish**. (e.g. 'Biryani', 'Pizza', 'Pasta' etc.)")

title = st.text_input("Type below:", placeholder="Hungry? Get yourself something to eat!", autocomplete="off").lower()

if title:
    st.markdown("### Recommendations:")
    st.write(recommend_dishes(title))

# print(recommend_dishes("indian"))