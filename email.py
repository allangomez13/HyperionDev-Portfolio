# Defines an email class
class Email:
  has_been_read = False

# Defines the constructor for the email class
  def __init__(self, email_address, subject_line, email_content):
    self.email_address = email_address
    self.subject_line = subject_line
    self.email_content = email_content

# A method that mark emails as read
  def mark_as_read(self):
    self.has_been_read = True

# An empty list that holds the emails
Inbox = []

# Defines a function that populates the inbox with emails
def populate_inbox():
  email1 = Email("johndoe@example.com", "Welcome to HyperionDev!", "Thank you for signing up for our course.")
  email2 = Email("janedoe@example.com", "Great work on the project!", "We were impressed with your submission.")
  email3 = Email("bob@example.com", "Reminder: Meeting at 2 PM", "Don't forget about the meeting this afternoon.")
  Inbox.extend([email1, email2, email3])

# Function that lists the emails in the inbox
def list_emails():
  for index, email in enumerate(Inbox):
    print(f"{index}. {email.subject_line}")

# Calls "populate_inbox" function to add emails to the inbox
populate_inbox()

# A loop that lets the user choose options
while True:
  print("\nPlease select an option:")
  print("1. List emails")
  print("2. Read email")
  print("3. Quit")

# Gets the users choice
  choice = input()

# If "List emails" is chosen it calls the "list_email" function
  if choice == "1":
   list_emails()
  
# If "Read email" is chosen it gets the index of the email and displays the details
  elif choice == "2":
    index = int(input("Enter the index of the email you want to read: "))
    email = Inbox[index]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    email.mark_as_read()  # Marks the email as read
  elif choice == "3":
    break
  else:
    print("Invalid choice. Please try again.")