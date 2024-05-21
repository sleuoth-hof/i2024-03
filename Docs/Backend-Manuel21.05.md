Link: https://docs.google.com/document/d/1DX7cFbrRc2wL0-W6Nk_aiMcFalggzMk_nkQrVUwQrYA/edit?usp=sharing
Project Structure
The project follows a Django-standard structure with a main project folder and an app named tradingbot. The app contains folders for models, controllers, and views.
Models
The models define the structure of the database tables. The main model is News, which stores financial news.
Controllers
The controllers contain the business logic of the application. The fetchNews controller retrieves financial news and stores it in the database. The evaluateNews controller evaluates the news and saves the results. The strategy controller executes a trading strategy based on the evaluated news.
Views
The views handle HTTP requests. The FetchNewsAPIView retrieves news and saves it. The EvaluateNewsAPIView evaluates news and returns the results. The TradingStrategyAPIView executes a trading strategy and returns the actions.
URLs
The URLs route requests to views. The app-specific URLs are defined in tradingbot/urls.py and include routes for fetching news, evaluating news, and executing the trading strategy.
Project Start
To start the project:
Ensure Python and Django are installed.
Navigate to the project folder.
Run python manage.py makemigrations and python manage.py migrate.
Start the development server with python manage.py runserver.
