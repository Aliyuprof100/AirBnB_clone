<<<<<<< HEAD
import cmd
=======
#/usr/bin/python3
import cmd 

class command(cmd.Cmd):
    """This is a simple command line interpreter"""

    def do_save(self, line):
        print("Please save this file succusssfully")

if __name__ == '__Main__':
    command.cmdloop()
>>>>>>> 42646d21f6e499439a553ed368f69c0118f99c25
