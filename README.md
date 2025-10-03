# DASHBOARD-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MOHAMED SAFEER ANFAL . C

*INTERN ID*: CT04DY2161

*DOMAIN*: Data Analytics

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:This program creates an interactive COVID-19 Dashboard using the Dash framework and Plotly Express. It allows users to explore COVID-19 data by country and WHO region, while also visualizing key performance indicators (KPIs) and graphical insights.

1. Libraries Used

dash, dash.dcc, dash.html → For building the web application layout and interactivity.

plotly.express → For generating interactive charts (bar plots, pie charts).

pandas → For loading and filtering the COVID-19 dataset (Covid - 19.csv).

2. Layout

The dashboard layout is divided into sections:

Filters (Dropdowns) → Users can select a country and a WHO region.

KPIs → Display important statistics such as:

🦠 Total Cases

☠️ Total Deaths

💚 Recovery Rate

📌 Active Cases

Graphs → Three main visualizations are displayed:

Top 10 Countries by Confirmed Cases (per Region) – A bar chart to compare the worst-hit countries in a selected region.

Distribution of Cases in Selected Country – A pie chart showing proportions of confirmed, deaths, recovered, and active cases.

Death vs Recovery Rate per 100 Cases (per Region) – A bar chart comparing recovery and death efficiency across countries in the region.

3. Callbacks

A callback function update_dashboard() is defined to make the dashboard interactive.

When the user selects a country or region, the function updates all KPIs and graphs dynamically.

It uses filtering logic on the dataset (df[df['WHO Region'] == region] and df[df['Country'] == country]).

4. Execution

Finally, app.run(debug=True) launches the web app in the browser, allowing interactive exploration of COVID-19 data.

🔹 Feedback on the Program

✅ Strengths:

Well-structured and modular: The layout is cleanly separated into filters, KPIs, and graphs.

Interactive and user-friendly: Dropdown filters for both country and region make it very intuitive.

Effective KPIs: Presenting metrics with emojis (🦠, ☠️, 💚, 📌) makes the dashboard more engaging and easy to read.

Good Visualization Choices:

Bar chart for comparison.

Pie chart for distribution.

Bar chart for rates — clear and informative.

Scalable Design: Works for different datasets and can easily be extended with new metrics.

🌟 Overall Feedback

This dashboard is an excellent demonstration of interactive data visualization. It combines real-world data, machine learning-style insights (KPIs), and intuitive charts into one interactive app. It shows your ability to go beyond static analysis and deliver an analytical tool that end-users can explore dynamically. With small UI improvements and time-series insights, this could be a portfolio-ready project.
