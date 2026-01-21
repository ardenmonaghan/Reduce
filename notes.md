Notes: Reducer - AI analytical database storage tool

Upload datasets in CSV format, Give them names, have them uploaded Cloud storage.
MapReduce framework is used for reducing the data and allowing for batch reductions
On site you can choose individual columns to aggregate and run reductions.

precomputed metric tables
ML insights (clusters/anomalies)
interactive dashboards + visualizations
optional: LLM-assisted querying over the aggregated tables (safe mode)

“mini warehouse + metrics generator + ML dashboard.”

pipeline-ai-dashboard/
├─ streamlit_app/app.py
├─ c_aggregator/ (C code + Makefile + bin/aggregator)
├─ python_ml/ (analysis scripts)
├─ jobs/ (generated job configs per dataset)
├─ data/
│  ├─ raw/
│  ├─ agg/
│  └─ results/
├─ metadata/
│  └─ pipeline.db
├─ scripts/
│  ├─ generate_sample_data.py
│  └─ run_local.sh
├─ Dockerfile
└─ .github/workflows/ci.yml

Workflow: 
1. A user can login, have all of their cloud stored datasets that are uploaded ready to go.
2. "Smart" reductions suggestions. Saved as job configs in JSON where they can be run in a MapReduce framework. -> Either this or we can simply use SQLite where we run queries for
reductions and save the tables. 
3. Streamlit calls your C aggregator:
reads the raw CSV filters/group-bys/aggregates (MapReduce pattern, multi-threaded) writes an aggregate CSV: data/agg/<dataset_id>/<job_name>.csv Then Python loads each aggregate CSV into SQLite tables for fast querying.
4. ML Insights (Run ML) clustering/k-means with anamoly detection.
5. Interactive dashboards + visualizations.

I was thinking about for the MVP
we have a streamlit frontend where I can store the database in 2 different ways CSV and SQLite, then have a run queries (Smart) for smart aggregations, and then have Visualizations like K means clustering and other things run for visualization provided, then have ML run queries where you can prompt an LLM to query where the LLM would have access to the reduced databases (easier for the ML to handle) and then run some of its suggested queries to get results, or the user can ask in english for a query to run