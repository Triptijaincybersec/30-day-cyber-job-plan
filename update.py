import json
from datetime import datetime

def format_time_slot(time_str):
    """Convert 06-08 to 6:00 AM - 8:00 AM"""
    try:
        start, end = time_str.split('-')
        start_hr = int(start)
        end_hr = int(end)
        
        start_period = 'AM' if start_hr < 12 else 'PM'
        end_period = 'AM' if end_hr < 12 else 'PM'
        
        start_12 = start_hr if start_hr <= 12 else start_hr - 12
        end_12 = end_hr if end_hr <= 12 else end_hr - 12
        if start_12 == 0: start_12 = 12
        if end_12 == 0: end_12 = 12
        
        return f"{start_12}:00 {start_period} - {end_12}:00 {end_period}"
    except:
        return time_str

def get_day_info(date_str):
    """Get day name from date"""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%A')
    except:
        return ''

def build_site():
    with open('progress.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_days = []
    day_counter = 1
    
    for week in data['weeks']:
        for date, day_data in week['days'].items():
            day_name = get_day_info(date)
            
            all_days.append({
                'date': date,
                'day_num': day_counter,
                'day_name': day_name,
                'title': day_data['title'],
                'slots': day_data['slots'],
                'completed': day_data.get('completed', False)
            })
            day_counter += 1

    weeks_html = ""
    total_days = len(all_days)
    completed_days = 0
    total_slots = 0
    completed_slots = 0

    # Group into weeks of 7 days
    for week_start in range(0, total_days, 7):
        week_days = all_days[week_start:week_start + 7]
        days_html = ""
        week_completed_days = 0
        week_total_days = len(week_days)
        w_idx = (week_start // 7) + 1
        
        for day in week_days:
            slots_html = ""
            all_slots_done = True
            day_completed_slots = 0
            day_total_slots = 0
            is_sunday = day['day_name'] == 'Sunday'
            rest_tag = '<span class="rest-tag">Rest Day</span>' if is_sunday else ''

            for time, slot in day['slots'].items():
                if isinstance(slot, dict):
                    task = slot['task']
                    done = slot.get('done', False)
                else:
                    task = slot
                    done = False
                
                total_slots += 1
                day_total_slots += 1
                if done: 
                    completed_slots += 1
                    day_completed_slots += 1
                if not done: all_slots_done = False
                checked = 'checked' if done else ''
                
                time_formatted = format_time_slot(time)

                slots_html += f'''
                <label class="slot">
                  <input type="checkbox" {checked} disabled>
                  <span class="checkmark"></span>
                  <span class="time">{time_formatted}</span> {task}
                </label>
                '''

            if all_slots_done: 
                completed_days += 1
                week_completed_days += 1
            
            day_percent = int((day_completed_slots / day_total_slots) * 100) if day_total_slots else 0
            day_class = 'completed' if all_slots_done else ''
            day_class += ' sunday' if is_sunday else ''
            
            # Format: Day 1 (Saturday) : Setup
            days_html += f'''
            <details class="day-folder {day_class}">
              <summary>
                <span class="folder-icon">📁</span>
                Day {day['day_num']} ({day['day_name']}) : {day['title']}
                {rest_tag}
                <span class="day-progress">{day_completed_slots}/{day_total_slots} = {day_percent}%</span>
              </summary>
              <div class="slots">{slots_html}</div>
            </details>
            '''
        
        week_percent = int((week_completed_days / week_total_days) * 100) if week_total_days else 0
        weeks_html += f'''
        <details class="week-folder" open>
          <summary>
            <span class="folder-icon">📂</span>
            Week {w_idx}
            <span class="week-progress">Days: {week_completed_days}/{week_total_days} = {week_percent}%</span>
          </summary>
          <div class="days">{days_html}</div>
        </details>
        '''

    day_percent = int((completed_days / total_days) * 100) if total_days else 0
    slot_percent = int((completed_slots / total_slots) * 100) if total_slots else 0

    html = f'''<!DOCTYPE html>
<html>
<head>
    <title>30 Day Cyber Job Plan</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
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
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .header h1 {{
            font-size: 32px;
            font-weight: 700;
            color: #58a6ff;
            margin: 0 0 10px 0;
        }}
        .progress {{
            font-size: 18px;
            font-weight: 600;
            padding: 16px 20px;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(88, 166, 255, 0.2);
            text-align: center;
            margin-bottom: 20px;
        }}
        .week-folder {{
            border: 1px solid #30363d;
            margin: 16px 0;
            border-radius: 12px;
            background: #161b22;
            overflow: hidden;
        }}
        .week-folder summary {{
            padding: 16px 20px;
            font-size: 20px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            background: #1c2128;
            list-style: none;
        }}
        .week-folder summary::-webkit-details-marker {{ display: none; }}
        .week-folder summary:hover {{ background: #21262d; }}
        .week-progress {{
            margin-left: auto;
            font-size: 14px;
            color: #3fb950;
            font-weight: 600;
        }}
        .days {{ padding: 0 10px 10px 10px; }}
        .day-folder {{
            border: 1px solid #30363d;
            margin: 12px 0;
            border-radius: 8px;
            background: #0d1117;
        }}
        .day-folder.sunday {{
            border-color: #1f6feb;
            background: #0c162d;
        }}
        .day-folder summary {{
            padding: 14px 16px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            list-style: none;
            flex-wrap: wrap;
        }}
        .day-folder summary::-webkit-details-marker {{ display: none; }}
        .day-folder summary:hover {{ background: #161b22; }}
        .day-folder.completed summary {{ color: #3fb950; }}
        .rest-tag {{
            background: #1f6feb;
            color: #fff;
            font-size: 11px;
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 700;
            text-transform: uppercase;
        }}
        .day-progress {{
            margin-left: auto;
            font-size: 13px;
            color: #8b949e;
        }}
        .folder-icon {{ font-size: 18px; }}
        .slots {{ padding: 8px 16px 16px 16px; }}
        .slot {{
            display: flex;
            align-items: center;
            margin: 10px 0;
            padding: 8px;
            border-radius: 6px;
            position: relative;
        }}
        .slot:hover {{ background: #161b22; }}
        .slot input {{
            position: absolute;
            opacity: 0;
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
            min-width: 140px;
            font-size: 13px;
        }}
        .slot input:checked ~ .time,
        .slot input:checked ~ span:last-child {{
            opacity: 0.6;
            text-decoration: line-through;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>30 Days Cyber Job Plan</h1>
    </div>
    <div class="progress">Days: {completed_days}/{total_days} = {day_percent}% | Tasks: {completed_slots}/{total_slots} = {slot_percent}%</div>
    {weeks_html}
</body>
</html>'''

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Done. Days: {completed_days}/{total_days} = {day_percent}% | Tasks: {completed_slots}/{total_slots} = {slot_percent}%")

if __name__ == "__main__":
    build_site()