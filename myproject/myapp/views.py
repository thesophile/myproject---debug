from django.shortcuts import render
from django.conf import settings
import subprocess
import os


def run_manim_command():
    try:

        current_directory = os.getcwd()

        #base_dir = '/home/sophile/Projects/django/myproject' 

        manim_command = f'sudo docker run -v {current_directory}/python_code_files:/mnt/code -v {current_directory}/media:/mnt/output manimcommunity/manim manim -ql /mnt/code/user_code.py -o /mnt/output/just_name'


        print(f"Running Manim command: {manim_command}")

        process = subprocess.Popen(
            manim_command,
            shell=True,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
            )

        stdout, stderr = process.communicate()

        print("STDOUT:", stdout)
        print("STDERR:", stderr)
        print("Proceeding to the next step...")

    except subprocess.CalledProcessError as e:
        # Handle the case when the command returns a non-zero exit code
        print("Docker command failed with return code:", e.returncode)
        print(e.stderr)
    except Exception as e:
        # Handle any other exceptions that may occur
        print("An error occurred:", e)



# Create your views here.
def execute_code(request):
    message = 'Before POST request'

    if request.method == 'POST':
        message = 'After POST request'
        try:
            run_manim_command()
            print('function completed')
            
        except Exception as e:
            error = f"Error executing shell command: {e}"
            print(error)

        #after HTTP request
        context = { 
            'message':message,    
        }
        return render(request, 'run.html',context)  
         
    #before HTTP request
    context = {
        'message':message,
    }
    return render(request, 'run.html',context )
