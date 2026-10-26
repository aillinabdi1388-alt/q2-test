from rich.console import Console

questions: list[tuple[str,list[str],str]] = [
    ("the best CMS in the world?",["A:Word Press","B:Joomla","c:Drupal","D:Squarspace"],"A"),
    ("what is the most popular CMS?",["A:Word Press","B:Joomla","C:Drupal","D:Squarspace"],"A"),
    ("which CMS is known for its user-friendly interface?",["A:WordPress","B:Joomla","C:Drupal","D:Squaresp"], "A")
]
console = Console()
def show_results(score,total_correct):
    console.print(f"Your score is:{score}",style="red on white")
    console.print(f"Total correct answer: {total_correct}",style="red on white")

def play_match():
    score=0
    total_correct=0
    CORRECT_BOUNES=10
    PENALTY=3
    for question , options , correct in questions:
        console.print(question,style="bold blue")
        for option in options:
            console.print(f"{option}/n",style="red on white")
        user_answer: str=input("your answer (A//B/C/D):").strip().upper()
        if user_answer==correct:
            total_correct +=1
            score += CORRECT_BOUNES
            console.print("correct!/n",style="bold cyan")
        else:
            score -=3
            console.print(f"Wrong! The correct answer is {correct}./n")
    return score,total_correct




score,total_correct = play_match()
show_results(score,total_correct)

















