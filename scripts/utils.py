import os
import json

SUPPORTED_EXTENSIONS = [
    ".java", ".cbl", ".jcl", ".p", ".cls", ".ts", ".tsx", ".js", ".jsx", 
    ".c", ".cpp", ".h", ".cs", ".py", ".go", ".rs", ".rb", ".php", 
    ".sh", ".sql", ".pas", ".yaml", ".yml", ".md", ".json", ".txt", ".html", ".css",
    ".xml", ".rex", ".rdf"
]

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
