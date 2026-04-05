import os
import json
import argparse

def init_irmapper(project_root):
    project_abs_path = os.path.abspath(project_root)
    project_name = os.path.basename(project_abs_path.rstrip(os.sep))
    if not project_name:
        project_name = "root"

    status_file = os.path.join("results", "irmapper_status.json")
    project_tree_file = os.path.join("results", "project_tree.json")
    
    if not os.path.exists(project_tree_file):
        print(f"Error: {project_tree_file} not found. Run init_project.py first.")
        return

    with open(project_tree_file, 'r') as f:
        tree = json.load(f)

    irmapper_status = {}

    def walk_tree(node):
        if node['type'] == 'file':
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

    output_data = {
        "project_name": project_name,
        "files": irmapper_status
    }

    if not os.path.exists("irmapper"):
        os.makedirs("irmapper")
    
    project_irmapper_dir = os.path.join("irmapper", project_name)
    if not os.path.exists(project_irmapper_dir):
        os.makedirs(project_irmapper_dir)

    with open(status_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"Initialized IRMapper status for '{project_name}' in {status_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize IRMapper Status Tracker")
    parser.add_argument("project_root", help="Path to the project root")
    args = parser.parse_args()
    init_irmapper(args.project_root)
