# Smart Log File Analyzer
# Reads a log file and counts INFO, WARNING, and ERROR messages

log_file = "sample.log"

info_count = 0
warning_count = 0
error_count = 0

try:
    with open(log_file, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("INFO"):
                info_count += 1
            elif line.startswith("WARNING"):
                warning_count += 1
            elif line.startswith("ERROR"):
                error_count += 1

    print("Log Analysis Report")
    print("\n")
    print("INFO logs    :", info_count)
    print("WARNING logs :", warning_count)
    print("ERROR logs   :", error_count)

except FileNotFoundError:
    print("Log file not found. Please check the file name.")
