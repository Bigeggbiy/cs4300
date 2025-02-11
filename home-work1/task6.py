# task6.py
def count_words(file_path):
    with open(file_path, "r") as f:
        return len(f.read().split())