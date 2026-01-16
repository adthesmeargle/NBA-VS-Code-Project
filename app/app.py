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

<<<<<<< HEAD
### Check Jan 2026 Model in google drive for the process to get the mvp_0126 df
mvp_0126_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0126.csv'))
=======
>>>>>>> origin/main
mvp_0425_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0425.csv'))
mvp_0325_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0325.csv'))
mvp_0225_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0225.csv'))
mvp_0125_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'../app' + '/mvp_0125.csv'))


# Update the DataFrame to use fully resolved paths (still relative-based!)
<<<<<<< HEAD
mvp_0126_df["headshot_path"] = mvp_0126_df["headshot_path"].apply(resolve_relative_path)
=======
>>>>>>> origin/main
mvp_0425_df["headshot_path"] = mvp_0425_df["headshot_path"].apply(resolve_relative_path)
mvp_0325_df["headshot_path"] = mvp_0325_df["headshot_path"].apply(resolve_relative_path)
mvp_0225_df["headshot_path"] = mvp_0225_df["headshot_path"].apply(resolve_relative_path)
mvp_0125_df["headshot_path"] = mvp_0125_df["headshot_path"].apply(resolve_relative_path)

# Add image objects to new column
<<<<<<< HEAD
mvp_0126_df["headshot_image"] = mvp_0126_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)
=======
>>>>>>> origin/main
mvp_0425_df["headshot_image"] = mvp_0425_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)
mvp_0325_df["headshot_image"] = mvp_0325_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)
mvp_0225_df["headshot_image"] = mvp_0225_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)
mvp_0125_df["headshot_image"] = mvp_0125_df["headshot_path"].apply(lambda path: Image.open(path) if os.path.exists(path) else None)



# Set default page
if "page" not in st.session_state:
<<<<<<< HEAD
    st.session_state.page = "jan 2026"
=======
    st.session_state.page = "apr"
>>>>>>> origin/main


# Page navigation
def go_to(page):
    st.session_state.page = page

# Buttons for navigation
<<<<<<< HEAD
st.sidebar.button("Jan 2026", on_click=go_to, args=("jan 2026",))
st.sidebar.button("Apr 2025", on_click=go_to, args=("apr 2025",))
st.sidebar.button("Mar 2025", on_click=go_to, args=("mar 2025",))
st.sidebar.button("Feb 2025", on_click=go_to, args=("feb 2025",))
st.sidebar.button("Jan 2025", on_click=go_to, args=("jan 2025",))

# Render page content
if st.session_state.page == "jan 2026":
    st.title("January MVP Predictions 2026")

    # Create table header
    cols = st.columns([1, 2, 1, 2])  # Widths of columns: Image, Player, Team, Predicted MVP Votes Share
    cols[0].markdown("")
    cols[1].markdown("**Player**")
    cols[2].markdown("**Team**")
    cols[3].markdown("**Predicted MVP Votes Share**")

    # Render each row
    for _, row in mvp_0126_df.iterrows():
        cols = st.columns([1, 2, 1, 2])
        if row["headshot_image"]:
            cols[0].image(row["headshot_image"], width=80)
        else:
            cols[0].warning("Missing")
        cols[1].markdown(row["Player"])
        cols[2].markdown(row["Team"])
        cols[3].markdown(row["Predicted MVP Votes Share"])


elif st.session_state.page == "apr 2025":
=======
st.sidebar.button("Apr", on_click=go_to, args=("apr",))
st.sidebar.button("Mar", on_click=go_to, args=("mar",))
st.sidebar.button("Feb", on_click=go_to, args=("feb",))
st.sidebar.button("Jan", on_click=go_to, args=("jan",))

# Render page content
if st.session_state.page == "apr":
>>>>>>> origin/main
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


<<<<<<< HEAD
elif st.session_state.page == "mar 2025":
=======
elif st.session_state.page == "mar":
>>>>>>> origin/main
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



<<<<<<< HEAD
elif st.session_state.page == "feb 2025":
=======
elif st.session_state.page == "feb":
>>>>>>> origin/main
    st.title("February MVP Predictions 2025")

    # Create table header
    cols = st.columns([1, 2, 1, 2])  # Widths of columns: Image, Player, Team, Predicted MVP Votes Share
    cols[0].markdown("")
    cols[1].markdown("**Player**")
    cols[2].markdown("**Team**")
    cols[3].markdown("**Predicted MVP Votes Share**")

    # Render each row
    for _, row in mvp_0225_df.iterrows():
        cols = st.columns([1, 2, 1, 2])
        if row["headshot_image"]:
            cols[0].image(row["headshot_image"], width=80)
        else:
            cols[0].warning("Missing")
        cols[1].markdown(row["Player"])
        cols[2].markdown(row["Team"])
        cols[3].markdown(row["Predicted MVP Votes Share"])

<<<<<<< HEAD
elif st.session_state.page == "jan 2025":
=======
elif st.session_state.page == "jan":
>>>>>>> origin/main
    st.title("January MVP Predictions 2025")

    # Create table header
    cols = st.columns([1, 2, 1, 2])  # Widths of columns: Image, Player, Team, Predicted MVP Votes Share
    cols[0].markdown("")
    cols[1].markdown("**Player**")
    cols[2].markdown("**Team**")
    cols[3].markdown("**Predicted MVP Votes Share**")

    # Render each row
    for _, row in mvp_0125_df.iterrows():
        cols = st.columns([1, 2, 1, 2])
        if row["headshot_image"]:
            cols[0].image(row["headshot_image"], width=80)
        else:
            cols[0].warning("Missing")
        cols[1].markdown(row["Player"])
        cols[2].markdown(row["Team"])
        cols[3].markdown(row["Predicted MVP Votes Share"])


