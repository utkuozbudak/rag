def init_routes(app):
  @app.route('/')
  def index():
    return "index.html"