# 🍽️ Restaurant Clustering App

A Machine Learning based Restaurant Clustering Web Application built using **Streamlit**, **K-Means Clustering**, **PCA**, and **Scikit-learn**.

This application predicts the category/cluster of a restaurant based on:
- ⭐ Rating
- 🗳️ Number of Votes
- 💰 Approximate Cost for Two

---

## 🚀 Features

- Interactive Streamlit Web App
- Machine Learning based clustering
- User-friendly interface
- Predicts restaurant category instantly
- Professional UI design

---

## 🧠 Machine Learning Concepts Used

- K-Means Clustering
- Data Scaling using StandardScaler
- PCA (Principal Component Analysis)
- Unsupervised Learning

---

## 📂 Project Structure
├── app.py
├── kmeans_model.pkl
├── scaler.pkl
├── pca.pkl
├── Zomato.xlsx
├── requirements.txt
└── README.md

---

## 📊 Cluster Categories
Cluster	Description
0	Budget Restaurants
1	Highly Rated Restaurants
2	Popular & Costly Restaurants
3	Average Restaurants

## 📦 Required Libraries
  streamlit
  numpy
  pandas
  scikit-learn
  pickle-mixin
  openpyxl

## 📸 Application Preview
  Input:
    Restaurant Rating
    Votes
    Approx Cost for Two
Output:
    Predicted Restaurant Cluster
    Restaurant Category Description

## 📈 Dataset and Trained Model
    https://www.kaggle.com/datasets/harsha2304/zomato-restaurant-clustering

## 🎯 Future Improvements
  Add restaurant recommendation system
  Deploy using Streamlit Cloud
  Add graphical cluster visualization
  Add location-based restaurant analysis

## Conclusion

The Restaurant Clustering App successfully demonstrates the use of Machine Learning techniques to categorize restaurants based on customer ratings, votes, and cost. By applying K-Means Clustering along with data preprocessing techniques like scaling and PCA, the project provides meaningful restaurant group predictions in an interactive and user-friendly way.

This project highlights the practical implementation of unsupervised learning and showcases how data analysis can help understand restaurant patterns and customer preferences. The Streamlit interface further improves accessibility by allowing users to interact with the model in real time.
