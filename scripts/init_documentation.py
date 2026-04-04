import os
import json
import sys

def init_documentation_status(project_root, output_json):
    status = {}
    doc_dir = "documentation"
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

    for root, dirs, files in os.walk(project_root):
        # Skip hidden and system dirs
        if any(d.startswith('.') for d in root.split(os.sep)):
            continue
        if "node_modules" in root or "target" in root or "documentation" in root:
            continue

        for file in files:
            if file.endswith(('.java', '.cbl', '.jcl', '.p', '.cls', '.ts', '.js', '.c', '.cpp', '.h', '.sh', '.sql', '.pas')):
                relative_path = os.path.relpath(os.path.join(root, file), project_root)
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
    init_documentation_status(project_path, "documentation_status.json")
