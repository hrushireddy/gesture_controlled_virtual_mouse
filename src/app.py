import eel
import os
from queue import Queue

class ChatBot:

    started = False
    userinputQueue = Queue()

    @staticmethod
    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    @staticmethod
    def popUserInput():
        return ChatBot.userinputQueue.get()

    @staticmethod
    def close_callback(route, websockets):
        if not websockets:  # Close only if no active connections
            print('Closing ChatBot...')
            ChatBot.started = False  # Ensure graceful shutdown

    @eel.expose
    def getUserInput(msg):
        ChatBot.userinputQueue.put(msg)
        print(f"User Input: {msg}")

    @staticmethod
    def close():
        ChatBot.started = False

    @staticmethod
    def addUserMsg(msg):
        print(f"User Message: {msg}")
        eel.addUserMsg(msg)

    @staticmethod
    def addAppMsg(msg):
        print(f"App Response: {msg}")
        eel.addAppMsg(msg)

    @staticmethod
    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])

        try:
            eel.start(
                'index.html', mode='chrome',
                host='localhost', port=27005, block=False,
                size=(350, 480), position=(10, 100),
                disable_cache=True, close_callback=ChatBot.close_callback
            )
            ChatBot.started = True

            while ChatBot.started:
                print("Chatbot is running...")
                try:
                    eel.sleep(10.0)  # Non-blocking UI update
                except Exception as e:
                    print(f"Error in Eel loop: {e}")
                    break  # Exit loop safely

        except Exception as e:
            print(f"Error starting Eel: {e}")
