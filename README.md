# Naturalization Quiz

A command-line quiz application to help you study for the US Naturalization Test. Practice all 100 civics questions required for the citizenship exam.

> [!WARNING]
> **State-specific questions:** Questions 20, 23, 43, and 44 contain **New York-specific** answers (NY Senators, Representative, Governor, and capital). See [Using Custom Questions](#using-custom-questions) to customize for your state.
> 
> **Question updates:** Make sure the questions are up to date by reviewing the official [USCIS Civics Test](https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test). This repository is not actively maintained, but you can update the questions yourself - see [Using Custom Questions](#using-custom-questions).

## Features

- 100 official USCIS civics questions (as of Oct 2025)
- Randomized question order for varied practice
- Fuzzy matching to check your answers
- Visual feedback showing valid answers and your closest match
- Track your score throughout the quiz
- Exit anytime and see your current progress

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

By default, this uses the included questions file with New York-specific answers.

### Using Custom Questions

You can create your own questions file or customize the existing one for your state:

#### Option 1: Modify the included file
1. Navigate to your installation: `naturalization_quiz/questions_NY_state_oct_2025.yaml`
2. Edit questions 20, 23, 43, and 44 with your state's information
3. Save and run the quiz normally

#### Option 2: Create a custom YAML file
1. Copy the format from `questions_NY_state_oct_2025.yaml`
2. Create your own file (e.g., `questions_CA_state.yaml`)
3. Run the quiz with your custom file:
```bash
naturalization-quiz --questions path/to/questions_CA_state.yaml
```

**YAML format example:**
```yaml
"20. Who is one of your state's U.S. Senators now?":
  - "Alex Padilla"
  - "Laphonza Butler"

"23. Name your U.S. Representative.":
  - "Your Representative Name"
```

Each question is a key with a list of acceptable answers. You can have multiple valid answers for each question.

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

## License

MIT

## Credits

The 100 civics questions are from the official [USCIS Civics Test](https://www.uscis.gov/citizenship/find-study-materials-and-resources/study-for-the-test). Good luck with your citizenship exam preparation!# Naturalization Quiz


