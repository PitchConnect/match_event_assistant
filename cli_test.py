import cmd


class MatchEventAssistantCLI(cmd.Cmd):
    intro = "Welcome to the Match Event Assistant CLI. Type help or ? to list commands."
    prompt = "(match-event) "

    def do_simulate_event(self, arg):
        """Simulate a match event: simulate_event <event_description>"""
        if arg:
            print(f"Simulating event: {arg}")
            # Here, core logic or mock logic would be called
            print(f'System response: [Mocked response for "{arg}"]')
        else:
            print("Please provide an event description.")

    def do_exit(self, arg):
        """Exit the CLI."""
        print("Exiting Match Event Assistant CLI.")
        return True

    def do_EOF(self, arg):
        """Exit on Ctrl-D."""
        print("Exiting Match Event Assistant CLI.")
        return True


if __name__ == "__main__":
    MatchEventAssistantCLI().cmdloop()
