from news import create_app, db

news_app = create_app()

if __name__ == '__main__':
    with news_app.app_context():
        db.create_all()

    news_app.run(debug=True)