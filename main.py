import numpy as np
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Page Title And Configuration
st.set_page_config(page_title='Chest X-ray Detection.', page_icon='🫁', layout='wide')
st.title('Chest X-ray Detection🫁')


# SideBar Section
st.sidebar.subheader("Upload Image")
file_uploader = st.sidebar.file_uploader('Upload The Image', type=['jpg', 'png', 'jpeg'])

if 'model' not in st.session_state:
    st.session_state.model = YOLO('./models/model_yolo-v1.pt')


if file_uploader:
    try:
        with st.spinner("Waiting for the prediction..."):
            st.subheader("Model output")
            image = Image.open(file_uploader)
            results = st.session_state.model.predict(image)
            names_dict = results[0].names
            probs = results[0].probs.data.tolist()


        st.info(f'Prediction: {names_dict[np.argmax(probs)]} | Probability:  {round(np.max(probs) * 100, 3)}%', icon='🤖')
        st.image(image, caption='Output Image', width=550)

    except: st.info('Pleases Enter The Correct Image.')