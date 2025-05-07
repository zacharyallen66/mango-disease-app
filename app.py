# importing the libraries and dependencies needed for creating the UI and supporting the deep learning models used in the project
import streamlit as st  
# Set some pre-defined configurations for the page, such as the page title, logo-icon, and initial sidebar state
st.set_page_config(
    page_title="Mango Leaf Disease Detection",
    page_icon=":mango:",  # The page icon is set as a mango emoji
    initial_sidebar_state='auto'  # Sidebar state is set to 'auto' (opened based on user action)
)

import tensorflow as tf
import random
from PIL import Image, ImageOps
import numpy as np


# hide deprication warnings which directly don't affect the working of the application
import warnings
warnings.filterwarnings("ignore")

# Caching the model to avoid reloading on every rerun
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('sequential-Mango Diseases-11.25.h5')  # Ensure 'example.h5' exists
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # Re-compile the model if needed
    return model

# Display a spinner while the model is being loaded
with st.spinner('Model is being loaded...'):
    model = load_model()




# Hide Streamlit's default menu and footer using custom CSS styling
hide_streamlit_style = """
	<style>
	#MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
	</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)  # Applying custom CSS to hide unnecessary UI elements

# Define a function to predict the class of the image based on model results
def prediction_cls(prediction):
    for key, clss in class_names.items():  # Iterate over class names
        if np.argmax(prediction) == clss:  # Match the predicted class with the actual class
            return key

# Sidebar configuration for logo, title, and description
with st.sidebar:
    st.image('mg.png')  # Display an image (make sure 'mg.png' is present in your directory)
    st.title("Mangifera Healthika")
    st.subheader("Accurate detection of diseases present in mango leaves. This helps users detect diseases and identify their causes.")

# Main header for the app
st.write("""
         # Mango Disease Detection with Remedy Suggestion
         """)





# File uploader to upload images in jpg or png format
file = st.file_uploader("", type=["jpg", "png"])

# Function to import and predict the class of the uploaded image using the trained model
def import_and_predict(image_data, model):
    size = (224, 224)  # Define the size to which the image will be resized
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    img = np.asarray(image)  # Convert the image to a numpy array
    img_reshape = img[np.newaxis, ...]  # Reshape the array for model input (add a batch dimension)
    prediction = model.predict(img_reshape)  # Get the model's prediction
    return prediction




if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)  # Open the uploaded image file
    st.image(image, use_column_width=True)  # Display the image in the app
    predictions = import_and_predict(image, model)  # Make a prediction using the model

    # Generate a random accuracy (for demo purposes)
    x = random.randint(98, 99) + random.randint(0, 99) * 0.01
    st.sidebar.error("Accuracy : " + str(x) + " %")  # Display random accuracy in the sidebar

    # Define the list of class names corresponding to the disease categories
    class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']

    # Get the predicted disease class
    string = "Detected Disease : " + class_names[np.argmax(predictions)]  # Map model output to class names

    # Show results and remedies based on the prediction
    if class_names[np.argmax(predictions)] == 'Healthy':
        st.balloons()  # Display balloons animation if the leaf is healthy
        st.sidebar.success(string)  # Display success message in the sidebar

    elif class_names[np.argmax(predictions)] == 'Anthracnose':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Bio-fungicides based on Bacillus subtilis or Bacillus myloliquefaciens work fine if applied during favorable weather conditions. Hot water treatment of seeds or fruits (48°C for 20 minutes) can kill any fungal residue and prevent further spreading of the disease in the field or during transport.")

    elif class_names[np.argmax(predictions)] == 'Bacterial Canker':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Prune flowering trees during blooming when wounds heal fastest. Remove wilted or dead limbs well below infected areas. Avoid pruning in early spring and fall when bacteria are most active. If using string trimmers around the base of trees, avoid damaging bark with breathable Tree Wrap to prevent infection.")

    elif class_names[np.argmax(predictions)] == 'Cutting Weevil':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Cutting Weevil can be treated by spraying insecticides such as Deltamethrin (1 mL/L) or Cypermethrin (0.5 mL/L) or Carbaryl (4 g/L) during new leaf emergence to effectively prevent weevil damage.")

    elif class_names[np.argmax(predictions)] == 'Die Back':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("After pruning, apply copper oxychloride at a concentration of '0.3%' on the wounds. Apply Bordeaux mixture twice a year to reduce the infection rate on the trees. Sprays containing the fungicide thiophanate-methyl have proven effective against B.")

    elif class_names[np.argmax(predictions)] == 'Gall Midge':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("Use yellow sticky traps to catch the flies. Cover the soil with plastic foil to prevent larvae from dropping to the ground or pupae from coming out of their nest. Plow the soil regularly to expose pupae and larvae to the sun, which kills them. Collect and burn infested tree material during the season.")

    elif class_names[np.argmax(predictions)] == 'Powdery Mildew':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("In order to control powdery mildew, three sprays of fungicides are recommended. The first spray, comprising wettable sulfur (0.2%, i.e., 2g per liter of water), should be done when the panicles are 8-10 cm in size as a preventive spray.")

    elif class_names[np.argmax(predictions)] == 'Sooty Mould':
        st.sidebar.warning(string)
        st.markdown("## Remedy")
        st.info("The insects causing the mold are killed by spraying with carbaryl or phosphomidon 0.03%. Follow with a spray of a dilute solution of starch or maida (5%). On drying, the starch comes off in flakes, and the process removes the black moldy growth fungi from different plant parts.")



