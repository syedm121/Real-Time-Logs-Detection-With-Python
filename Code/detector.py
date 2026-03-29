from collections import defaultdict
from datetime import timedelta
from config import THRESHOLD, TIME_WINDOW
from alerts import send_alert

failed_attempts = defaultdict(list)


def process_failed_login(user, timestamp):
    failed_attempts[user].append(timestamp)

    cleanup_old_attempts(user, timestamp)
    check_bruteforce(user)


def cleanup_old_attempts(user, current_time):
    window_start = current_time - timedelta(seconds=TIME_WINDOW)

    failed_attempts[user] = [
        t for t in failed_attempts[user]
        if t >= window_start
    ]


def check_bruteforce(user):
    attempts = failed_attempts[user]

    if len(attempts) >= THRESHOLD:
        send_alert(
            user=user,
            attempt_count=len(attempts),
            last_attempt=attempts[-1]
        )

        # Reset after alert (avoid spam)
        failed_attempts[user].clear()
