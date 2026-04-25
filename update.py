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
                  <span class="checkmark"></span>
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
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        * {{ box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: #0d1117;
            color: #e6edf3;
            padding: 20px;
            max-width: 900px;
            margin: 0 auto;
            line-height: 1.6;
        }}
        
       .progress {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 30px;
            padding: 16px 20px;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(88, 166, 255, 0.2);
            text-align: center;
        }}
        
       .day-card {{
            border: 1px solid #30363d;
            padding: 20px;
            margin: 16px 0;
            border-radius: 12px;
            background: #161b22;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        }}
        
       .day-card:hover {{ transform: translateY(-2px); }}
       .day-card.completed {{ border-left: 4px solid #3fb950; }}
        
       .day-card h3 {{
            margin: 0 0 16px 0;
            color: #58a6ff;
            font-size: 20px;
            font-weight: 700;
        }}
        
       .slot {{
            display: flex;
            align-items: center;
            margin: 12px 0;
            padding: 8px;
            border-radius: 6px;
            cursor: default;
            position: relative;
        }}
        
       .slot:hover {{ background: #21262d; }}
        
       .slot input {{
            position: absolute;
            opacity: 0;
            cursor: default;
        }}
        
       .checkmark {{
            height: 20px;
            width: 20px;
            background-color: #21262d;
            border: 2px solid #30363d;
            border-radius: 4px;
            margin-right: 12px;
            flex-shrink: 0;
            position: relative;
        }}
        
       .slot input:checked ~ .checkmark {{
            background-color: #3fb950;
            border-color: #3fb950;
        }}
        
       .slot input:checked ~ .checkmark:after {{
            content: "";
            position: absolute;
            left: 6px;
            top: 2px;
            width: 5px;
            height: 10px;
            border: solid #000;
            border-width: 0 3px 3px 0;
            transform: rotate(45deg);
        }}
        
       .time {{
            color: #3fb950;
            font-weight: 600;
            margin-right: 10px;
            min-width: 55px;
            font-size: 14px;
        }}
        
       .slot input:checked ~ .time,
       .slot input:checked ~ span:last-child {{
            opacity: 0.6;
            text-decoration: line-through;
        }}
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