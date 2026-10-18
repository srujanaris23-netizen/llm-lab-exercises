
from pathlib import Path

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForTokenClassification,
    DataCollatorForTokenClassification,
    Trainer,
    TrainingArguments,
)

MODEL_NAME = "bert-base-cased"
OUTPUT_DIR = "./course_model"

# Each example contains a sentence and the exact course name in it.
# Add more real college/course examples for better accuracy.
examples = [
    {"text": "I want to study Computer Science.", "course": "Computer Science"},
    {"text": "Our college offers Machine Learning.", "course": "Machine Learning"},
    {"text": "Please tell me about Data Structures and Algorithms.", "course": "Data Structures and Algorithms"},
    {"text": "I am interested in Operating Systems.", "course": "Operating Systems"},
    {"text": "Does the college teach Artificial Intelligence?", "course": "Artificial Intelligence"},
    {"text": "I want to enroll in Computer Networks.", "course": "Computer Networks"},
    {"text": "Tell me about Database Management Systems.", "course": "Database Management Systems"},
    {"text": "The course available is Cloud Computing.", "course": "Cloud Computing"},
    {"text": "I would like to learn Cyber Security.", "course": "Cyber Security"},
    {"text": "Our syllabus includes Software Engineering.", "course": "Software Engineering"},
    {"text": "Can I select Data Science?", "course": "Data Science"},
    {"text": "Explain the course called Web Development.", "course": "Web Development"},
    {"text": "I am looking for an Electronics Engineering course.", "course": "Electronics Engineering"},
    {"text": "Does this college offer Information Science?", "course": "Information Science"},
    {"text": "Tell me about the course Computer Science.", "course": "Computer Science"},
    {"text": "I want to study Cloud Computing this year.", "course": "Cloud Computing"},
    {"text": "The subject is Machine Learning.", "course": "Machine Learning"},
    {"text": "Is Data Science offered at this college?", "course": "Data Science"},
    {"text": "I need details about Cyber Security.", "course": "Cyber Security"},
    {"text": "Please explain Database Management Systems.", "course": "Database Management Systems"},
]

LABEL2ID = {"O": 0, "B-COURSE": 1, "I-COURSE": 2}
ID2LABEL = {value: key for key, value in LABEL2ID.items()}

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

dataset = Dataset.from_list(examples)


def tokenize_and_align(example):
    text = example["text"]
    course = example["course"]

    start = text.index(course)
    end = start + len(course)

    encoded = tokenizer(
        text,
        truncation=True,
        max_length=128,
        return_offsets_mapping=True,
    )

    labels = []
    first_course_token = True

    for token_start, token_end in encoded["offset_mapping"]:
        # Special tokens have an offset of (0, 0).
        if token_start == token_end:
            labels.append(-100)
        elif token_start < end and token_end > start:
            if first_course_token:
                labels.append(LABEL2ID["B-COURSE"])
                first_course_token = False
            else:
                labels.append(LABEL2ID["I-COURSE"])
        else:
            labels.append(LABEL2ID["O"])

    encoded.pop("offset_mapping")
    encoded["labels"] = labels
    return encoded


tokenized_dataset = dataset.map(
    tokenize_and_align,
    remove_columns=dataset.column_names,
)

model = AutoModelForTokenClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(LABEL2ID),
    id2label=ID2LABEL,
    label2id=LABEL2ID,
)

training_args = TrainingArguments(
    output_dir="./training_results",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    num_train_epochs=10,
    weight_decay=0.01,
    save_strategy="no",
    report_to="none",
    use_cpu=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=DataCollatorForTokenClassification(tokenizer),
)

print("Starting fine-tuning...")
trainer.train()

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"Fine-tuned model saved to {OUTPUT_DIR}")
