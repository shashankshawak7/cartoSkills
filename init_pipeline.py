import os
import sys
import subprocess
import argparse

"""
init_pipeline.py (Master Orchestration Script)

Logic Parity: 100% (Unified Pipeline)
Refactored to accept a project directory and call modular initialization scripts.
"""
def run_script(script_name, project_root):
    script_path = os.path.join(os.path.dirname(__file__), "scripts", script_name)
    print(f"🔄 Executing: {script_name}...")
    try:
        subprocess.run([sys.executable, script_path, project_root], check=True)
        print(f"✅ Success: {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {script_name} failed with exit code {e.returncode}")
        sys.exit(1)

def initialize_universal_pipeline(project_root):
    print("🚀 Initializing Universal SKILLaI Pipeline (Resumable V2.0)...")
    
    # Ensure results directory exists
    results_dir = os.path.join(project_root, "results")
    os.makedirs(results_dir, exist_ok=True)

    # Sequence of Initialization
    init_scripts = [
        "init_project.py",      # Cartesian (Phase 1)
        "init_documentation.py",# Retro Documentor (Phase 2)
        "init_irmapper.py",     # IRMapper (Phase 3)
        "init_modernizer.py"    # Digital Modernizer (Phase 4)
    ]

    for script in init_scripts:
        run_script(script, project_root)

    print("\n🎉 Unified Pipeline Initialized.")
    print("Next Steps: Run Modernizer Orchestrator to begin state-aware transformation.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize the Unified SKILLaI ALM Pipeline.")
    parser.add_argument("project_dir", nargs="?", default=".", help="Target project directory (default: current)")
    args = parser.parse_args()
    
    project_abs_path = os.path.abspath(args.project_dir)
    initialize_universal_pipeline(project_abs_path)
