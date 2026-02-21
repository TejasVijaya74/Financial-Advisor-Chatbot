class MemoryService:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})

    def add_bot_message(self, message):
        self.history.append({"role": "assistant", "content": message})

    def get_context(self):
        return "\n".join(
            f"{msg['role']}: {msg['content']}"
            for msg in self.history
        )