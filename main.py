"""
Simple log-file analyzer.
"""

import sys
from collections import Counter

def display_log_counts(counts: dict):
    """
    Print a simple table of log levels and their counts.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key:<17}| {value}")

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Return logs filtered by a given log level.
    """
    return list(filter(lambda log: log["level"] == level, logs))

def display_logs(logs: list, level: str):
    """
    Print detailed log lines for a specific level.
    """
    print("")
    print(f"Деталі логів для рівня '{level}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def count_logs_by_level(logs: list) -> dict:
    """
    Count logs per level and return a dict level->count.
    """
    logs_by_level = Counter(log["level"] for log in logs)
    return dict(logs_by_level)

def parse_log_line(line: str) -> dict:
    """
    Parse a single log line into its components.
    """
    if not line:
        return {}
    log = line.split()
    if len(log) < 3:
        return {}
    return {
        "date": log[0],
        "time": log[1],
        "level": log[2],
        "message": ' '.join(log[3:])
    }

def load_logs(file_path: str) -> list :
    """
    Load logs from a text file and return a list of parsed log dicts.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
        return logs
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from exc
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}") from e

def main():
    """Entry point: load the file given on the command line and show stats.
    Usage: python main.py <log_file> [LEVEL]
    """
    if len(sys.argv) < 2:
        return
    file_path = sys.argv[1]
    logs = load_logs(file_path)
    display_log_counts(count_logs_by_level(logs))
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        display_logs(filter_logs_by_level(logs, level), level)

if __name__ == "__main__" :
    main()
