# Knowledge Assistant Assignment

Submitted by: Yuvaraja Mohan

## API Stack
- Java 17+
- Maven 3.8+
- Karate 1.4+

Run:
cd api-tests
mvn test

## UI Stack
- Python 3.10+
- Selenium 4
- webdriver-manager

Run:
cd ui-tests
pip install -r requirements.txt
python -m unittest discover -s tests -v

## Locators Used
Region      -> id='region'
Role        -> id='role'
Question    -> id='q'
Ask Button  -> id='ask'
Answer      -> id='answer'
Citations   -> id='cites'
Documents   -> css='aside.card.panel'
