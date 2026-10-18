# Final Presentation / Report Assembly Guide

Use this as a slide-by-slide structure for `Data Science Capstone Project Report.pdf`. Fill all result fields from the outputs produced by running the repository. Do not use assumed values.

1. **Executive Summary** — business context, objective, data sources, methods, measured best-model result.
2. **Introduction and Business Problem** — why predicting first-stage landing outcomes matters; define target.
3. **Data Collection: SpaceX API** — endpoint/source, request → JSON parsing → tabular extraction flowchart, screenshot/output, GitHub link.
4. **Data Collection: Web Scraping** — Wikipedia source, request → BeautifulSoup → parse tables → save CSV flowchart, screenshot/output, GitHub link.
5. **Data Wrangling** — missing-value summary, imputation method, target definition, encoding and exported data, GitHub link.
6. **EDA Methodology** — chart types, questions each chart answers, source notebook link.
7. **EDA Visual Results** — flight number vs launch site, payload vs launch site, success rate by orbit, yearly trend. Use actual chart images and 1–2 observations per chart.
8. **EDA with SQL** — representative queries and their actual outputs; include distinct sites, payload aggregation, landing outcomes, and yearly success rates.
9. **Folium Map** — actual map screenshot, marker/popup meaning, source notebook link. Include proximity distances only if independently measured and documented.
10. **Plotly Dash Dashboard** — actual screenshots of the site dropdown, outcome pie chart, payload slider and scatter chart; include how filters change the charts.
11. **Predictive Analysis Methodology** — train/test split, preprocessing pipeline, CV strategy, four algorithms and parameter search.
12. **Model Evaluation** — table from `model_comparison_results.csv`, confusion matrix image, precision, recall, F1 and accuracy for the selected model.
13. **Conclusion and Future Work** — evidence-based summary, limitations (small historical dataset, class definition, missing values), and future improvements.

Before export, check that every slide has a readable title, charts are legible, URLs work, and every numeric claim can be traced to an output in the repository.
