
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
curl -v -XPOST -d 'text=Test+sent%3F+Don%27t+or+ms.+Not%21+Yes%2C+of+course.+Maybe+mr.Jeck+and+band.&lang=en' http://127.0.0.1:9090/tokenize

# extraction of text from an html document:
curl -v XPOST -d 'html=%3Chtml%3E%3Cbody%3E%3Ch1%3Etest%3C%2Fh1%3E%3Cp%3Ethis%20is%20test%3C%2Fp%3E%3C%2Fbody%3E%3C%2Fhtml%3E' http://127.0.0.1:9090/extract

# deletion of sentence duplicates:
curl -v XPOST -d '{"sentences": ["1 sentence", "2 sentence", "Another sentence"], "threshold": 0.8}' http://127.0.0.1:9090/deduplicate
```

To check from another server, you need to change the IP address and ensure the `9090` port is not closed in the built-in firewall.

## 📚 API Endpoint Description

All endpoints only process requests with the `POST` HTTP method.

### Text Language Identification

**API Endpoint**: `/detect`

Supports the following input parameters:
- `text` – a string with the text for which you want to identify the language;
- `count` – number of results. By default: `3`.

As a result, there will be JSON in the form of an array of dictionaries:
```json
[
  {
    "confidence": 0.5937589406967163,
    "code": "en",
    "name": "English",
    "family": "Indo-European",
    "endonym": "English",
    "iso639-1": "en",
    "iso639-2/T": "eng",
    "iso639-2/B": "eng",
    "iso639-3": "eng"
  }
]
```

### Text Segmentation into Sentences

**API Endpoint**: `/tokenize`

Supports the following input parameters:
- `text` – a string with text that needs to be broken down into sentences;
- `lang` – text language code. By default: `en`.

Supported languages for tokenization:
```json
{
    "en": "english",
    "ru": "russian",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "et": "estonian",
    "fi": "finnish",
    "fr": "french",
    "de": "german",
    "el": "greek",
    "it": "italian",
    "ml": "malayalam",
    "no": "norwegian",
    "pl": "polish",
    "pt": "portuguese",
    "sl": "slovene",
    "es": "spanish",
    "sv": "swedish",
    "tr": "turkish"
}
```

As a result, there will be JSON in the form of an array of strings:
```json
[
  "Test sent?",
  "Don't or ms. Not!",
  "Yes, of course.",
  "Maybe mr.Jeck and band."
]
```

### Extracting Main Content from an HTML Document

**API Endpoint**: `/extract`

This supports only one input parameter:
- `html` – the content of an HTML page, encoded using the `urlencode` function (the page needs to be downloaded independently).

It's very important to encode the transmitted page in `URL-encoding` format because if there is no encoding, the parser will process only part of the page (up to the first symbol `&`)!

As a result, the main content of the page will be returned without html tags.

### Fuzzy Application Duplicate Deletion

**API Endpoint**: `/deduplicate`

❗️ Please note that only `JSON` is acceptable.

The following keys with values must be inside `json`:
- `sentences` – an array of strings (sentences) from which duplicates are to be deleted;
- `threshold` – a threshold value in the interval `[0.0, 1.0]`, triggering which considers the sentence as a fuzzy duplicate (the parameter is optional, by default: `0.8`).