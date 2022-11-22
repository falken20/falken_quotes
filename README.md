<div align="center">
  
<!-- Para logo se puede usar https://studio.tailorbrands.com/-->
<img src="./static/assets/logo_app.png" alt="drawing" width="400"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://falken-home.herokuapp.com/static/home_project/img/falken_logo.png" width=40 alt="Personal Portfolio web"></a>

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/falken_quotes) ![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/falken_quotes) ![Test coverage](https://img.shields.io/badge/test%20coverage-0%25-green) ![GitHub License](https://img.shields.io/github/license/falken20/search_extensions)[![Python used version](https://img.shields.io/static/v1?label=python&message=3.8&color=blue&logo=python&logoColor=white)

  
[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) [![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)
</div>

---
### falken_quotes
It is a web where you can see every day or every moment a quote about one or several topics.
Daily quotes. API: https://zenquotes.io/keywords.

##### Deploy
```bash
Explain Heroku, GCP, etc. deploy method
```

##### Setup
```bash
pip install -r requirements.txt
```

##### Running the app
```bash
cd falken_chat
python main.py
```

##### Setup tests
```bash
pip install -r requirements-tests.txt
```

##### Running the tests with pytest and coverage
```bash
./scripts/ccheck_project.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/tests/*
```

##### Environment vars
```bash
ENV_PRO=N
LOG_LEVEL=INFO

# Weather station API key
API_KEY=XXXXXXXXXXXX
STATION_ID=XXXXXXXXXXXX

# Twitter params
CONSUMER_KEY=XXXXXXXXXXXX
CONSUMER_SECRET=XXXXXXXXXXXX
ACCESS_TOKEN=XXXXXXXXXXXX
ACCESS_TOKEN_SECRET=XXXXXXXXXXXX
```

---

##### Versions
1.2.0 New Log model integrated
1.1.0 Adaptations to ORM SQLAlchemy