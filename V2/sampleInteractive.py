# pip install streamlit seaborn pandas plotly altair
# streamlit run sampleInteractive.py

# Data: https://www.geeksforgeeks.org/seaborn-datasets-for-data-science/


import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import altair as alt

# Set up Streamlit app
st.title("Interactive Visualizations with Penguins Dataset")

# Load dataset
@st.cache_data
def load_data():
    return sns.load_dataset('penguins')

penguins = load_data()

# List of interactive visualizations
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
    st.write("Interactive Scatter Plot: Bill Length vs Bill Depth")
    fig = px.scatter(
        penguins,
        x="bill_length_mm",
        y="bill_depth_mm",
        color="species",
        hover_data=["island", "sex"]
    )
    st.plotly_chart(fig)

elif plot_type == "Line Plot":
    st.write("Interactive Line Plot: Flipper Length by Species")
    fig = alt.Chart(penguins).mark_line().encode(
        x="species",
        y="flipper_length_mm",
        tooltip=["species", "flipper_length_mm"]
    )
    st.altair_chart(fig, use_container_width=True)

elif plot_type == "Histogram":
    st.write("Interactive Histogram: Bill Length")
    fig = px.histogram(
        penguins,
        x="bill_length_mm",
        color="species",
        nbins=20,
        marginal="rug",
        hover_data=["island", "sex"]
    )
    st.plotly_chart(fig)

elif plot_type == "Box Plot":
    st.write("Interactive Box Plot: Bill Length by Species")
    fig = px.box(
        penguins,
        x="species",
        y="bill_length_mm",
        color="species",
        hover_data=["island", "sex"]
    )
    st.plotly_chart(fig)

elif plot_type == "Violin Plot":
    st.write("Interactive Violin Plot: Flipper Length by Species")
    fig = px.violin(
        penguins,
        x="species",
        y="flipper_length_mm",
        color="species",
        box=True,
        points="all"
    )
    st.plotly_chart(fig)

elif plot_type == "Bar Plot":
    st.write("Interactive Bar Plot: Average Flipper Length by Species")
    summary = penguins.groupby("species").flipper_length_mm.mean().reset_index()
    fig = px.bar(
        summary,
        x="species",
        y="flipper_length_mm",
        color="species",
        hover_data=["flipper_length_mm"]
    )
    st.plotly_chart(fig)

elif plot_type == "Count Plot":
    st.write("Interactive Count Plot: Species Distribution")
    fig = px.bar(
        penguins["species"].value_counts().reset_index(),
        x="index",
        y="species",
        labels={"index": "Species", "species": "Count"},
        color="index"
    )
    st.plotly_chart(fig)

elif plot_type == "Heatmap":
    st.write("Interactive Heatmap: Correlation Matrix")
    corr = penguins.corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="coolwarm"
    )
    st.plotly_chart(fig)

elif plot_type == "Pair Plot":
    st.write("Interactive Pair Plot: Pairwise Relationships")
    fig = px.scatter_matrix(
        penguins,
        dimensions=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"],
        color="species",
        labels={col: col.replace('_', ' ') for col in penguins.columns}
    )
    st.plotly_chart(fig)

elif plot_type == "KDE Plot":
    st.write("Interactive KDE Plot: Flipper Length Distribution")
    fig = px.density_contour(
        penguins,
        x="flipper_length_mm",
        y="bill_length_mm",
        color="species",
        marginal_x="histogram",
        marginal_y="rug"
    )
    st.plotly_chart(fig)

elif plot_type == "Ridge Plot":
    st.write("Interactive Ridge Plot: Flipper Length by Species")
    st.write("Ridge plots are challenging in interactive tools; try using area-based visualization.")
    fig = px.violin(
        penguins,
        x="flipper_length_mm",
        y="species",
        color="species",
        orientation="h",
        box=True,
        points="all"
    )
    st.plotly_chart(fig)

elif plot_type == "Swarm Plot":
    st.write("Interactive Swarm Plot: Bill Depth by Species")
    fig = alt.Chart(penguins).mark_circle(size=60).encode(
        x="species",
        y="bill_depth_mm",
        color="species",
        tooltip=["species", "bill_depth_mm", "island"]
    ).interactive()
    st.altair_chart(fig, use_container_width=True)

elif plot_type == "Strip Plot":
    st.write("Interactive Strip Plot: Bill Length by Species")
    fig = alt.Chart(penguins).mark_circle(size=50).encode(
        x="species",
        y="bill_length_mm",
        color="species",
        tooltip=["species", "bill_length_mm", "island"]
    ).interactive()
    st.altair_chart(fig, use_container_width=True)

elif plot_type == "ECDF Plot":
    st.write("Interactive ECDF Plot: Flipper Length")
    fig = alt.Chart(penguins).transform_window(
        ecdf="cumulate",
        sort=[alt.SortField("flipper_length_mm")],
    ).mark_line().encode(
        x="flipper_length_mm",
        y="ecdf:Q",
        color="species",
        tooltip=["flipper_length_mm", "species"]
    )
    st.altair_chart(fig, use_container_width=True)

elif plot_type == "Facet Grid":
    st.write("Interactive Facet Grid: Bill Depth by Island and Species")
    fig = px.scatter(
        penguins,
        x="bill_length_mm",
        y="bill_depth_mm",
        color="species",
        facet_col="island",
        hover_data=["sex"]
    )
    st.plotly_chart(fig)
