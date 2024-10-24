# NER + RE

## Features
- Named Entity Recognition (NER) and Relationship Extraction (RE) using GLiNER
- Arabic-English translation using the AYA model

## Model Downloads
- Download GLiNER Models
You need the following GLiNER models for Named Entity Recognition (NER) and Relationship Extraction (RE):
1. `gliner_multi-v2.1`
2. `gliner_multi`
3. `gliner_multi_pii-v1`
4. `gliner-multitask-large-v0.5`

#### Automatic Download
The models will automatically download when you run the code, provided you have an active internet connection.

- Download the AYA Model
For Arabic-English translation, download the AYA model:
Visit the SILMA AYA Model Page.
Download the aya-23-8B-Q5_K_M.gguf model.
Place the model in a directory like: models/aya/.
Update your script to point to the model path:
model = Llama(model_path="models/aya/aya-23-8B-Q5_K_M.gguf")

## Usage
Run the following commands to execute the scripts:
- For Named Entity Recognition and Relationship Extraction:
python test_gliner.py

- For Arabic-English Translation:
python test_aya_with_multitask.py
