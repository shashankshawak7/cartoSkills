import os
import json
import argparse

def init_irmapper(project_root):
    status_file = os.path.join(project_root, "results", "irmapper_status.json")
    project_tree_file = os.path.join(project_root, "results", "project_tree.json")
    
    if not os.path.exists(project_tree_file):
        print(f"Error: {project_tree_file} not found. Run init_project.py first.")
        return

    with open(project_tree_file, 'r') as f:
        tree = json.load(f)

    irmapper_status = {}

    def walk_tree(node):
        if node['type'] == 'file':
            # Skip non-source files if desired, but for now we follow the project tree
            irmapper_status[node['path']] = {
                "mapped": False,
                "logic_mapped": False,
                "statement_level": False,
                "checksum": None
            }
        elif 'children' in node:
            for child in node['children']:
                walk_tree(child)

    walk_tree(tree)

    with open(status_file, 'w') as f:
        json.dump(irmapper_status, f, indent=2)

    print(f"Initialized IRMapper status in {status_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize IRMapper Status Tracker")
    parser.add_argument("project_root", help="Path to the project root")
    args = parser.parse_args()
    init_irmapper(args.project_root)
