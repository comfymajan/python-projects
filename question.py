class question:
    def __init__(self,prompt,options,answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer
    def show_question(self):
        print(self.prompt)
        for option in self.options:
            print(option)