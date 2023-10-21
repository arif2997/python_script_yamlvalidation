import yaml
import sys

def validate_yaml(/c/Users/MOHAMMED ARIF/python_script_yamlvalidation):
    try:
        with open(/c/Users/MOHAMMED ARIF/python_script_yamlvalidation, 'r') as file:
            yaml.safe_load(/c/Users/MOHAMMED ARIF/python_script_yamlvalidation)
        print(f"YAML validation successful for {/c/Users/MOHAMMED ARIF/python_script_yamlvalidation}")
        return 0
    except Exception as e:
        print(f"YAML validation failed for {/c/Users/MOHAMMED ARIF/python_script_yamlvalidation}: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_yaml.py <yaml_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    sys.exit(validate_yaml(yaml_file))

