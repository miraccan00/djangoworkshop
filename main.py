import subprocess
from djangostart.continues_integration import continues_integration
from updatehelmchart import update_helm_chart_image_tag
from gitcommit import commit

def install_project():
    subprocess.run(['sh', 'start.sh'])
    
def main():
    while True:
        print("1. Continues integration")
        option = input("Select option: ")
        if option == "1":
            continues_integration("microservicename", "1.0.3")
            values_file_path = "deploymentchart/values.yaml"
            new_image_tag = "1.0.3"
            update_helm_chart_image_tag(values_file_path, new_image_tag)
            commit()
            subprocess.run(['sh', 'argocontinuesdeployment'])
        else:
            print("Invalid option")
            exit(1)

if __name__ == "__main__":
    main()