import os
import json
import argparse

"""
init_modernizer.py (Modernizer Tracker Initialization)

Logic Parity: 100% (IRMapper Mapping Integrity)
Seeds the results/modernization_status.json based on existing IRMapper data.
"""
def init_modernization_status(project_root):
    project_abs_path = os.path.abspath(project_root)
    project_name = os.path.basename(project_abs_path.rstrip(os.sep))
    if not project_name:
        project_name = "root"

    results_dir = "results"
    irmapper_file = os.path.join(results_dir, "irmapper_status.json")
    output_file = os.path.join(results_dir, "modernization_status.json")
    
    if not os.path.exists(irmapper_file):
        print(f"⚠️ IRMapper status not found. Initializing empty modernization queue.")
        irmapper_data = {"project_name": project_name, "files": {}}
    else:
        with open(irmapper_file, 'r') as f:
            irmapper_data = json.load(f)

    modernization_status = []
    
    files_data = irmapper_data.get("files", {})
    if isinstance(files_data, dict):
        for file_path, entry in files_data.items():
            modernization_status.append({
                "file": file_path,
                "mapped": entry.get("mapped", False),
                "modernized": False,
                "target_stack": "PENDING",
                "test_generated": False,
                "error_log": None,
                "retry_count": 0
            })
    else:
        # Fallback for legacy format
        for entry in files_data:
            modernization_status.append({
                "file": entry["file"],
                "mapped": entry.get("mapped", False),
                "modernized": False,
                "target_stack": "PENDING",
                "test_generated": False,
                "error_log": None,
                "retry_count": 0
            })

    output_data = {
        "project_name": project_name,
        "files": modernization_status
    }

    if not os.path.exists("modernizer"):
        os.makedirs("modernizer")
    
    project_modernizer_dir = os.path.join("modernizer", project_name)
    if not os.path.exists(project_modernizer_dir):
        os.makedirs(project_modernizer_dir)

    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=2)

    print(f"✅ Modernization tracker for '{project_name}' seeded: {len(modernization_status)} items tracked in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize Digital Modernization Tracker")
    parser.add_argument("project_root", help="Path to the project root directory")
    args = parser.parse_args()
    init_modernization_status(args.project_root)
