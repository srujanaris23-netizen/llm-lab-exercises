# Exercise 1: LLM Course Name Extraction

## Objective
Extract course names from user-provided text using a fine-tuned language model.

## Technologies
- Python
- Hugging Face Transformers
- FastAPI
- Uvicorn
- Docker

## Files
- `app.py` — API application for course-name extraction
- `train.py` — Model training script
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container configuration
- `course_model/` — Model configuration and tokenizer files

## Run locally
1. Install the required dependencies.
2. Ensure the trained model weights are available in `course_model/`.
3. Start the API with:

```bash
uvicorn app:app --reload
```

4. Open `http://127.0.0.1:8000/docs` to test the API.

## Note
The trained model weights are excluded from this Git repository because the file exceeds GitHub's regular file size limit.
