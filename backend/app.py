#----------------------------------------------------------------#
# Imports
#----------------------------------------------------------------#
import sys
from flask import (Flask, jsonify, request, abort)
from flask_cors import CORS

from model import setup_db, Articles, db

#----------------------------------------------------------------#
# Create app configure
#----------------------------------------------------------------#

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    CORS(app, resources={r"/*": {"origins": "*"}})

#----------------------------------------------------------------#
# API
#----------------------------------------------------------------#

    # The Get route handler

    @app.route('/articles', methods=['GET'])
    def get_articles():
        error = False
        try:
            articles = Articles.query.all()
            formatted_article = [article.format() for article in articles]
            totale_articles = len(articles)
        except:
            error = True
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(404)
        else:
            return jsonify({
                "Success": True,
                "Status": 200,
                "Articles": formatted_article,
                "Totale Articles": totale_articles
            })

    # Get one article handler
    @app.route('/article/<int:article_id>', methods=['GET'])
    def get_one_article(article_id):
        article = Articles.query.get(article_id)
        if article is None:
            abort(404)
        else:
            return jsonify({
                "Success": True,
                "Status": 200,
                "Article": article.format()
            })

    # The Post route handler
    @app.route('/new', methods=['POST'])
    def add_new_article():
        error = False
        try:
            add_article = request.get_json()
            Articles(
                title=add_article['title'],
                art_body=add_article['body']
            ).insert()
        except:
            error = True
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(500)
        else:
            return jsonify({
                'Success': True,
                "Status": 200,
                "Message": 'Article added'
            })

    # The Put route handler
    @app.route('/update/<int:article_id>', methods=['PUT'])
    def update_article(article_id):
        error = False
        try:
            up_article = Articles.query.filter_by(id=article_id).first()
            req = request.get_json()
            title = up_article.title = req['title']
            art_body = up_article.art_body = req['body']
            
            Articles(
                title=title,
                art_body=art_body
            ).update()
        except:
            error = True
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(422)
        else:
            return jsonify({
                "Success": True,
                "Status": 200,
                "Message": "Article Update"
            })

    # The Delete route handler
    @app.route('/delete/<int:article_id>', methods=['DELETE'])
    def delete_article(article_id):
        error = False
        try:
            del_article = Articles.query.filter_by(id=article_id).first()
            del_article.delete()
        except:
            error = True
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()
        if error:
            abort(404)
        else:
            return jsonify({
                "Success": True,
                "Status": 200,
                "Message": "Article Deleted"
            })

    return app