
# NLPUtilCollection

A collection of useful tools from Natural Language Processing, wrapped in an API in the form of a Docker container.

## 📖 NLPUtilCollection Contents

Currently includes:
1. **Language identification** – using the [fastText](https://fasttext.cc/) package with its pre-trained model for recognizing 176 languages.
2. **Sentence segmentation** – based on tokenizers from [NLTK](https://www.nltk.org/).
3. **Extraction of the main content from html documents** – using the [Trafilatura](https://trafilatura.readthedocs.io/) package.
4. **Removal of fuzzy application duplicates** – using Levenshtein distance and the [Levenshtein](https://maxbachmann.github.io/Levenshtein/) package.

## 📦 Docker Installation

To use, install the latest version of [Docker Engine](https://docs.docker.com/engine/install/).

## 🚀 Launching NLPUtilCollection

Clone the repo:
```shell
git clone https://github.com/kinamoroll/NLPUtilCollection.git
```

Or download it via this [link](https://github.com/kinamoroll/NLPUtilCollection/archive/refs/heads/main.zip) as a zip archive (_don't forget to unzip the archive_).

And start the container:
```shell
cd NLPUtilCollection
docker compose up --build -d
```

To stop the container, navigate to the folder where `NLPUtilCollection` is cloned and run:
```shell
docker compose stop
```

## 🚦 Checking Functionality

After launching _on the same machine_, you can send requests to the container for checking (_curl should be installed for checking_):
```shell
# checking language identification:
curl -v -XPOST -d 'text=some+useful+info' http://127.0.0.1:9090/detect

# checking tokenization: