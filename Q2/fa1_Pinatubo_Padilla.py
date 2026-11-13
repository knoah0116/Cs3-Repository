class Publication:
    title:str
    author:str


    def __init__(self,title,author):
        self.title=title
        self.author=author
    def set_title(title):
        title=self.title
    def get_title(self):
        return self.title
    def get_author():
        return self.author
    def display_info(self):
        return print(f"Title: {self.title}\nAuthor: {self.author}")


class Book(Publication):
    number_of_pages=0
    def __init__(self,title,author,number_pages):
        self.title=title
        self.author=author
        self.number_pages=number_pages
    def get_number_of_pages(self):
        return self.number_pages
    def set_number_of_pages(self,number_pages):
        if number_pages < 0:
            self.number_pages=self.number_pages
            print("The number of pages must be positive.")
        
            
class Magazine(Publication):
    issue_number=0
    def __init__(self,title,author,issue_number):
        self.title=title
        self.author=author
        self.issue_number=issue_number
    def get_issue_number(self):
        return self.issue_number
    def set_issue_number(self,issue_number):
        if issue_number < 0:
            self.issue_number=self.issue_number
            print("The issue number must be positive.")

pub1=Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1=Book(f"The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(f"Number of Pages: {book1.get_number_of_pages()}")

print("\nMagazine Information:")
mag1.display_info()
print(f"Issue Number: {mag1.get_issue_number()}")

