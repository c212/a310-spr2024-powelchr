from termcolor import colored

print(colored('Hello, World!', 'green'))
print(colored('Warning: ', 'yellow'), colored('System overload!', 'red', attrs=['blink']))
print(colored('Success', 'green', attrs=['bold']))
