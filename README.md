# Code Melli Generator
code melli generator is a python class for generating iranian national code by area code

# Instalation
to install the app you should just download the project directly or you can clone it
### clone
````shell
git clone https://github.com/naderidev/codemelligenerator
````

# Usage
````python
from classes.CodeMelliGenerator import CodeMelliGenerator

# replace 011 with your area code
cmg = CodeMelliGenerator(area_code='011', print_status_live=True)

# generate and prints the status
cmg.generate()

# prints generated codes array
print(cmg.get_codes())

# prints all checked modes
print(cmg.all_modes)

# prints all valid modes (which modes that is a valid national code)
print(cmg.valid_modes)
````

> ATTENTION: activing "print_status_live" will increase the execution time

### Use with CMD
also there is a file to use in cmd with out writing any codes.

in the first step run the following command in the command line:
````shell
py cmg.py -h
````
then you will see the full usage:
```shell
usage: cmg.py [-h] -a AREACODE -s SAVE [-psl]

options:
  -h, --help            show this help message and exit

required arguments:
  -a AREACODE, --areacode AREACODE
                        area code [numerical]
  -s SAVE, --save SAVE  file path for save codes

not required arguments:
  -psl, --print_status_live
                        print status in live | ATTENTION: printing status in live will decrease speed
```
### Example 
for the example if you want to generate all national codes for 011(south tehran), you should do some thing like this:
```shell
py cmg.py -a=011 -s=tehran-south.txt -psl
# adding -psl will increase the execution time but it's hot :)
```
after the code executed, you will see a txt file named "tehran-south.txt" in the directory
