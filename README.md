## Project Idea

1. React / Stream Lit for the frontend

End to End Idea:

1.  Insert / upload a dataset
Uploading CSV file into react or streamlit frontend

2. MapReduce aggregation: 

Possibly start with C first. 
Hold a library of possible aggregations. 
Worker tasks parse -> filter -> group then aggregate
Press run suggested reductions via streamlit. 
System runs each job (system aggregator) producing multuple aggregate CSV

Multiple levels (if user_id) suggest group by user_id
If there exists an amount then suggest sum, avg, max. 
Number of jobs may be capped. 

3. ML/AI analysis in python
C sends the aggregated data to python for ML/AI analysis. Which can be run on multiple batches (auto metrics generation for dataset)


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
