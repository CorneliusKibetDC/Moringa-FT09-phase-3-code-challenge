
from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")  # Added input for content

    # Create models
    author = Author(name=author_name)
    magazine = Magazine(name=magazine_name, category=magazine_category)
    article = Article(author=author, magazine=magazine, title=article_title, content=article_content)  # Pass content

    print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}, Content: {article.content}")

if __name__ == "__main__":
    main()
