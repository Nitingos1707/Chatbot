import time
from tkinter import *
from fuzzywuzzy import fuzz
import random

responses = {
    'hi': 'hello',
    'hello': 'hi',
    'how are you?': "I'm a bot, so I don't have feelings, but I'm here and ready to assist you!",
    "i'm fine too": 'Nice to hear that!',
    'what is your name?': "I'm Dytto, your friendly chatbot!",
    'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
    'tell me a fact': 'Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!',
    'how can I be happy?': 'Finding happiness is a personal journey. Engage in activities you love, connect with others, and take care of yourself.',
    'who created you?': 'I was created by a developer using Python and the magic of code!',
    'what is the meaning of life?': "The meaning of life is a profound question. It's up to each individual to find their own purpose and fulfillment.",
    'why do we dream?': 'Dreams are a fascinating aspect of the human mind. They may reflect our thoughts, experiences, and emotions.',
    'where do you live?': "I exist in the digital realm, always ready to chat with you!",
    'i feel alone': "I'm here for you. It's okay to feel this way. Reach out to someone you trust or consider talking to a professional.",
    "i can't sleep at night": "Difficulty sleeping can be challenging. Try creating a bedtime routine, avoid screens before bed, and consider relaxation techniques like deep breathing.",
    'i am facing a breakup': "I'm sorry to hear that you're going through a breakup. It's okay to feel a range of emotions. Take time for self-care, talk to friends or a professional, and remember that healing takes time.",
}

sad_responses = [
    "I'm sorry to hear that you're feeling sad. It's okay to express your emotions.",
    "Feeling lonely is tough, but remember that you're not alone. Reach out to friends or family for support.",
    "I'm here for you. If you want to talk about what's on your mind, I'm all ears.",
    "It's okay to have days when you feel down. Take it one step at a time.",
    "Remember that your feelings are valid. If you need someone to talk to, I'm here.",
]

motivational_low_responses = [
    "Dytto: It's normal to feel low at times, but remember that you have the strength to overcome challenges.",
    "Dytto: Tough times don't last, but tough people do. You've got this!",
    "Dytto: You're capable of more than you know. Take small steps and celebrate your progress.",
    "Dytto: When you feel low, focus on the things that bring you joy. It's okay to prioritize your well-being.",
    "Dytto: Remember that setbacks are a part of life. Use them as opportunities for growth and learning.",
]

greetings = ['hi', 'hello', 'hey', 'what\'s up', 'namaste']
general_responses = ["I'm here to chat with you! Feel free to ask me anything.", "Let's have a conversation! Ask me a question.", "Hello! How can I assist you today?"]

jokes = [
    'Why don’t scientists trust atoms? Because they make up everything!',
    'Parallel lines have so much in common. It’s a shame they’ll never meet.',
    'Why did the scarecrow win an award? Because he was outstanding in his field!',
    'I only know 25 letters of the alphabet. I don’t know y.',
    'What do you get when you cross a snowman and a vampire? Frostbite!',
    'Why don\'t skeletons fight each other? They don\'t have the guts.',
    'What did one ocean say to the other ocean? Nothing, they just waved.',
]

facts = [
    'Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!',
    'Bananas are berries, but strawberries aren’t.',
    'The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.',
    'Cows have best friends and can become stressed when they are separated.',
    'Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.',
    'The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.',
    'The longest hiccuping spree lasted 68 years!',
]

class DyttoBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dytto: Your Friendly Chatbot")

        # Set the background color to a friendly light blue
        self.text = Text(master, bg='#ADD8E6', fg='black', wrap=WORD, font=('Helvetica', 12))
        self.text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.text.insert(END, random.choice(general_responses) + "\n")

        self.entry = Entry(master, width=50, font=('Helvetica', 12))
        self.send_button = Button(master, text='Send', bg='deeppink', fg='white', width=20, command=self.send)
        self.entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

    def send_message(self, message):
        self.text.insert(END, "\n" + message)

    def fuzzy_match(self, input_text, response):
        return fuzz.ratio(input_text.lower(), response.lower()) >= 80

    def detect_greeting(self, user_input):
        for greeting in greetings:
            if self.fuzzy_match(user_input, greeting):
                return True
        return False

    def detect_keywords(self, user_input):
        keywords = []
        for key in responses:
            if self.fuzzy_match(user_input, key) or key in user_input.lower():
                keywords.append(key)
        return keywords

    def detect_keywords_in_response(self, response):
        keywords = []
        for key in responses:
            if key in response.lower():
                keywords.append(key)
        return keywords

    def generate_response(self, user_input):
        user_input_lower = user_input.lower()

        if self.detect_greeting(user_input_lower):
            return "Dytto: " + random.choice(greetings).capitalize() + "! How can I assist you today?"

        detected_keywords = self.detect_keywords(user_input)

        for key in detected_keywords:
            if key in responses:
                return "Dytto: " + responses[key]

        for key in detected_keywords:
            if key == 'tell me a joke':
                return "Dytto: " + random.choice(jokes)

        for key in detected_keywords:
            if key == 'tell me a fact':
                return "Dytto: " + random.choice(facts)

        for key in detected_keywords:
            if key == 'tell me something motivational':
                return "Dytto: " + random.choice(motivational_low_responses)

        for key in detected_keywords:
            if key in ['help', 'consult']:
                return "Dytto: It's important to prioritize your mental health. Consider speaking to a mental health professional for personalized support."

        for keyword in ['lonely', 'sad', 'feeling low']:
            if keyword in user_input_lower:
                return "Dytto: " + random.choice(sad_responses)

        for key in detected_keywords:
            if key in ['low', 'stress', 'feeling low']:
                return "Dytto: " + random.choice(motivational_low_responses)

        for key in detected_keywords:
            if key == 'need help':
                return "Dytto: I'm here to help! What can I assist you with?"

        for key in detected_keywords:
            if key == 'i am facing a breakup':
                return "Dytto: I'm sorry to hear that you're going through a breakup. It's okay to feel a range of emotions. Take time for self-care, talk to friends or a professional, and remember that healing takes time."

        response = "Dytto: Sorry, I didn't understand that. Ask me anything, and I'll do my best to help!"
        response_keywords = self.detect_keywords_in_response(response)

        for key in response_keywords:
            if key in ['lonely', 'sad']:
                return "Dytto: " + random.choice(sad_responses)

            if key in ['low', 'stress', 'feeling low','stressed']:
                return "Dytto: " + random.choice(motivational_low_responses)

            if key == 'need help':
                return "Dytto: I'm here to help! What can I assist you with?"

        return response

    def send(self):
        user_input = self.entry.get()
        self.send_message("You: " + user_input)

        if user_input.lower() == 'exit':
            self.send_message("Dytto: Goodbye! Have a great day!")
            self.master.destroy()
            return

        bot_response = self.generate_response(user_input)
        self.send_message(bot_response)
        self.entry.delete(0, END)

def main():
    root = Tk()
    bot_gui = DyttoBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()