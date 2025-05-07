# 🥭 Mango Leaf Disease Detection with Remedy Suggestion

A deep learning-powered web application for classifying mango leaf diseases and offering tailored remedies — built with TensorFlow and Streamlit.

## 📸 Application Preview

| Disease Detection Interface |
|----------------------------|
| ![image](https://github.com/user-attachments/assets/74d05a21-cdab-4de1-ba1d-bb45468646ed)|

> The model predicts the disease category from a user-uploaded leaf image and displays an explanation and treatment advice.

---

## 🧠 Core Features

- **Image Classification** of mango leaves into 8 categories:
  - Anthracnose
  - Bacterial Canker
  - Cutting Weevil
  - Die Back
  - Gall Midge
  - Healthy
  - Powdery Mildew
  - Sooty Mould
- **Remedy Suggestions** based on disease prediction
- Real-time image upload via **Streamlit UI**
- Uses a **pre-trained CNN model** saved in `.keras` format
- Simple **drag-and-drop UX** with animated result handling

---

## 🧱 Technologies Used

- **TensorFlow** / Keras (image classification, CNN model training)
- **Streamlit** (interactive frontend)
- **PIL** / **NumPy** (image preprocessing)
- **Python 3.8** (compatible with legacy and current TensorFlow APIs)

---

## 🚀 Getting Started

### 1. Clone and Install

```bash
git clone https://github.com/yourusername/mango-leaf-detection.git
cd mango-leaf-detection

# (Recommended) Create and activate virtual environment
conda create -n mango_tf python=3.8
conda activate mango_tf

pip install -r requirements.txt
