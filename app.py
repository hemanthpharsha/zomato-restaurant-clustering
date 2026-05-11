import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(page_title="Restaurant Clustering", page_icon="🍽️", layout="centered")

# Custom CSS (for professional look)
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    color: #ff4b4b;
    text-align: center;
}
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Load models
with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('pca.pkl', 'rb') as f:
    pca = pickle.load(f)

# Title
st.title("🍽️ Restaurant Clustering App")
st.caption("Smart ML-based restaurant category prediction")

# Input section (in columns)
st.subheader("🔍 Enter Restaurant Details")

col1, col2, col3 = st.columns(3)

with col1:
    rating = st.number_input("⭐ Rating", 0.0, 5.0, step=0.1)

with col2:
    votes = st.number_input("🗳️ Votes", min_value=0)

with col3:
    cost = st.number_input("💰 Cost for Two", min_value=0)

st.divider()

# Prediction
if st.button("🚀 Predict Cluster"):

    data = np.array([[rating, votes, cost]])
    data_scaled = scaler.transform(data)
    data_pca = pca.transform(data_scaled)

    cluster = kmeans.predict(data_scaled)

    # Result UI
    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader(f"📌 Predicted Cluster: {cluster[0]}")

    if cluster[0] == 0:
        st.success("💰 Budget Restaurants")
        st.write("✔ Low cost, moderate ratings")
        st.write("✔ Suitable for students & daily dining")

    elif cluster[0] == 1:
        st.success("⭐ Highly Rated Restaurants")
        st.write("✔ Excellent ratings & reviews")
        st.write("✔ Best for quality food lovers")

    elif cluster[0] == 2:
        st.success("🔥 Popular & Costly Restaurants")
        st.write("✔ High cost, high demand")
        st.write("✔ Premium dining experience")

    elif cluster[0] == 3:
        st.success("🍽️ Average Restaurants")
        st.write("✔ Balanced cost, rating & votes")
        st.write("✔ Normal casual dining")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.caption("📊 Powered by K-Means Clustering | Built with Streamlit")