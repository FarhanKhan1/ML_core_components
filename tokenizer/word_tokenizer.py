from dataset_word_tokenizer import dataset
import re
vocabulary = {"UNK":0}

def tokenize(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Split into words
    tokens = text.split()

    return tokens

def populate_vocabulary(list_of_tokens):
    for token in list_of_tokens:
        if token not in vocabulary:
            vocabulary[f"{token}"]=len(vocabulary)

def buiding_model_vocab(row):
    question=row["Question"]
    answer=row["Answer"]
    tokens=tokenize(question+" "+answer)
    populate_vocabulary(tokens)

def text_to_input_ids(text):
    tokens = tokenize(text)
    input_ids = list()
    for token in tokens:
        if token in vocabulary:
            input_ids.append(vocabulary[token])
        else:
            input_ids.append(vocabulary['UNK'])
    return input_ids

def main(dataset):
    print("building vocabulary for the dataset...")
    dataset.apply(buiding_model_vocab, axis=1)
    print("Vocabulary has been built successfully")
    print(f"Vocabulary Length: {len(vocabulary)} \n Vocabulary Type: Space based Tokenization")



if __name__ == "__main__":
    main(dataset)
    print(vocabulary)
    while True:
        sentence=input("Please Enter your Sentence to get its token_ids: ")
        input_ids = text_to_input_ids(sentence)   
        print(input_ids)


