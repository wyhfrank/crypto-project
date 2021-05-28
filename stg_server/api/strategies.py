from flask import jsonify, request, g, url_for, current_app
# from .. import db
# from ..models import Post, Permission, Comment
from . import api
from .decorators import permission_required
from invest_adviser import get_invest_advice


@api.route('/strategy/execute/', methods=['POST'])
def execute_strategy():
    # comment = Comment.query.get_or_404(id)
    print(request.json)
    # request["jpy"]
    strategy_id = request.json["strategy_id"]
    jpy = request.json["jpy"]
    crypto_name = request.json["crypto_name"]
    crypto_amount = request.json["crypto_amount"]

    if strategy_id < 0:
        current_app.logger.info("Executing the default strategy...")

    result = get_invest_advice(strategy_id)
    return jsonify(result)


# @api.route('/comments/')
# def get_comments():
#     page = request.args.get('page', 1, type=int)
#     pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
#         page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
#         error_out=False)
#     comments = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('api.get_comments', page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('api.get_comments', page=page+1)
#     return jsonify({
#         'comments': [comment.to_json() for comment in comments],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })


# @api.route('/comments/<int:id>')
# def get_comment(id):
#     comment = Comment.query.get_or_404(id)
#     return jsonify(comment.to_json())
#
#
# @api.route('/posts/<int:id>/comments/')
# def get_post_comments(id):
#     post = Post.query.get_or_404(id)
#     page = request.args.get('page', 1, type=int)
#     pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
#         page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
#         error_out=False)
#     comments = pagination.items
#     prev = None
#     if pagination.has_prev:
#         prev = url_for('api.get_post_comments', id=id, page=page-1)
#     next = None
#     if pagination.has_next:
#         next = url_for('api.get_post_comments', id=id, page=page+1)
#     return jsonify({
#         'comments': [comment.to_json() for comment in comments],
#         'prev': prev,
#         'next': next,
#         'count': pagination.total
#     })
#
#
# @api.route('/posts/<int:id>/comments/', methods=['POST'])
# @permission_required(Permission.COMMENT)
# def new_post_comment(id):
#     post = Post.query.get_or_404(id)
#     comment = Comment.from_json(request.json)
#     comment.author = g.current_user
#     comment.post = post
#     db.session.add(comment)
#     db.session.commit()
#     return jsonify(comment.to_json()), 201, \
#         {'Location': url_for('api.get_comment', id=comment.id)}
