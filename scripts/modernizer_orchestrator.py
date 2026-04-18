import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger("ModernizerOrchestrator")

"""
ModernizerOrchestrator (State-Aware Engine)

Manages the Digital Modernization queue, ensuring resumability and 
logic parity tracking across batch transformations.
"""
class ModernizerOrchestrator:
    def __init__(self, project_root):
        self.project_root = project_root
        self.results_dir = os.path.join(project_root, "results")
        self.status_file = os.path.join(self.results_dir, "modernization_status.json")
        self.status_data = self._load_status()

    def _load_status(self):
        if not os.path.exists(self.status_file):
            logger.error(f"❌ Status file not found: {self.status_file}. Run init_modernizer.py first.")
            return []
        with open(self.status_file, 'r') as f:
            return json.load(f)

    def _save_status(self):
        with open(self.status_file, 'w') as f:
            json.dump(self.status_data, f, indent=2)

    def get_pending_tasks(self):
        """Returns files that are mapped but not yet modernized."""
        return [entry for entry in self.status_data if entry.get("mapped") and not entry.get("modernized")]

    def mark_as_started(self, file_path, target_stack):
        """Marks a file as in-progress."""
        for entry in self.status_data:
            if entry["file"] == file_path:
                entry["target_stack"] = target_stack
                entry["error_log"] = None
                self._save_status()
                logger.info(f"🚀 Modernization STARTED: {file_path} -> {target_stack}")
                break

    def finalize_modernization(self, file_path, test_generated=True):
        """Finalizes the modernization state for a file."""
        for entry in self.status_data:
            if entry["file"] == file_path:
                entry["modernized"] = True
                entry["test_generated"] = test_generated
                self._save_status()
                logger.info(f"✅ Modernization COMPLETE: {file_path}")
                break

    def log_failure(self, file_path, error_msg):
        """Logs a failure and increments retry count."""
        for entry in self.status_data:
            if entry["file"] == file_path:
                entry["error_log"] = error_msg
                entry["retry_count"] = entry.get("retry_count", 0) + 1
                self._save_status()
                logger.error(f"❌ Modernization FAILED: {file_path} - {error_msg}")
                break

    def run_autonomous(self, process_callback):
        """
        Drives the modernization process autonomously until the queue is empty.
        'process_callback' should be a function that takes (file_path, target_stack) 
        and returns success (bool).
        """
        pending = self.get_pending_tasks()
        if not pending:
            logger.info("✅ Modernization queue is empty. Zero-Touch Completion achieved.")
            return

        logger.info(f"🦾 Starting Autonomous Modernization: {len(pending)} files remaining.")
        
        for task in pending:
            file_path = task["file"]
            target_stack = task.get("target_stack", "MODERN_STACK") # Default if pending
            
            self.mark_as_started(file_path, target_stack)
            
            try:
                success = process_callback(file_path, target_stack)
                if success:
                    self.finalize_modernization(file_path)
                else:
                    self.log_failure(file_path, "Process callback returned failure.")
            except Exception as e:
                self.log_failure(file_path, str(e))

if __name__ == "__main__":
    import sys
    project_root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    orchestrator = ModernizerOrchestrator(project_root)
    
    if "--run-all" in sys.argv:
        # This is a placeholder for actual autonomous execution via AI worker
        logger.info("🦾 Zero-Touch Autonomous Mode Requested.")
        pending = orchestrator.get_pending_tasks()
        print(f"Pending tasks: {len(pending)}")
    else:
        pending = orchestrator.get_pending_tasks()
        print(f"📊 Modernization Queue Status:")
        print(f"   - Project: {orchestrator.status_data.get('project_name', 'Unknown')}")
        print(f"   - Total Files: {len(orchestrator.status_data.get('files', []))}")
        print(f"   - Pending Modernization: {len(pending)}")
