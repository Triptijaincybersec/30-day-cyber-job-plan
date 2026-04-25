import json
import datetime

def build_site():
    # 1. Load your JSON data
    with open('progress.json', 'r') as f:
        data = json.load(f)

    # 2. Generate HTML for each day
    html_days = ""
    total_days = 0
    completed_days = 0

    for week in data['weeks']:
        for date, day_data in week['days'].items():
            total_days += 1
            slots_html = ""
            all_slots_done = True

            # Build subtask checkboxes
            for time, slot in day_data['slots'].items():
                task = slot['task'] if isinstance(slot, dict) else slot
                done = slot.get('done', False) if isinstance(slot, dict) else False

                if not done: all_slots_done = False
                checked = 'checked' if done else ''

                slots_html += f'''
                <label class="slot">
                  <input type="checkbox" {checked} disabled>
                  <span class="time">{time}</span> {task}
                </label>
                '''

            # Auto-complete day if all slots done
            day_data['completed'] = all_slots_done
            if all_slots_done: completed_days += 1

            day_class = 'completed' if all_slots_done else ''
            html_days += f'''
            <div class="day-card {day_class}">
              <h3>{day_data['title']}</h3>
              <div class="slots">{slots_html}</div>
            </div>
            '''

    # 3. Calculate %
    percent = int((completed_days / total_days) * 100) if total_days else 0

    # 4. Write full index.html
    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>30 Day Cyber Job Plan</title>
    <style>
        body {{ font-family: sans-serif; background: #111; color: #eee; padding: 20px; }}
       .day-card {{ border: 1px solid #333; padding: 15px; margin: 10px 0; border-radius: 8px; }}
       .day-card.completed {{ border-left: 4px solid #00ff88; }}
       .slot {{ display: block; margin: 8px 0; }}
       .slot.time {{ color: #00ff88; font-weight: bold; margin-right: 8px; }}
       .progress {{ font-size: 24px; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="progress">Progress: {completed_days}/{total_days} Days = {percent}%</div>
    {html_days}
</body>
</html>'''

    with open('index.html', 'w') as f:
        f.write(html)

    print(f"Done. Site rebuilt. {completed_days}/{total_days} days complete = {percent}%")

if __name__ == "__main__":
    build_site()
