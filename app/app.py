import streamlit as st
import pandas as pd
import os
from PIL import Image


# Get the directory this script is in
script_dir = os.path.dirname(os.path.abspath(__file__))

# Example: your headshot relative path from the script location
# (stored in your DataFrame like 'data/headshots/headshot/gilgesh01.jpg')
def resolve_relative_path(rel_path):
    return os.path.join(script_dir, rel_path)

mvp_0425_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0425.csv'))
mvp_0325_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0325.csv'))


# Update the DataFrame to use fully resolved paths (still relative-based!)
mvp_0425_df["headshot_path"] = mvp_0425_df["headshot_path"].apply(resolve_relative_path)
mvp_0325_df["headshot_path"] = mvp_0325_df["headshot_path"].apply(resolve_relative_path)


# Add image objects to new column
mvp_0425_df["headshot_image"] = mvp_0425_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)
mvp_0325_df["headshot_image"] = mvp_0325_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)



# Set default page
if "page" not in st.session_state:
    st.session_state.page = "home"


# Page navigation
def go_to(page):
    st.session_state.page = page

# Buttons for navigation
st.sidebar.button("Home", on_click=go_to, args=("home",))
st.sidebar.button("Page 1", on_click=go_to, args=("page1",))
st.sidebar.button("Page 2", on_click=go_to, args=("page2",))
st.sidebar.button("Page 3", on_click=go_to, args=("page3",))

# Render page content
if st.session_state.page == "home":
    st.title("April MVP Predictions 2025")

    # Create table header
    cols = st.columns([1, 2, 1, 2])  # Widths of columns: Image, Player, Team, Predicted MVP Votes Share
    cols[0].markdown("")
    cols[1].markdown("**Player**")
    cols[2].markdown("**Team**")
    cols[3].markdown("**Predicted MVP Votes Share**")

    # Render each row
    for _, row in mvp_0425_df.iterrows():
        cols = st.columns([1, 2, 1, 2])
        if row["headshot_image"]:
            cols[0].image(row["headshot_image"], width=80)
        else:
            cols[0].warning("Missing")
        cols[1].markdown(row["Player"])
        cols[2].markdown(row["Team"])
        cols[3].markdown(row["Predicted MVP Votes Share"])


elif st.session_state.page == "page1":
    st.title("March MVP Predictions 2025")

    # Create table header
    cols = st.columns([1, 2, 1, 2])  # Widths of columns: Image, Player, Team, Predicted MVP Votes Share
    cols[0].markdown("")
    cols[1].markdown("**Player**")
    cols[2].markdown("**Team**")
    cols[3].markdown("**Predicted MVP Votes Share**")

    # Render each row
    for _, row in mvp_0325_df.iterrows():
        cols = st.columns([1, 2, 1, 2])
        if row["headshot_image"]:
            cols[0].image(row["headshot_image"], width=80)
        else:
            cols[0].warning("Missing")
        cols[1].markdown(row["Player"])
        cols[2].markdown(row["Team"])
        cols[3].markdown(row["Predicted MVP Votes Share"])



elif st.session_state.page == "page2":
    st.title("February MVP Predictions 2025")

elif st.session_state.page == "page3":
    st.title("January MVP Predictions 2025")


