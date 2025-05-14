# quiz-scrapler
I wrote this script to scrap multiple choices quizzes on canvas and put them all in a text file so it's easier to import to Quizlet

# How to use this cript:
1. Download html of quizzes from canvas and put in the same folder. Ex: `/Users/Thang/Documents/SJSU materials/CMPE 131/quizlet/`
2. Go to main.py and change `source_folder` to that folder: 
    Ex: 
    ``` source_folder = str = r'/Users/Thang/Documents/SJSU materials/CMPE 131/quizlet/'
   ```
3. Run: 
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python3 main.py # or python main.py depends on your python version.
```
4. Check out the `result.txt` file generated on the same `source_folder`
5. Upload to quizlet as Flashcard for convenient reviewing. <3