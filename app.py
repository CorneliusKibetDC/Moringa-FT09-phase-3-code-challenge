
# # from database.setup import create_tables
# # from database.connection import get_db_connection
# # from models.article import Article
# # from models.author import Author
# # from models.magazine import Magazine

# # def main():
# #     create_tables()

# #     # Collect user input
# #     author_name = input("Enter author's name: ")
# #     magazine_name = input("Enter magazine name: ")
# #     magazine_category = input("Enter magazine category: ")
# #     article_title = input("Enter article title: ")
# #     article_content = input("Enter article content: ")  # Added input for content

# #     # Create models
# #     author = Author(name=author_name)
# #     magazine = Magazine(name=magazine_name, category=magazine_category)
# #     article = Article(author=author, magazine=magazine, title=article_title, content=article_content)  # Pass content

# #     print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}, Content: {article.content}")

# # if __name__ == "__main__":
# #     main()



# import os
# from database.setup import create_tables
# from models.article import Article
# from models.author import Author
# from models.magazine import Magazine

# def main():
#     create_tables()

#     # Read values from environment variables
#     author_name = os.environ.get("AUTHOR_NAME", "Default Author")
#     magazine_name = os.environ.get("MAGAZINE_NAME", "Default Magazine")
#     magazine_category = os.environ.get("MAGAZINE_CATEGORY", "General")
#     article_title = os.environ.get("ARTICLE_TITLE", "Default Article Title")
#     article_content = os.environ.get("ARTICLE_CONTENT", "Default article content.")

#     # Create models
#     author = Author(name=author_name)
#     magazine = Magazine(name=magazine_name, category=magazine_category)
#     article = Article(author=author, magazine=magazine, title=article_title, content=article_content)

#     print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}")

# if __name__ == "__main__":
#     main()




import http.server
import socketserver
from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database
    create_tables()

    # Use default data instead of user input (since Render has no stdin)
    author_name = "Default Author"
    magazine_name = "Default Magazine"
    magazine_category = "General"
    article_title = "Default Article Title"
    article_content = "Default Content"

    # Create models
    author = Author(name=author_name)
    magazine = Magazine(name=magazine_name, category=magazine_category)
    article = Article(author=author, magazine=magazine, title=article_title, content=article_content)

    print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}")

if __name__ == "__main__":
    main()

    # Start a minimal HTTP server to keep Render alive
    PORT = 8080  # Default port for Render
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
