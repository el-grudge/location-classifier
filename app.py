import streamlit as st
from PIL import Image
import requests
import boto3

# Load secrets from secrets.toml
url = st.secrets["aws"]["url_2"]
s3_bucket_name = st.secrets["aws"]["s3_bucket_name"]
image_url = st.secrets["aws"]["image_url"]

st.title("Location Classifier App")

st.header('Upload an image of your location')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"],
                                 help="Upload a street-level view from one of these cities: Cairo, Paris, Moscow")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, use_column_width=False, width=300)

    # Save the image to a file
    image.save("temp.jpg", format="JPEG")

    s3 = boto3.client('s3',
            aws_access_key_id=st.secrets["aws"]["ACCESS_ID"],
            aws_secret_access_key=st.secrets["aws"]["ACCESS_KEY"])
    with open("temp.jpg", "rb") as data:
        s3.upload_fileobj(data, f'{s3_bucket_name}', 'myimage.jpg', ExtraArgs={'ACL': 'public-read'})

    # Now 'myimage.jpg' is accessible
    img_url = f'{image_url}'

    # Send the image URL as JSON data
    result = requests.post(url, json={"url": img_url})
    
    # Including the variable in the text using f-string formatting
    last_line = f"<span style='font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif; font-style: italic; font-size:24px;'>Where am I? {result.json()}</span>."
    st.markdown(last_line, unsafe_allow_html=True)