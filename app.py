import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
# Load your trained model
model = load_model(r'C:\Users\Dell 5470\Desktop\Pan Detection Using Streamlit\models\Panto.h5')  # Replace 'your_model_path.h5' with the actual path to your model file

def main():
    st.title("Pan Card Detection App")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Read the uploaded image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # Display the original image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image for prediction
        resized_image = cv2.resize(image, (128, 128))
        scaled_image = resized_image / 255.0
        reshaped_image = np.reshape(scaled_image, [1, 128, 128, 3])

        # Make prediction
        prediction = model.predict(reshaped_image)
        pred_label = np.argmax(prediction)

        # Display prediction result
        if pred_label == 1:
            st.success('Pan card detected!')
        else:
            st.warning('No Pan card detected.')

if __name__ == "__main__":
    main()


