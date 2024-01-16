import sys, argparse, time

class TerminalApp:
    INPUT_MARKER = '> '

    def __init__(self, time_allowed_seconds):
        self.modes = []
        self.time_allowed_seconds = time_allowed_seconds

    def start(self):
        print('Welcome to Mental Math Trainer!\n')
        print('Select a mode from the following list')

        for i, mode in enumerate(self.modes):
            print(f'{i + 1}. {mode.getName()}')
        print('\n')

        mode = int(input(self.INPUT_MARKER))

        if (mode < 1 or mode > len(self.modes)):
            print('ERROR: incorrect mode index', file=sys.stderr)
            sys.exit(1)

        self.run(mode - 1)

    def run(self, mode_index):
        mode = self.modes[mode_index]
        score = 0

        start_time = time.time()

        while True:
            question, answer = mode.generateQuestion()
            print(f'{question}')
            user_answer = input(self.INPUT_MARKER)

            if (user_answer == answer):
                print('Correct!\n')
                score += 1
            else:
                print('Incorrect.\n')

            end_time = time.time()
            elapsed = end_time - start_time
            if (elapsed > self.time_allowed_seconds):
                break

        print('Finished!')
        print(f'Your score is: {score}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='mental-math-trainer',
        description='Helps improve mental math, particularly through learning tricks',
        epilog='© 2023 Mohammad M. Rakib. All rights reserved.'\
    )
    parser.add_argument('--no-gui', action='store_true')
    args = parser.parse_args()
    
    if (args.no_gui == True):
        app = TerminalApp(60)
        app.start()
    else:
        print('ERROR: GUI not implemented', file=sys.stderr)
        sys.exit(1)
