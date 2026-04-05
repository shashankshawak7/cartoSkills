import os
import json
from utils import load_ignore_map, should_skip, SUPPORTED_EXTENSIONS

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
                if any(item.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                    node["children"].append({
                        "name": item,
                        "path": os.path.relpath(full_path, target_dir),
                        "type": "file"
                    })
        return node

    return build_tree(target_dir)

def init_project(target_dir="."):
    target_abs_path = os.path.abspath(target_dir)
    project_name = os.path.basename(target_abs_path.rstrip(os.sep))
    if not project_name:
        project_name = "root"

    if not os.path.exists("results"):
        os.makedirs("results")
        
    tree = get_project_tree(target_abs_path)
    # Add project metadata to the tree
    tree["project_name"] = project_name
    
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
        "project_name": project_name,
        "files": files_to_process,
        "global_symbols": [],
        "total_files": len(files_to_process),
        "completed_files": 0,
        "root_dir": target_abs_path
    }
    
    with open("results/status.json", "w") as f:
        json.dump(status, f, indent=2)
    
    if not os.path.exists("results/graph.json"):
        with open("results/graph.json", "w") as f:
            json.dump({
                "nodes": [], 
                "edges": [], 
                "metadata": {
                    "version": "4.0.0",
                    "status": "CLEAN",
                    "project_name": project_name
                }
            }, f, indent=2)
            
    if not os.path.exists("results/symbol_table.json"):
        with open("results/symbol_table.json", "w") as f:
            json.dump({"project_name": project_name}, f, indent=2)

    print(f"Project '{project_name}' initialized.")
    print(f"Project Tree saved to results/project_tree.json")
    print(f"Found {len(files_to_process)} files to process.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Initialize AI Code Cartography project.")
    parser.add_argument("target_dir", nargs="?", default=".", help="Directory to analyze (default: current)")
    args = parser.parse_args()
    
    init_project(args.target_dir)
