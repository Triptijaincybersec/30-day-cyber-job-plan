import datetime
import json

def mark_today():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Marking {today} as complete")
    print("1. Open README.md")
    print("2. Find today's date and change - [ ] to - [x]")
    print("3. git add README.md")
    print(f"4. git commit -m 'Day complete: {today}'")
    print("5. git push")
    print("\nDone. Recruiter can see daily commits = consistency.")

if __name__ == "__main__":
    mark_today()
