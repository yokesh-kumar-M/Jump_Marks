import matplotlib.pyplot as plt
import seaborn as sns

def plot_cgpa_trend(df_history):
    plt.figure(figsize=(8,5))
    sns.lineplot(data=df_history, x='Semester', y='CGPA', marker='o')
    plt.title('CGPA Progression Over Semesters')
    plt.ylabel('CGPA')
    plt.xlabel('Semester')
    plt.grid(True)
    plt.show()

def radar_chart(df):
    import plotly.graph_objects as go
    categories = df['Subject'].tolist()
    values = df['Grade Point'].tolist()
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Performance'
    ))
    fig.update_layout(
      polar=dict(
        radialaxis=dict(visible=True, range=[0,10])
      ),
      showlegend=False
    )
    fig.show()
