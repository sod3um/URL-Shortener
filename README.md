# URL-Shortener
Converts long URLs into short, easy-to-share links.

Simple project, which shows my knowledges in **Python** and **FastAPI**.

**I didn't use AI**

## Features
- Create shorted links.
- Store links in database.
- Validate the link and ensure it has not already been shortened.
- Testing tool.

## Installation
Go to ```/app``` directory
Install all required modules:
```bash
pip install -r requirements.txt
```
Run main file:
```bash
python main.py
```
## Testing
I created fast testing tool to test my API. So if you want to test post methods you need this.

1. Run API (tutorial above)
2. Run testing tool (```/test``` directory):
   ```bash
   python test.py https://google.com
   ```
Then it will show server response!
