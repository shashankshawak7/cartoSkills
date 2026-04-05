import os
import json
import sys
from utils import load_ignore_map, should_skip, SUPPORTED_EXTENSIONS

def init_documentation_status(project_root, output_json):
    status = {}
    ignore_map = load_ignore_map()
    doc_dir = "documentation"
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    project_root = os.path.abspath(project_root)
    for root, dirs, files in os.walk(project_root):
        # Dynamically exclude ignored directories from the walk
        dirs[:] = [d for d in dirs if not should_skip(os.path.join(root, d), d, True, ignore_map)]
        
        # Skip hidden and system dirs
        if any(d.startswith('.') for d in root.split(os.sep)):
            continue
            
        current_root_name = os.path.basename(root)
        if should_skip(root, current_root_name, True, ignore_map):
            continue

        for file in files:
            # Check if individual file should be skipped
            if should_skip(os.path.join(root, file), file, False, ignore_map):
                continue
                
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                relative_path = os.path.relpath(os.path.join(root, file), project_root)
                # Ensure status uses 'status' naming for consistency where possible or keep 'documented' for doc engine
                status[relative_path] = {
                    "mapped": False,
                    "documented": False,
                    "hyper_detailed": False,
                    "diagram_verified": False,
                    "batch": None
                }

    with open(output_json, 'w') as f:
        json.dump(status, f, indent=2)
    print(f"Retro Documentation seeds generated: {len(status)} files tracked from {project_root}")

if __name__ == "__main__":
    project_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    init_documentation_status(project_path, os.path.join(results_dir, "documentation_status.json"))
