import json
import os
import sys
import jsonschema

def load_json(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Could not find {filepath}")
        return None
    with open(filepath, 'r') as f:
        return json.load(f)

def validate_against_schema(data, schema_file):
    import jsonschema

    schemas_dir = os.path.join(os.path.dirname(__file__), "..", "schemas")
    schema_path = os.path.join(schemas_dir, schema_file)
    schema = load_json(schema_path)
    if not schema:
        return False

    # Create a resolver for local file references
    schema_uri = "file:///" + schemas_dir.replace("\\", "/") + "/"
    resolver = jsonschema.RefResolver(base_uri=schema_uri, referrer=schema)

    try:
        jsonschema.validate(instance=data, schema=schema, resolver=resolver)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"\n[!] JSON Schema Validation Error in {schema_file}:")
        print(f"Path: {' -> '.join([str(p) for p in e.absolute_path])}")
        print(f"Error: {e.message}")
        return False
    except Exception as e:
        print(f"\n[ERROR] Unexpected validation error: {str(e)}")
        return False

def check_dangling_edges(graph_data, symbol_data):
    nodes = {node["id"] for node in graph_data.get("nodes", [])}
    
    # Symbols in symbol table should ideally be nodes too, but at least collect them
    symbols = {symbol["id"] for symbol in symbol_data.values()} if isinstance(symbol_data, dict) else set()
    for symbol_list in symbol_data.values() if isinstance(symbol_data, dict) else []:
        # Handle dicts vs lists in symbol table according to schema if needed
        pass

    valid_targets = nodes.union(symbols)
    dangling = []

    for edge in graph_data.get("edges", []):
        target = edge.get("target")
        if target and target not in valid_targets:
            dangling.append({"source": edge.get("source"), "target": target, "type": edge.get("type")})

    if dangling:
        print("\n[!] Zero-Trust Violation: Dangling Edges Detected!")
        for err in dangling:
            print(f"Edge from '{err['source']}' targets non-existent '{err['target']}' (Type: {err['type']})")
        return False
    return True

def run():
    print("Initiating Zero-Trust Validation Pipeline...")
    
    root_dir = os.path.join(os.path.dirname(__file__), "..")
    graph_path = os.path.join(root_dir, "results", "graph.json")
    symbol_path = os.path.join(root_dir, "results", "symbol_table.json")

    graph = load_json(graph_path)
    symbol_table = load_json(symbol_path)
    
    if graph is None or symbol_table is None:
        sys.exit(1)

    isValid = True
    
    print("Validating graph.json against graph.schema.json...")
    if not validate_against_schema(graph, "graph.schema.json"):
        isValid = False

    # Need symbol_table schema check if defined, here we focus on graph
    print("Checking for Dangling Edges...")
    if not check_dangling_edges(graph, symbol_table):
        isValid = False

    if isValid:
        print("\n[SUCCESS] Enterprise Validation Passed. 100% Trust Verified.")
        sys.exit(0)
    else:
        print("\n[FAILURE] Enterprise Validation Failed. Halting pipeline.")
        sys.exit(1)

if __name__ == "__main__":
    run()
