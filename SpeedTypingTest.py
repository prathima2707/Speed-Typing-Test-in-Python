from tkinter import *
import ctypes
import random
import tkinter

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup
storage = Tk()
storage.title('CopyAssignment - Typing Speed Test')

storage.geometry('1400x700')

storage.option_add("*Label.Font", "consolas 30")
storage.option_add("*Button.Font", "consolas 30")


def handlingLabels():
    # Text List
    random_selection = [
        "If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways."
        "For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool."
        "For those writers who have writers' block, this can be an excellent way to take a step to crumbling those walls. By taking the writer away from the subject matter that is causing the block, a random sentence may allow them to see the project they're working on in a different light and perspective. Sometimes all it takes is to get that first sentence down to help break the block."
        "Random sentences can also spur creativity in other types of projects being done. If you are trying to come up with a new concept, a new idea or a new product, a random sentence may help you find unique qualities you may not have considered. Trying to incorporate the sentence into your project can help you look at it in different and unexpected ways than you would normally on your own."
        "These are just a few ways that one might use the random sentence generator for their benefit. If you're not sure if it will help in the way you want, the best course of action is to try it and see. Have several random sentences generated and you'll soon be able to see if they can help with your project. Our goal is to make this tool as useful as possible. For anyone who uses this tool and comes up with a way we can improve it, we'd love to know your thoughts. Please contact us so we can consider adding your ideas to make the random sentence generator the best it can be."
    ]

    # Chosing one of the texts randomly with the choice function
    text = random.choice(random_selection).lower()

    splitPoint = 0

    global nameLabelLeft
    nameLabelLeft = Label(storage, text=text[0:splitPoint], fg='green')
    nameLabelLeft.place(relx=0.5, rely=0.5, anchor=E)

    global nameLabelRight
    nameLabelRight = Label(storage, text=text[splitPoint:])
    nameLabelRight.place(relx=0.5, rely=0.5, anchor=W)

    global currentAlphabetLabel
    currentAlphabetLabel = Label(storage, text=text[splitPoint], fg='grey')
    currentAlphabetLabel.place(relx=0.5, rely=0.6, anchor=N)

    global secondsLeft
    headingLabel = Label(storage, text=f'CopyAssignment - Typing Speed Test', fg='blue')
    headingLabel.place(relx=0.5, rely=0.2, anchor=S)
    secondsLeft = Label(storage, text=f'0 Seconds', fg='red')
    secondsLeft.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    storage.bind('<Key>', handlekeyPress)

    global secondsPassed
    secondsPassed = 0

    storage.after(60000, stopGame)
    storage.after(1000, timeAddition)


def stopGame():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(nameLabelLeft.cget('text').split(' '))

    secondsLeft.destroy()
    currentAlphabetLabel.destroy()
    nameLabelRight.destroy()
    nameLabelLeft.destroy()

    global labelOfResult
    labelOfResult = Label(storage, text=f'Words per Minute (WPM): {amountWords}', fg='black')
    labelOfResult.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restartGame the game
    global showcaseResults
    showcaseResults = Button(storage, text=f'Retry', command=restartGame)
    showcaseResults.place(relx=0.5, rely=0.6, anchor=CENTER)


def restartGame():
    # Destry result widgets
    labelOfResult.destroy()
    showcaseResults.destroy()
    handlingLabels()


def timeAddition():
    global secondsPassed
    secondsPassed += 1
    secondsLeft.configure(text=f'{secondsPassed} Seconds')
    if writeAble:
        storage.after(1000, timeAddition)


def handlekeyPress(event=None):
    try:
        if event.char.lower() == nameLabelRight.cget('text')[0].lower():
            nameLabelRight.configure(text=nameLabelRight.cget('text')[1:])
            nameLabelLeft.configure(text=nameLabelLeft.cget('text') + event.char.lower())
            currentAlphabetLabel.configure(text=nameLabelRight.cget('text')[0])
    except tkinter.TclError:
        pass


handlingLabels()

storage.mainloop()
