import difflib
import numpy as np
from pathlib import Path
import yaml
import argparse


def find_similar(answers: list[str], user_answer: str):
    match = difflib.get_close_matches(user_answer, answers, 1, 0.0)
    return match[0]


def create_answer_table(answers: list[str], best_match: str, this_answer: str):
    idx = answers.index(best_match)

    col_len = max(*(len(a) for a in answers), len(this_answer), 13) + 2

    matching = [""] * len(answers)
    matching[idx] = this_answer
    table = "+" + "-" * col_len + "+" + "-" * col_len + "+"
    table += (
            "\n| Valid Answers"
            + " " * (col_len - 14)
            + "| Best Match"
            + " " * (col_len - 11)
            + "|"
    )
    table += "\n+" + "-" * col_len + "+" + "-" * col_len + "+"

    for a, m in zip(answers, matching):
        entry_line = (
                f"\n| {a}"
                + " " * (col_len - len(a) - 1)
                + f"| {m}"
                + " " * (col_len - len(m) - 1)
                + "|"
        )
        table += entry_line
    table += "\n+" + "-" * col_len + "-" + "-" * col_len + "+"
    return table


def load_questions(yaml_path: Path) -> dict:
    """Load questions from a YAML file."""
    with open(yaml_path, 'r') as f:
        questions = yaml.safe_load(f)
    return questions


def main():
    parser = argparse.ArgumentParser(
        description="US Naturalization Test Quiz"
    )

    # Get the default path relative to the package
    default_yaml = Path(__file__).parent / "questions_NY_state_oct_2025.yaml"

    parser.add_argument(
        '--questions',
        type=Path,
        default=default_yaml,
        help=f'Path to questions YAML file (default: {default_yaml.name})'
    )

    args = parser.parse_args()

    # Load questions from YAML
    if not args.questions.exists():
        print(f"Error: Questions file not found at {args.questions}")
        print("Please provide a valid path using --questions")
        return

    questions_dict = load_questions(args.questions)
    num_questions = len(questions_dict)

    question_order = np.random.permutation(np.arange(num_questions))
    qa_list = [(q, a) for q, a in questions_dict.items()]
    count_correct = 0
    abort = False

    print(
        f"\n\nWelcome to the {num_questions} question quiz!\n\n"
        f"Using questions from: {args.questions.name}\n"
        "Answer 'exit' to quit at any time. Press 'enter' to continue."
    )
    input()

    for num, question_num in enumerate(question_order):
        current_question, current_answers = qa_list[question_num]
        print(f"Question #{num + 1} of {num_questions}:")
        print(f"{current_question}")
        user_answer = input()
        if user_answer == "exit":
            abort = True
            break
        match = find_similar(current_answers, user_answer)
        table = create_answer_table(current_answers, match, user_answer)
        print(table)
        while True:
            print("\nWas your answer correct? y/n")
            yn = input()
            if yn == "y":
                count_correct += 1
                break
            elif yn == "n":
                break
            else:
                print("Please enter either 'y' or 'n'.")

    if not abort:
        print(f"\nYour final score is {count_correct}/{num_questions}.")
        passing_score = int(num_questions * 0.8)
        if count_correct >= passing_score:
            print(f"\nYou passed the test!")
        else:
            print(f"\nYou failed! Never give up brother :D")


if __name__ == "__main__":
    main()