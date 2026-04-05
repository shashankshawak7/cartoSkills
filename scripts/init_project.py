import os
import json

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
        # Check for exact matches or wildcard/prefix matches
        for d in all_dirs:
            if name == d:
                return True
            if d.endswith('*') and name.startswith(d[:-1]):
                return True
            if d.startswith('.') and name.startswith(d):
                return True
        return False
    else:
        # Check for exact matches or extension wildcards
        for f in all_files:
            if name == f:
                return True
            if f.startswith('*') and name.endswith(f[1:]):
                return True
        return False

def get_project_tree(target_dir="."):
    ignore_map = load_ignore_map()
    
    def build_tree(path):
        name = os.path.basename(path)
        if not name:
            name = "root"
        
        is_dir = os.path.isdir(path)
        if should_skip(path, name, is_dir, ignore_map):
            return None

        node = {
            "name": name,
            "path": os.path.relpath(path, target_dir) if path != target_dir else ".",
            "type": "folder",
            "children": []
        }
        
        try:
            items = os.listdir(path)
        except PermissionError:
            return None
            
        for item in sorted(items):
            full_path = os.path.join(path, item)
            child_is_dir = os.path.isdir(full_path)
            
            if should_skip(full_path, item, child_is_dir, ignore_map):
                continue
                
            if child_is_dir:
                child = build_tree(full_path)
                if child:
                    node["children"].append(child)
            else:
                # Use the same list of supported extensions as init_documentation
                extensions = [".java", ".cbl", ".jcl", ".p", ".cls", ".ts", ".tsx", ".js", ".jsx", ".c", ".cpp", ".h", ".cs", ".py", ".go", ".rs", ".rb", ".php", ".sh", ".sql", ".pas", ".yaml", ".yml", ".md", ".json", ".txt", ".html", ".css"]
                if any(item.endswith(ext) for ext in extensions):
                    node["children"].append({
                        "name": item,
                        "path": os.path.relpath(full_path, target_dir),
                        "type": "file"
                    })
        return node

    return build_tree(target_dir)

def init_project(target_dir="."):
    if not os.path.exists("results"):
        os.makedirs("results")
        
    tree = get_project_tree(target_dir)
    with open("results/project_tree.json", "w") as f:
        json.dump(tree, f, indent=2)
    
    files_to_process = []
    def flat_files(node):
        if node["type"] == "file":
            files_to_process.append({
                "path": node["path"],
                "status": "NOT_STARTED",
                "extracted_symbols": [],
                "error": None,
                "parsed_at": None
            })
        elif "children" in node:
            for child in node["children"]:
                flat_files(child)
                
    flat_files(tree)
    
    status = {
        "files": files_to_process,
        "global_symbols": [],
        "total_files": len(files_to_process),
        "completed_files": 0,
        "root_dir": os.path.abspath(target_dir)
    }
    
    with open("results/status.json", "w") as f:
        json.dump(status, f, indent=2)
    
    # Initialize empty graph and symbol table
    if not os.path.exists("results/graph.json"):
        with open("results/graph.json", "w") as f:
            json.dump({"nodes": [], "edges": []}, f, indent=2)
            
    if not os.path.exists("results/symbol_table.json"):
        with open("results/symbol_table.json", "w") as f:
            json.dump({}, f, indent=2)

    print(f"Project initialized.")
    print(f"Project Tree saved to results/project_tree.json")
    print(f"Found {len(files_to_process)} files to process.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Initialize AI Code Cartography project.")
    parser.add_argument("target_dir", nargs="?", default=".", help="Directory to analyze (default: current)")
    args = parser.parse_args()
    
    init_project(args.target_dir)
