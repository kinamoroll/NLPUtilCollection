
# NLPUtilCollection

A collection of useful tools from Natural Language Processing, wrapped in an API in the form of a Docker container.

## 📖 NLPUtilCollection Contents

Currently includes:
1. **Language identification** – using the [fastText](https://fasttext.cc/) package with its pre-trained model for recognizing 176 languages.
2. **Sentence segmentation** – based on tokenizers from [NLTK](https://www.nltk.org/).
3. **Extraction of the main content from html documents** – using the [Trafilatura](https://trafilatura.readthedocs.io/) package.
4. **Removal of fuzzy application duplicates** – using Levenshtein distance and the [Levenshtein](https://maxbachmann.github.io/Levenshtein/) package.

## 📦 Docker Installation