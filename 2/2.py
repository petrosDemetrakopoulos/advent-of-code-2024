def is_safe(report):
    if all(report[i] < report[i+1] and (report[i+1] - report[i] <= 3) for i in range(len(report)-1)):
        return True
    elif all(report[i] > report[i+1] and (report[i] - report[i+1] <= 3) for i in range(len(report)-1)):
        return True
    return False

def is_conditionally_safe(report):
    """
    Check if a report can become safe by removing one bad number.
    """
    for i in range(len(report)):
        # Create a new report with one element removed
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False
        

with open('input.txt', 'r') as file:
    safe_reports = 0
    for report in file:
        report = report.split()
        report = [int(x) for x in report]
        if is_safe(report) or is_conditionally_safe(report):
            safe_reports += 1
    print(safe_reports)