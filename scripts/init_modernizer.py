import os
import json
import argparse

"""
init_modernizer.py (Modernizer Tracker Initialization)

Logic Parity: 100% (IRMapper Mapping Integrity)
Seeds the results/modernization_status.json based on existing IRMapper data.
"""
def init_modernization_status(project_root):
    results_dir = os.path.join(project_root, "results")
    irmapper_file = os.path.join(results_dir, "irmapper_status.json")
    output_file = os.path.join(results_dir, "modernization_status.json")
    
    if not os.path.exists(irmapper_file):
        print(f"⚠️ IRMapper status not found. Initializing empty modernization queue.")
        irmapper_data = []
    else:
        with open(irmapper_file, 'r') as f:
            irmapper_data = json.load(f)

    modernization_status = []
    # If irmapper_data is a dictionary (from init_irmapper.py)
    if isinstance(irmapper_data, dict):
        for file_path, entry in irmapper_data.items():
            modernization_status.append({
                "file": file_path,
                "mapped": entry.get("mapped", False),
                "modernized": False,
                "target_stack": "PENDING",
                "test_generated": False,
                "error_log": None,
                "retry_count": 0
            })
    # If it's a list (legacy format)
    else:
        for entry in irmapper_data:
            modernization_status.append({
                "file": entry["file"],
                "mapped": entry.get("mapped", False),
                "modernized": False,
                "target_stack": "PENDING",
                "test_generated": False,
                "error_log": None,
                "retry_count": 0
            })

    with open(output_file, 'w') as f:
        json.dump(modernization_status, f, indent=2)

    print(f"✅ Modernization tracker seeded: {len(modernization_status)} items tracked in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize Digital Modernization Tracker")
    parser.add_argument("project_root", help="Path to the project root directory")
    args = parser.parse_args()
    init_modernization_status(args.project_root)
