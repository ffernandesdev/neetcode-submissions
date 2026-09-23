class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_page_index = 0
        

    def visit(self, url: str) -> None:
        self.curr_page_index += 1
        self.history = self.history[:self.curr_page_index]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr_page_index = max(0, self.curr_page_index - steps)
        return self.history[self.curr_page_index]
        

    def forward(self, steps: int) -> str:
        self.curr_page_index = min(len(self.history) - 1, self.curr_page_index + steps)
        return self.history[self.curr_page_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)