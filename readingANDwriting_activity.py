import time
class Story:
    def __init__(self):
        self.stories = {
            "1": ("The Hare and the Tortoise", '''
One day, a hare was showing off how fast he could run. He laughed at the turtle for being so slow. After seeing the overconfidence, the turtle challenged him to a race. The hare laughed at the turtle's challenge and accepted.

As the race began, the hare ran extremely quickly and went far ahead of the turtle. He thought he had plenty of time to relax, so he lay down to sleep, thinking he would win easily.

However, the turtle kept walking slowly but steadily until he arrived at the finish line. When the hare woke up, he saw the turtle had already crossed the finish line. The turtle had won the race.
            '''),

            "2": ("The Elephant and the Ants", '''
There was once a proud elephant who enjoyed harassing smaller animals. He would go to the ant colony and shower them with water. The ants, being small, could only cry. The elephant laughed and threatened them.

The ants had enough and decided to teach the elephant a lesson.

They entered the elephant's trunk and started causing chaos. The elephant cried out in pain, realizing his mistake. He apologized to the ants and to all the animals he had bullied.
            '''),

            "3": ("The Talking Birds", '''
Once upon a time, there lived two talking birds with their parents. One day, when their parents were away, a villager caught them. One of the birds escaped and searched for its parents. Eventually, it found a hermitage where it was welcomed and fed, living happily there.

Meanwhile, the captured bird was discovered by an explorer. He spoke rudely to the bird, shocked to see a talking creature. The explorer later visited the hermitage and met the other bird, who spoke respectfully and welcomed him.
            '''),
        }

        self.questions = {
            "1": [
                {"question": "Who challenged the hare to a race?", "answer": "turtle"},
                {"question": "What did the hare do during the race?", "answer": "slept"},
                {"question": "Who won the race?", "answer": "turtle"}
            ],
            "2": [
                {"question": "What did the elephant do to the ants?", "answer": "harassed"},
                {"question": "How did the ants respond?", "answer": "taught him a lesson"},
                {"question": "What did the elephant do after realizing his mistake?", "answer": "apologized"}
            ],
            "3": [
                {"question": "What happened to one of the birds?", "answer": "caught by a villager"},
                {"question": "Where did the escaped bird go?", "answer": "hermitage"},
                {"question": "How did the explorer react to the talking bird?", "answer": "rudely"}
            ]
        }

    def write_to_file(self, content):
        with open('story.txt', 'a') as file:
            file.write(content)

    def display_menu(self):
        print('''
           1. The Hare and the Tortoise
           2. The Elephant and the Ants
           3. The Talking Birds
           4. Write your own story 
           5. Display all kids stories
           6. Exit 
        ''')

    def read_story(self, title, content):
        print(content)
        print("Press 'Enter' when you finish reading...")
        start_time = time.time()
        input()  
        
        end_time = time.time()
        time_taken = (end_time - start_time) / 60
        print(f"You took {time_taken:.2f} minutes to read '{title}'.")

    def ask_questions(self, story_number):
        start_time = time.time() 

        for q in self.questions[story_number]:
            user_answer = input(q["question"] + " ").strip().lower()
            if user_answer == q["answer"]:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {q['answer']}")

        end_time = time.time() 
        time_taken = (end_time - start_time) / 60  
        print(f"You took {time_taken:.2f} minutes to answer the questions.")

    def run(self):
        self.display_menu()
        choose = input("Choose number 1 - 6: ")

        while True:
            if choose in self.stories:
                title, story_content = self.stories[choose]
                self.read_story(title, story_content)
                self.ask_questions(choose)

            elif choose == '4':
                story_title = input("Write your story title then press enter: ")
                your_story = input("Write your story then press enter: ")
                self.write_to_file(f"{story_title} : \n{your_story} . \n ")
                print(f"\nYour story titled '{story_title}' \n{your_story}\n")  

            elif choose == '5':
                with open('story.txt','r') as file:
                    for s in file:
                        print(s.strip())

            elif choose == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select again.")

            self.display_menu()
            choose = input("Choose number 1 - 6: ")

story_app = Story()
story_app.run()
