from datetime import datetime

def generate_log(data):
    # validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # filename format: log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # write file
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

    # confirmation message
    print(f"Log file {filename} created successfully")

    return filename