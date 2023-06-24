from app import app
from app.views import user_bp

# Registering the user blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)