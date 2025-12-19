# End to End ML project — Students Performance in Exams prediction

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Data Ingestion](#data-ingestion)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This repository contains an end-to-end machine learning project for predicting student exam performance. It includes source code for data ingestion, preprocessing, model training, a small web application for prediction, and notebooks used for exploratory analysis and experiments.

## Installation

```bash
git clone https://github.com/Farzam1372/mlproject.git
cd mlproject
# (Optional) Create and activate a virtual environment
python -m venv venv
# On Unix/macOS
source venv/bin/activate
# On Windows (PowerShell)
# .\venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt
```

Note: The project was developed with Python 3.11 (see notebook metadata). Using a recent Python 3.x interpreter is recommended.

## Data Ingestion (Kaggle Dataset)

This project loads the **Students Performance in Exams** dataset directly from Kaggle using the `kagglehub` adapter in the data ingestion component.

Kaggle dataset reference: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

To run the data ingestion module locally:

```bash
python -m src.components.data_ingestion
```

What this does:
- Downloads/loads the dataset via `kagglehub` (the code uses KaggleDatasetAdapter to load into a pandas DataFrame).
- Standardizes column names (lowercase, non-alphanumerics replaced by underscores).
- Writes a raw copy to `artifacts/data.csv` and creates `artifacts/train.csv` and `artifacts/test.csv` (80/20 split).

Requirements / notes:
- `kagglehub` must be installed and configured. The dataset load requires internet access and appropriate credentials if needed by your environment.

## Usage

Available entry points in this repository:

- Training pipeline (programmatic):
  ```bash
  python -m src.pipeline.train_pipeline
  ```
  This runs the training pipeline implemented under `src/pipeline` and will produce model artifacts under `artifacts/`.

- Prediction pipeline (programmatic):
  ```bash
  python -m src.pipeline.predict_pipeline
  ```

- Web app (Flask) UI for single datapoint prediction:
  ```bash
  python application.py
  ```
  Then open http://127.0.0.1:5000 in your browser.

Important note about the web form (templates/home.html): currently the two numeric input fields in the HTML are mislabeled (the `name` attributes are swapped between `reading_score` and `writing_score`). If you rely on the form, be aware of this mismatch or correct `templates/home.html` so the inputs match their labels.

## Project Structure

(This is the actual layout in the repository root — updated to match repository contents)

```
mlproject/
├── .ebextensions/
├── artifacts/                # Generated dataset and model artifacts (data.csv, train.csv, test.csv, model.pkl, preprocessor.pkl)
├── catboost_info/
├── notebook/                 # Jupyter notebooks used for EDA and experiments
├── src/                      # Source code (components, pipeline, utils, etc.)
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/                # HTML templates for the web UI
├── application.py            # Flask app entry point for predictions
├── requirements.txt
├── setup.py
└── README.md
```

## Features

- Data ingestion from Kaggle via `kagglehub` adapter
- Data preprocessing and column standardization
- Training pipeline that outputs model and preprocessor artifacts
- A small web UI to submit single datapoints for prediction
- Notebooks for EDA and experimentation

## Requirements

- Python 3.11+ is recommended (notebooks were run with Python 3.11)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- If running data ingestion via Kaggle, ensure `kagglehub` (and any credentials) are set up in your environment.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

Please follow the existing coding style and include tests where appropriate.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact

- GitHub: [Farzam1372](https://github.com/Farzam1372)
- LinkedIn: [Farzamnazari](https://www.linkedin.com/in/farzamnazari/)
