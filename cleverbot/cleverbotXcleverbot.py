import cleverbot

cb1 = cleverbot.Cleverbot()
cb2 = cleverbot.Cleverbot()

text = cb1.ask("Hi")
print("Hello")
while True:
    text = cb2.ask(text)
    print("Cleverbot 2: " + text)
    text = cb1.ask(text)
    print("Cleverbot 1: " + text)
