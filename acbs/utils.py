
import os
import fnmatch

def search_csvs(path: str, tipo: str) -> list:
    csv_files: list = []

    for root, _, files, in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, f"{tipo}-*.csv"):
                csv_files.append(file)

    return csv_files
