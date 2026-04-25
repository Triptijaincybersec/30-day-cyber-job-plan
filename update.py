import json

def build_site():
    with open('progress.json', 'r') as f:
        data = json.load(f)

    html_days = ""
    total_days = 0
    completed_days = 0
    total_slots = 0
    completed_slots = 0

    for week in data['weeks']:
        for date, day_data in week['days'].items():
            total_days += 1
            slots_html = ""
            all_slots_done = True

            for time, slot in day_data['slots'].items():
                # Handle both old string format and new object format
                if isinstance(slot, dict):
                    task = slot['task']
                    done = slot.get('done', False)
                else:
                    task = slot
                    done = False
                
                total_slots += 1
                if done: completed_slots += 1
                if not done: all_slots_done = False
                checked = 'checked' if done else ''

                slots_html += f'''
                <label class="slot">
                  <input type="checkbox" {checked} disabled>
                  <span class="time">{time}</span> {task}
                </label>
                '''

            if all_slots_done: completed_days += 1
            day_class = 'completed' if all_slots_done else ''
            html_days += f'''
            <div class="day-card {day_class}">
              <h3>{day_data['title']}</h3>
              <div class="slots">{slots_html}</div>
            </div>
            '''

    day_percent = int((completed_days / total_days) * 100) if total_days else 0
    slot_percent = int((completed_slots / total_slots) * 100) if total_slots else 0

    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>30 Day Cyber Job Plan</title>
    <style>
        body {{ font-family: sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }}
       .progress {{ font-size: 20px; margin-bottom: 20px; color: #58a6ff; }}
       .day-card {{ border: 1px solid #30363d; padding: 15px; margin: 10px 0; border-radius: 6px; background: #161b22; }}
       .day-card.completed {{ border-left: 4px solid #3fb950; }}
       .slot {{ display: block; margin: 8px 0; }}
       .slot input {{ margin-right: 8px; accent-color: #3fb950; }}
       .time {{ color: #3fb950; font-weight: bold; margin-right: 8px; }}
       h3 {{ margin-top: 0; color: #58a6ff; }}
    </style>
</head>
<body>
    <div class="progress">Days: {completed_days}/{total_days} = {day_percent}% | Tasks: {completed_slots}/{total_slots} = {slot_percent}%</div>
    {html_days}
</body>
</html>'''

    with open('index.html', 'w') as f:
        f.write(html)

    print(f"Done. Days: {completed_days}/{total_days} = {day_percent}% | Tasks: {completed_slots}/{total_slots} = {slot_percent}%")

if __name__ == "__main__":
    build_site()