import pyperclip

UNICODE = "\\u10$"
NSPACE = "\\uF801"

bar = [(0, 1)]
bar.extend([(2, 6) for _ in range(17)])
bar.append((7, 10))

fullbar = []

class BarCounter:
    count = 0
    length = 0

    def __init__(self, bar: list):
        self.bar = bar
        self.num = [x for _, x in bar]
        self.length = len(bar)

    def get(self):
        return NSPACE.join([UNICODE.replace("$", f"{i:02}") for i in self.num])

    def next(self):
        i = 0
        self.num[i] -= 1

        while i < self.length:
            if self.num[i] < self.bar[i][0]:
                # carry digit
                self.num[i] = self.bar[i][0]
                
                i += 1
                try:
                    self.num[i] -= 1
                except:
                    return True
            else:
                break
        return False
        


bc = BarCounter(bar)

L = []
for i in range(100):
    L.append(f'"rpg.new_ui.{i}": "{bc.get()}",')
    if bc.next():
        pyperclip.copy('\n'.join(L))
        exit(1)