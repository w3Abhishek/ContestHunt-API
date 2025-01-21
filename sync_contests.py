import os
import importlib
from dbmanager import update_items

EXTRACTORS_DIR = "extractors"
contest_platforms = ['atcoder', 'code360', 'codechef', 'codeforces', 'csacademy', 'geeksforgeeks', 'hackerearth', 'leetcode', 'nowcoder', 'topcoder']
hackathon_platforms = ['devfolio', 'devpost', 'unstop']
bounty_platforms = ['replit']
def run_extractors():
    extractor_files = [
        f for f in os.listdir(EXTRACTORS_DIR)
        if f.endswith(".py") and f != "__init__.py"
    ]

    for file_name in extractor_files:
        module_name = f"{EXTRACTORS_DIR}.{file_name[:-3]}"
        
        try:
            extractor_module = importlib.import_module(module_name)
            response = extractor_module.fetch_contests()
            if file_name[:-3] in hackathon_platforms:
                update_items("hackathons", response)
            if file_name[:-3] in contest_platforms:
                update_items("contests", response)
            if file_name[:-3] in bounty_platforms:
                update_items("bounties", response)
        except Exception as e:
            print(f"Error running extractor {module_name}: {e}")

if __name__ == "__main__":
    run_extractors()