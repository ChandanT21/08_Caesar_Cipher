import display
import cipher

if __name__ == '__main__':
    print(display.logo)
    active = True
    choices = ['yes', 'no']
    while active:
        cipher.launch()
        rerun = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
        while rerun not in choices:
            rerun = input("Incorrect option stated. Please type 'yes' to go again or 'no' to quit. ")
        if rerun == 'no':
            active = False
        else:
            active = True
