import re
from datasets import load_dataset

def preprocess(text):
    # Custom preprocessing steps can be added here
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def process_docs(dataset):
    # Assuming the dataset has 'query', 'choices', and 'label' fields
    def _process_doc(doc):
        doc["query"] = preprocess(doc["query"])
        doc["choices"] = [preprocess(choice) for choice in doc["choices"]]
        # Convert label to integer if it's not already
        doc["label"] = int(doc["label"]) if isinstance(doc["label"], str) else doc["label"]
        return doc

    return dataset.map(_process_doc)
