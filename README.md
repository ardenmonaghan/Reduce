## Project Idea

1. React / Stream Lit for the frontend

End to End Idea:

1.  Insert / upload a dataset
Uploading CSV file into react or streamlit frontend
C# backend to process the data and create a dataset record

2. MapReduce aggregation: 

Possibly start with C first. 
C# backend reads data in chunks 
Worker tasks parse -> filter -> group then aggregate

3. ML/AI analysis in python
C# sends the aggregated data to python for ML/AI analysis

Python computes features (optional)
RUNS ML (Data analysis, clustering, classification, etc.)
Python returns the results to C#

4. React frontend displays the results

Streamlit frontend to start then migrate to react, have the fastAPI endpoints. 
POST /datasets/upload
POST /datasets/{id}/aggregate
GET /datasets/{id}/aggregates
POST /datasets/{id}/ml
POST /datasets/{id}/ask

Upload → C map/reduce → aggregated CSV → ML → dashboard

pipeline-ai-dashboard/
├─ streamlit_app/app.py
├─ python_ml/...
├─ c_aggregator/Makefile
├─ c_aggregator/src/...
├─ c_aggregator/bin/aggregator   (built output)
├─ requirements.txt
└─ data/...
