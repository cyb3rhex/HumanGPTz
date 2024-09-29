import sys
import random
import spacy
import nltk
import ssl
from nltk.tokenize import word_tokenize
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from sentence_transformers import SentenceTransformer, util
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
def download_nltk_resources():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    resources = ['punkt', 'averaged_perceptron_tagger', 'punkt_tab']
    for resource in resources:
        try:
            nltk.download(resource, quiet=True)
        except Exception as e:
            print(f"Error downloading {resource}: {str(e)}")
            return False
    return True

class AdvancedTextHumanizer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    def humanize_text(self, text):
        doc = self.nlp(text)
        humanized_sentences = []
        for sent in doc.sents:
            humanized_sent = self.humanize_sentence(sent.text)
            humanized_sentences.append(humanized_sent)
        return ' '.join(humanized_sentences)
    def humanize_sentence(self, sentence):
        sentence = self.introduce_imperfections(sentence)
        sentence = self.vary_sentence_structure(sentence)
        sentence = self.add_conversational_elements(sentence)
        return sentence
    def introduce_imperfections(self, sentence):
        words = word_tokenize(sentence)
        if random.random() < 0.3:
            words = [w for w in words if w.lower() not in ['a', 'an', 'the']]
        if random.random() < 0.2:
            for i, word in enumerate(words):
                if word == "is":
                    words[i] = "'s"
                elif word == "are":
                    words[i] = "'re"
        return ' '.join(words)
    def vary_sentence_structure(self, sentence):
        if random.random() < 0.3:
            conjunctions = ['And', 'But', 'So']
            sentence = f"{random.choice(conjunctions)} {sentence}"
        if random.random() < 0.2:
            doc = self.nlp(sentence)
            if any(token.dep_ == 'nsubj' for token in doc):
                subject = next(token for token in doc if token.dep_ == 'nsubj')
                verb = subject.head
                object = next((token for token in verb.children if token.dep_ == 'dobj'), None)
                if object:
                    passive = f"{object.text} {verb.text} by {subject.text}"
                    sentence = sentence.replace(f"{subject.text} {verb.text} {object.text}", passive)
        return sentence
    def add_conversational_elements(self, sentence):
        if random.random() < 0.3:
            fillers = ['um', 'uh', 'like', 'you know']
            sentence = f"{random.choice(fillers)}, {sentence}"
        if random.random() < 0.2:
            opinions = ["I think", "In my opinion", "It seems to me"]
            sentence = f"{random.choice(opinions)}, {sentence}"
        return sentence

class TextHumanizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.humanizer = AdvancedTextHumanizer()

    def initUI(self):
        layout = QVBoxLayout()
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter your text here...")
        layout.addWidget(self.input_text)
        self.humanize_button = QPushButton("Humanize Text")
        self.humanize_button.clicked.connect(self.on_humanize)
        layout.addWidget(self.humanize_button)
        self.output_text = QTextEdit()
        self.output_text.setPlaceholderText("Humanized text will appear here...")
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)
        self.setLayout(layout)
        self.setWindowTitle('HumanGPTz - htdark.com [ LSDeep - v 1.0]')
        self.setGeometry(300, 300, 500, 400)
    def on_humanize(self):
        input_text = self.input_text.toPlainText()
        try:
            humanized_text = self.humanizer.humanize_text(input_text)
            self.output_text.setPlainText(humanized_text)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    if not download_nltk_resources():
        print("Failed to download required NLTK resources. The application may not function correctly.")
    app = QApplication(sys.argv)
    ex = TextHumanizerApp()
    ex.show()
    sys.exit(app.exec())