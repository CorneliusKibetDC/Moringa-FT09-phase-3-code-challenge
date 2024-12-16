



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
