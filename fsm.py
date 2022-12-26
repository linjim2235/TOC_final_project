from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

machine = TocMachine(
    states=["user", "introduction", "location", "else"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "introduction",
            "conditions": "is_going_to_introduction",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "location",
            "conditions": "is_going_to_location",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "else",
            "conditions": "is_going_to_else",
        },
        {"trigger": "go_back", "source": ["introduction", "location", "else"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
machine.get_graph().draw("fsm.png", prog="dot", format="png")