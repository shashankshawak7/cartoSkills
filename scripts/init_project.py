import os
import json

def get_project_tree(target_dir="."):
    ignore_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", "dist", "build"}
    ignore_files = {".gitignore", "package-lock.json", "poetry.lock", "status.json", "graph.json", "project_tree.json", "symbol_table.json"}
    
    def build_tree(path):
        name = os.path.basename(path)
        if not name:
            name = "root"
        
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
            if item in ignore_dirs or item in ignore_files:
                continue
                
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                child = build_tree(full_path)
                if child:
                    node["children"].append(child)
            else:
                if any(item.endswith(ext) for ext in [".py", ".js", ".ts", ".java", ".cpp", ".c", ".go"]):
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
