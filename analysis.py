"""
Marimo Interactive Data Analysis Notebook
Contact: 23f2005402@ds.study.iitm.ac.in

This notebook demonstrates variable relationships in a synthetic dataset
using interactive widgets and dynamic markdown generation.
"""

import marimo

__generated_with = "0.7.17"
app = marimo.App(width="medium")


@app.cell
def __():
    # Email contact: 23f2005402@ds.study.iitm.ac.in
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    return mo, np, pd, px, go


@app.cell
def __(mo):
    """
    Data Flow: This cell creates interactive controls that will be used 
    by downstream cells to generate dynamic content.
    """
    # Interactive slider for sample size (dependency source)
    sample_size_slider = mo.ui.slider(
        start=50, 
        stop=500, 
        step=25, 
        value=200,
        label="Sample Size"
    )
    
    # Interactive slider for noise level (dependency source)  
    noise_level_slider = mo.ui.slider(
        start=0.1,
        stop=2.0, 
        step=0.1,
        value=0.5,
        label="Noise Level"
    )
    
    return sample_size_slider, noise_level_slider


@app.cell
def __(mo, sample_size_slider, noise_level_slider):
    """
    Display the interactive controls in a nice layout
    """
    mo.md(f"""
    ## Interactive Data Analysis Controls
    **Contact**: 23f2005402@ds.study.iitm.ac.in
    
    Adjust the parameters below to see how they affect the generated dataset and analysis:
    
    {sample_size_slider}
    {noise_level_slider}
    """)


@app.cell  
def __(np, pd, sample_size_slider, noise_level_slider):
    """
    Data Flow: This cell DEPENDS on the slider values from the control cell.
    It generates a synthetic dataset based on the interactive parameters.
    """
    # Get current slider values (dependencies from control cells)
    n_samples = sample_size_slider.value
    noise_level = noise_level_slider.value
    
    # Generate synthetic data with controllable parameters
    np.random.seed(42)  # For reproducibility
    
    # Create correlated variables
    x = np.random.normal(0, 1, n_samples)
    y = 2 * x + 3 + np.random.normal(0, noise_level, n_samples)  # Linear relationship with noise
    z = x**2 + np.random.normal(0, noise_level/2, n_samples)     # Quadratic relationship
    
    # Create DataFrame (output dependency for downstream cells)
    dataset = pd.DataFrame({
        'x_variable': x,
        'y_linear': y, 
        'z_quadratic': z,
        'category': np.random.choice(['A', 'B', 'C'], n_samples)
    })
    
    # Calculate correlation coefficients (output dependency)
    corr_xy = np.corrcoef(x, y)[0, 1]
    corr_xz = np.corrcoef(x, z)[0, 1]
    
    return dataset, corr_xy, corr_xz, n_samples, noise_level


@app.cell
def __(mo, dataset, corr_xy, corr_xz, n_samples, noise_level):
    """
    Data Flow: This cell DEPENDS on dataset and correlation values from the previous cell.
    It creates dynamic markdown content that updates based on widget state.
    """
    # Dynamic markdown that changes based on current parameter values
    mo.md(f"""
    ## Dataset Analysis Summary
    
    **Generated Dataset Properties** (Updates dynamically based on sliders):
    - Sample Size: **{n_samples}** observations
    - Noise Level: **{noise_level:.1f}**
    - X-Y Linear Correlation: **{corr_xy:.3f}**
    - X-Z Quadratic Correlation: **{corr_xz:.3f}**
    
    ### Data Quality Assessment:
    {
        "✅ **Strong linear relationship** detected between X and Y variables." 
        if abs(corr_xy) > 0.7 
        else "⚠️ **Moderate correlation** - consider adjusting noise level for clearer patterns."
        if abs(corr_xy) > 0.4
        else "❌ **Weak correlation** - high noise is masking the underlying relationship."
    }
    
    **Dataset Shape**: {dataset.shape[0]} rows × {dataset.shape[1]} columns
    
    *Contact for questions: 23f2005402@ds.study.iitm.ac.in*
    """)


@app.cell
def __(px, dataset):
    """
    Data Flow: This cell DEPENDS on the dataset from the data generation cell.
    Creates interactive visualization that updates when dataset changes.
    """
    # Create interactive scatter plot (depends on dataset)
    fig = px.scatter(
        dataset, 
        x='x_variable', 
        y='y_linear',
        color='category',
        size='z_quadratic',
        title="Interactive Scatter Plot: X vs Y (sized by Z)",
        labels={'x_variable': 'X Variable', 'y_linear': 'Y Linear'},
        hover_data=['z_quadratic']
    )
    
    fig.update_layout(
        showlegend=True,
        hovermode='closest'
    )
    
    return fig,


@app.cell
def __(mo, fig):
    """
    Display the interactive plot
    """
    mo.md(f"""
    ## Variable Relationship Visualization
    
    The plot below updates automatically when you change the slider values:
    
    {mo.as_html(fig)}
    """)


@app.cell
def __(dataset):
    """
    Data Flow: This cell DEPENDS on the dataset to show statistical summary.
    Provides tabular view that updates with widget changes.
    """
    # Statistical summary (depends on current dataset)
    summary_stats = dataset.describe()
    return summary_stats,


@app.cell
def __(mo, summary_stats):
    """
    Display summary statistics table
    """
    mo.md(f"""
    ## Statistical Summary
    
    Summary statistics for the current dataset configuration:
    
    {mo.as_html(summary_stats)}
    
    ---
    *Analysis by: 23f2005402@ds.study.iitm.ac.in*
    """)


if __name__ == "__main__":
    app.run()
