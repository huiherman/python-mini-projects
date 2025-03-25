import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# --- Page Setup ---
st.set_page_config(page_title="Mini Data Dashboard", page_icon="📊", layout="centered")
st.title("📊 Python Mini Projects - Data Explorer")

st.markdown("""
Welcome to a simple Streamlit dashboard for exploring data.  
Filter records by age, view summaries, visualize departments, and download results.
""")

# --- Load Data ---
df = pd.read_csv('sample_data.csv')

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
age_filter = st.sidebar.slider(
    "Minimum Age", 
    min_value=int(df['Age'].min()), 
    max_value=int(df['Age'].max()), 
    value=int(df['Age'].min())
)

filtered_df = df[df['Age'] >= age_filter]

# --- Show Filtered Data ---
st.subheader(f"👥 People with Age ≥ {age_filter}")
st.dataframe(filtered_df, use_container_width=True)

# --- Summary Stats ---
st.subheader("📈 Summary Statistics")
st.metric("Average Age", round(filtered_df['Age'].mean(), 2))

# --- Bar Chart: People by Department ---
st.subheader("🏢 People per Department (Filtered)")
dept_counts = filtered_df['Department'].value_counts()


#fig, ax = plt.subplots()
#dept_counts.plot(kind='bar', color='skyblue', ax=ax)
#ax.set_xlabel("Department")
#ax.set_ylabel("Count")
#ax.set_title("Number of People per Department")
#st.pyplot(fig)


dept_counts = filtered_df['Department'].value_counts().reset_index()
dept_counts.columns = ['Department', 'Count']

fig = px.bar(dept_counts, x='Department', y='Count', color='Department',
             title='Number of People per Department',
             labels={'Count': 'Number of People'},
             height=400)
st.plotly_chart(fig)

# --- Download Button ---
st.subheader("📥 Download Filtered Data")
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)

# --- Footer ---
st.markdown("---")
st.markdown("Created by Herman Hui · [GitHub](https://github.com/yourusername)")
