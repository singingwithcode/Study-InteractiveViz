# pip install streamlit seaborn matplotlib pandas joypy
# streamlit run sampleStatic.py

# Data: https://www.geeksforgeeks.org/seaborn-datasets-for-data-science/

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set up Streamlit app
st.title("Static Visualizations with Penguins Dataset")

# Load dataset
@st.cache_data
def load_data():
    return sns.load_dataset('penguins')

penguins = load_data()

# List of visualizations
visualizations = [
    "Scatter Plot",
    "Line Plot",
    "Histogram",
    "Box Plot",
    "Violin Plot",
    "Bar Plot",
    "Count Plot",
    "Heatmap",
    "Pair Plot",
    "KDE Plot",
    "Ridge Plot",
    "Swarm Plot",
    "Strip Plot",
    "ECDF Plot",
    "Facet Grid"
]

# User selection
plot_type = st.selectbox("Choose a visualization type", visualizations)

# Generate plots based on selection
if plot_type == "Scatter Plot":
    st.write("Scatter Plot: Bill Length vs Bill Depth")
    fig, ax = plt.subplots()
    sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=ax)
    st.pyplot(fig)

elif plot_type == "Line Plot":
    st.write("Line Plot: Flipper Length by Species")
    fig, ax = plt.subplots()
    sns.lineplot(data=penguins, x="species", y="flipper_length_mm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Histogram":
    st.write("Histogram: Bill Length")
    fig, ax = plt.subplots()
    sns.histplot(data=penguins, x="bill_length_mm", bins=20, kde=True, ax=ax)
    st.pyplot(fig)

elif plot_type == "Box Plot":
    st.write("Box Plot: Bill Length by Species")
    fig, ax = plt.subplots()
    sns.boxplot(data=penguins, x="species", y="bill_length_mm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Violin Plot":
    st.write("Violin Plot: Flipper Length by Species")
    fig, ax = plt.subplots()
    sns.violinplot(data=penguins, x="species", y="flipper_length_mm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Bar Plot":
    st.write("Bar Plot: Average Flipper Length by Species")
    fig, ax = plt.subplots()
    sns.barplot(data=penguins, x="species", y="flipper_length_mm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Count Plot":
    st.write("Count Plot: Species Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=penguins, x="species", ax=ax)
    st.pyplot(fig)

elif plot_type == "Heatmap":
    st.write("Heatmap: Correlation Matrix")
    fig, ax = plt.subplots()
    corr = penguins.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Pair Plot":
    st.write("Pair Plot: Pairwise Relationships")
    st.pyplot(sns.pairplot(penguins, hue="species"))

elif plot_type == "KDE Plot":
    st.write("KDE Plot: Flipper Length Distribution")
    fig, ax = plt.subplots()
    sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", fill=True, ax=ax)
    st.pyplot(fig)

elif plot_type == "Ridge Plot":
    st.write("Ridge Plot: Flipper Length by Species")
    from joypy import joyplot
    fig, ax = plt.subplots()
    joyplot(
        data=penguins[['species', 'flipper_length_mm']].dropna(),
        by="species",
        column="flipper_length_mm",
        ax=ax,
        fade=True
    )
    st.pyplot(fig)

elif plot_type == "Swarm Plot":
    st.write("Swarm Plot: Bill Depth by Species")
    fig, ax = plt.subplots()
    sns.swarmplot(data=penguins, x="species", y="bill_depth_mm", ax=ax)
    st.pyplot(fig)

elif plot_type == "Strip Plot":
    st.write("Strip Plot: Bill Length by Species")
    fig, ax = plt.subplots()
    sns.stripplot(data=penguins, x="species", y="bill_length_mm", jitter=True, ax=ax)
    st.pyplot(fig)

elif plot_type == "ECDF Plot":
    st.write("ECDF Plot: Flipper Length")
    fig, ax = plt.subplots()
    sns.ecdfplot(data=penguins, x="flipper_length_mm", hue="species", ax=ax)
    st.pyplot(fig)

elif plot_type == "Facet Grid":
    st.write("Facet Grid: Bill Depth by Island and Species")
    g = sns.FacetGrid(penguins, col="island", row="species", margin_titles=True)
    g.map_dataframe(sns.scatterplot, x="bill_length_mm", y="bill_depth_mm")
    st.pyplot(g)
