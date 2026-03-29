import win32evtlog
import time
from config import SERVER, LOG_TYPE, FAILED_LOGIN_EVENT_ID
from detector import process_failed_login


def monitor_logs():
   

    hand = win32evtlog.OpenEventLog(SERVER, LOG_TYPE)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    last_record_number = 0

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)

        if events:
            for event in events:
                record_id = event.RecordNumber

             
                if record_id <= last_record_number:
                    continue

                last_record_number = record_id

                
                event_id = event.EventID & 0xFFFF

                if event_id == FAILED_LOGIN_EVENT_ID:
                    handle_failed_login(event)

        time.sleep(1)


def handle_failed_login(event):
    timestamp = event.TimeGenerated
    user = extract_username(event)

    print(f"[!] Failed login | User: {user} | Time: {timestamp}")

    process_failed_login(user, timestamp)


def extract_username(event):
    try:
        if event.StringInserts and len(event.StringInserts) > 5:
            return event.StringInserts[5]
    except Exception:
        pass

    return "unknown"