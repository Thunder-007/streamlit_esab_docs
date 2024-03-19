import os
import streamlit as st
import re
import time
from streamlit_extras.app_logo import add_logo
import streamlit_shadcn_ui as ui
import random


class Document:
    def __init__(self, name, type):
        self.document_id = random.randint(100000, 999999)
        self.document_name = name
        self.type = type


documents = [Document("Renegade VOLT ES 200i", "User manual"), Document("Rebel EMP 205ic", "Hand book"),
             Document("Warrior EDGE 500 DX", "Installation document"), ]

st.sidebar.image("esab_logo.png", width=160, )
manual_type = st.sidebar.multiselect("Manual Type", options=["ALL", "ACCESSORIES", "HANDBOOK", ], )
category = st.sidebar.multiselect("Category",
                                  options=["ALL", "ARC GOUGING", "ARC WELDING", "DIGITAL SOLUTION", "GAS EQUIPMENT"], )
region = st.sidebar.multiselect("Region", options=["ALL", "Asia and Pacific", "Australia", "Middle East and Africa",
                                                   "North America"], )
language = st.sidebar.multiselect("Language",
                                  options=["ALL", "Arabic", "Chinese", "English", "French", "German", "Italian",
                                           "Japanese", "Korean", "Portuguese", "Russian", "Spanish"], )
st.sidebar.markdown("---")
sort_by = st.sidebar.selectbox("Sort By", options=["Release Date", "Relevance", "Product Name"], )
search_bar = st.text_input("Search")

if search_bar:
    # loading animation for 3 seconds
    with st.spinner("Searching..."):
        time.sleep(1)
    for index, document in enumerate(documents):
        ui.metric_card(title=f"Document No: {document.document_id}", content=f"{document.document_name}",
                       description=f"Type: {document.type} Date: 13-03-2003 Serial number: OP137 Article No 04406300880",
                       key=f"card{index}")
