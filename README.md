# Cyberabuse Irtaza Final

Cyberabuse-irtaza-final is a text classification application for detecting abusive comments.

![Django](https://img.shields.io/badge/Django-2563EB?style=flat-square) ![SQLite](https://img.shields.io/badge/SQLite-0F172A?style=flat-square)

## Overview

The Django implementation is organized around the entry points and modules below.

## Implemented workflows

The source defines these handlers:

- **Predict** — `predict`

## Getting started

### 1. Get the project

```bash
git clone https://github.com/nasirabbas827/Cyberabuse-irtaza-final.git
cd Cyberabuse-irtaza-final
```

### 2. Prepare Python

Create an isolated environment:

```bash
python -m venv .venv
```

Activate it with `.venv\Scripts\activate` on Windows Command Prompt, or `source .venv/bin/activate` on macOS/Linux.

No requirements file is included. The inspected Python imports indicate these dependencies as a starting point:

```bash
python -m pip install Django pandas joblib scikit-learn
```

Dependency versions are not pinned in this repository.

### 3. Configure and run

Review [`hatespeech/settings.py`](hatespeech/settings.py) for database, media, and any email configuration. Use a local copy of the supplied database when available.

```bash
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/. If you need a Django administration account, run `python manage.py createsuperuser`. Application-specific user roles may be managed separately.

### Model files

Included artifacts: [`models/nb_model.pkl`](models/nb_model.pkl), [`models/rf_model.pkl`](models/rf_model.pkl), [`models/svm_model.pkl`](models/svm_model.pkl), [`models/tfidf_vectorizer.pkl`](models/tfidf_vectorizer.pkl).

Keep models, preprocessing objects, and label mappings together in the locations expected by the source.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`db.sqlite3`](db.sqlite3) | Included SQLite database |
| [`manage.py`](manage.py) | Django command-line entry point |
| [`models`](models) | Model resources |

## Development notes

These setup instructions are based on the repository source. The application has not been executed as part of this documentation update; verify dependencies and configuration in your local environment.
