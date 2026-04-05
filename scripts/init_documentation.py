import os
import json
import sys

def init_documentation_status(project_root, output_json):
    status = {}
    doc_dir = "documentation"
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

def load_ignore_map():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "ignore_map.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {"global": {"directories": [], "files": []}}

def should_skip(path, name, is_dir, ignore_map):
    all_dirs = []
    all_files = []
    for category in ignore_map.values():
        all_dirs.extend(category.get("directories", []))
        all_files.extend(category.get("files", []))
    
    if is_dir:
        for d in all_dirs:
            if name == d:
                return True
            if d.endswith('*') and name.startswith(d[:-1]):
                return True
            if d.startswith('.') and name.startswith(d):
                return True
        return False
    else:
        for f in all_files:
            if name == f:
                return True
            if f.startswith('*') and name.endswith(f[1:]):
                return True
        return False

def init_documentation_status(project_root, output_json):
    status = {}
    ignore_map = load_ignore_map()
    doc_dir = "documentation"
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)

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
                
            extensions = [".java", ".cbl", ".jcl", ".p", ".cls", ".ts", ".tsx", ".js", ".jsx", ".c", ".cpp", ".h", ".cs", ".py", ".go", ".rs", ".rb", ".php", ".sh", ".sql", ".pas", ".yaml", ".yml", ".html"]
            if any(file.endswith(ext) for ext in extensions):
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
