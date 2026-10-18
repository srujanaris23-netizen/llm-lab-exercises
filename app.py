
from pathlib import Path

import torch
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_DIR = Path(__file__).parent / "course_model"

if not MODEL_DIR.exists():
    raise RuntimeError(
        "Fine-tuned model not found. Run python train.py first."
    )

tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))
model = AutoModelForTokenClassification.from_pretrained(str(MODEL_DIR))
model.eval()

app = FastAPI(
    title="Course Name Extraction API",
    description="Extract college course names using a fine-tuned BERT model.",
    version="1.0.0",
)


class CourseRequest(BaseModel):
    text: str = Field(min_length=1, max_length=2000)


@app.get("/")
def home():
    return {"message": "Course Name Extraction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


@app.post("/extract-course-name/")
def extract_course_name(request: CourseRequest):
    text = request.text

    encoded = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
        return_offsets_mapping=True,
    )

    offsets = encoded.pop("offset_mapping")[0].tolist()

    with torch.no_grad():
        outputs = model(**encoded)

    predictions = outputs.logits.argmax(dim=-1)[0].tolist()
    id2label = model.config.id2label

    extracted_names = []
    current_start = None
    current_end = None

    def save_current():
        if current_start is not None and current_end is not None:
            name = text[current_start:current_end].strip()
            if name and name not in extracted_names:
                extracted_names.append(name)

    for (start, end), prediction in zip(offsets, predictions):
        if start == end:
            continue

        label = id2label[prediction]

        if label == "B-COURSE":
            save_current()
            current_start = start
            current_end = end

        elif label == "I-COURSE":
            if current_start is None:
                current_start = start
            current_end = end

        else:
            save_current()
            current_start = None
            current_end = None

    save_current()

    return {
        "input_text": text,
        "extracted_course_names": extracted_names,
    }
