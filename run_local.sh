set -e  

echo "Building C aggregator..."
make -C c_aggregator

echo "Generating sample data..."
python scripts/generate_sample_data.py \
  --rows 200000 \
  --output data/raw/sample.jsonl

echo "Running aggregation..."
./c_aggregator/bin/aggregator \
  --input data/raw/sample.jsonl \
  --output data/agg/sample_agg.csv \
  --filter "event==purchase" \
  --group_by "user_id" \
  --agg "sum(amount),count(*)"

echo "Running ML analysis..."
python python_ml/analyze.py \
  --input data/agg/sample_agg.csv \
  --output data/results/sample_ml.json

echo "Done!"
echo "Aggregates: data/agg/sample_agg.csv"
echo "ML results: data/results/sample_ml.json"
