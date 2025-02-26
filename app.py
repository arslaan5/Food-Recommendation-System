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
submit_btn = st.button("Search")

if submit_btn:
    st.markdown("### Recommendations:")

    # Assuming 'recommendations' is a DataFrame with 'name' and 'imgurl' columns
    recommendations = recommend_dishes(title)
    cols = st.columns(3, gap='medium', border=True, vertical_alignment='bottom')  # Creates 3 columns
    
    try:
        with st.spinner("Searching...", show_time=True):
            for i, (index, row) in enumerate(recommendations.iterrows()):
                with cols[i % 3]:  # Distribute images across columns
                    st.markdown(
                        f"""
                        <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                            <img src="{row['imgurl']}" style="width: 100%; height: 180px; object-fit: cover; border-radius: 10px;">
                            <div style="height: 80px; display: flex; align-items: center; justify-content: center; margin-top: 12px; margin-bottom: 12px;">
                                <p style="font-weight: bold; font-size: 1.1rem; margin: 8px; padding: 4px; text-align: center;">{row['name']}</p>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        st.success("Search succesfull!", icon="✔️")
    except:
        st.error("Unable to retrieve information.", icon="❌")
