# Submission Notes

## API Execution
cd api-tests
mvn test

## UI Execution
cd ui-tests
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m unittest discover -s tests -v

Machine-specific artifacts (.venv, target, __pycache__) are intentionally excluded.
