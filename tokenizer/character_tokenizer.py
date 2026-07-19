from dataset_word_tokenizer import dataset
text_corpus = ""
vocabulary = {"[UNK]":0}
ids_to_str = {0:"[UNK]"}
dataset["merged_qa"] = dataset["Question"] + dataset["Answer"]

def build_vocabulary(raw_text):
    unique_chars = list(set(raw_text))
    for each_character in unique_chars:
        vocabulary[each_character] = len(vocabulary)
        ids_to_str[len(vocabulary)-1] = each_character

def combine_text(row):
    global text_corpus
    text_corpus = text_corpus + "\n" + row["merged_qa"]

encode = lambda any_str: [vocabulary[char] if char in vocabulary else vocabulary["[UNK]"] for char in any_str]
decode = lambda input_ids: "".join([ids_to_str[input_id] for input_id in input_ids])

dataset.apply(combine_text, axis=1)
build_vocabulary(text_corpus)
result = encode("structure")


while True:
    text = input("Enter text (q to quit): ")
    if text.lower() == "q":
        break
    print(f"Here is the input_ids: {encode(text)}")

    text_1 = input("Enter 'd' to decode your text: ")
    if text_1.lower() == 'd':
        print(f"Your Original text: {decode(encode(text))}")
    

