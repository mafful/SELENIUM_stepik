import subprocess

# Run pip freeze and capture the output
output = subprocess.check_output(['pip', 'freeze'])

# Add the PyPI index URL as the first line
requirements_txt = '-i https://pypi.org/simple\n\n' + output.decode('utf-8')

# Write the updated content back to requirements.txt
with open('requirements.txt', 'w') as file:
    file.write(requirements_txt)