import cv2
import streamlit as st
import numpy as np


def canny_filter(image, t_lower, t_upper):
    canny_output = cv2.Canny(image, t_lower, t_upper)
    return canny_output


def main_loop():
    st.title("OpenCV Canny Fliter App")
    st.subheader("This app allows you to play with Canny filter!")
    
    st.sidebar.header('Input Parameters for Canny flter')		
	
    # Lower Threshold
    t_lower = st.sidebar.slider("Lower Threshold", min_value=0, max_value=255, value=50)
    
    # Upper Threshold
    t_upper = st.sidebar.slider("Upper Threshold", min_value=0, max_value=255, value=100)
    
    uploaded_file = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])
    

    if uploaded_file is not None:
       # Convert the file to an opencv image.
       file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
       original_image = cv2.imdecode(file_bytes, 1)
       image_gray = cv2.imdecode(file_bytes, 0)

       #Image Resizing
       original_image = cv2.resize(original_image, (970, 780),interpolation = cv2.INTER_LINEAR)
       image_gray = cv2.resize(image_gray, (970, 780),interpolation = cv2.INTER_LINEAR)

       eq_image = cv2.equalizeHist(image_gray)  #Equalized histogram image
    
       processed_image = canny_filter(eq_image, t_lower, t_upper)
       
       st.text("Original Image vs Processed Image")
       st.image(original_image, channels="BGR")
       st.image(processed_image) 


if __name__ == '__main__':
    main_loop()