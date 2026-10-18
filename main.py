from rich.console import Console

questions: list[tuple[str,list[str],str]] = [
    ("the best CMS in the world?",["A:Word Press","B:Joomla","c:Drupal","D:Squarspace"],"A"),
    ("what is the most popular CMS?",["A:Word Press","B:Joomla","C:Drupal","D:Squarspace"],"A"),
    ("which CMS is known for its user-friendly interface?",["A:WordPress","B:Joomla","C:Drupal","D:Squaresp"], "A")
]
console = Console()
score=0
total_correct=0
CORRECT_BOUNES=10
PENALTY=3
for question , options , correct in questions:
    console.print(question,style="bold blue")
    for option in options:
        console.print(f"{option}/n")
    user_answer: str=input("your answer (A//B/C/D):").strip().upper()
    if user_answer==correct:
       total_correct +=1
       score += CORRECT_BOUNES
       console.print("correct!/n",style="bold cyan")
    else:
        score -=3
        console.print(f"Wrong! The correct answer is {correct}./n")

console.print(f"Your score is:{score}")
console.print(f"Total correct answer: {total_correct}")
print('hello')
















