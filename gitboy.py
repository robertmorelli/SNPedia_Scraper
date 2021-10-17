commands = '''
echo "a"
echo "b"
echo "c"
echo "d"
'''

process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = process.communicate(commands)
print(out)