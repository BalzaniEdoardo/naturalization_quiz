# Naturalization Quiz

A command-line quiz application to help you study for the US Naturalization Test. Practice all 100 civics questions required for the citizenship exam.

## Features

- 100 official USCIS civics questions (as of Oct 2025)
- Randomized question order for varied practice
- Fuzzy matching to check your answers
- Visual feedback showing valid answers and your closest match
- Track your score throughout the quiz
- Exit anytime and see your current progress

> [!NOTE]
> Questions 20, 23, 43, and 44 contain **New York-specific** answers (NY Senators, Representative, Governor, and capital). If you live in a different state, you'll need to customize these answers in the `naturalization_quiz/quiz.py` file.

## Installation

### Windows

#### Step 1: Extract the ZIP file
Extract the downloaded ZIP file to a location of your choice (e.g., `C:\Users\YourName\naturalization-quiz`).

#### Step 2: Install uv
Open PowerShell and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen PowerShell for the changes to take effect.

#### Step 3: Install and run
Navigate to the extracted folder:
```powershell
cd C:\Users\YourName\naturalization-quiz
```
(Replace with your actual path)

Then copy and paste the following command:
```powershell
uv python install 3.12; uv venv; .venv\Scripts\activate; pip install -e .; naturalization-quiz
```

This will install Python, create a virtual environment, install the package, and start the quiz!

### macOS/Linux

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Python
uv python install 3.12

# Navigate to the extracted repository
cd /path/to/naturalization-quiz

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install the package
pip install -e .
```

## Usage

After installation, simply run:
```bash
naturalization-quiz
```

### How to Play

1. The quiz will present you with questions in random order
2. Type your answer and press Enter
3. Review the table showing valid answers and your match
4. Confirm if your answer was correct (y/n)
5. Type `exit` at any time to quit and see your score
6. Complete all 100 questions to get your final score

### Passing Score

You need to answer at least 80 out of 100 questions correctly to pass!

## Running the Quiz Later

To run the quiz after installation:

**Windows:**
```powershell
cd C:\Users\YourName\naturalization-quiz
.venv\Scripts\activate
naturalization-quiz
```

**macOS/Linux:**
```bash
cd /path/to/naturalization-quiz
source .venv/bin/activate
naturalization-quiz
```

## Development

To install development dependencies (Black and isort):
```bash
pip install -e ".[dev]"
```

## License

MIT

## About

This quiz is based on the official USCIS 100 civics questions for the naturalization test. Good luck with your citizenship exam preparation!

## Credits

The 100 civics questions are from the official [USCIS Civics Test](https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test). 

Note: Questions 20, 23, 43, and 44 contain New York-specific answers. You may need to customize these for your state.