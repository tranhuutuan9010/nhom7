# from flask import Flask, render_template, abort
# import mysql.connector

# app = Flask(__name__)

# # Cấu hình kết nối cơ sở dữ liệu
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '12345',
#     'database': 'learning'
# }

# # Route trang chính
# @app.route('/')
# def index():
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách các chủ đề bao gồm đường dẫn ảnh
#         cursor.execute("SELECT id, name, image_path FROM categories")
#         categories = cursor.fetchall()

#     finally:
#         cursor.close()
#         conn.close()

#     # Render template index.html và truyền danh sách chủ đề
#     return render_template('index.html', categories=categories)

# # Route hiển thị các chủ đề học
# @app.route('/learn')
# def learn():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách chủ đề bao gồm đường dẫn ảnh
#         cursor.execute("SELECT id, name, image_path FROM categories")
#         categories = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template learn.html với danh sách chủ đề
#     return render_template('learn.html', categories=categories)

# # Route hiển thị từ vựng theo chủ đề
# @app.route('/learn/<int:category_id>')
# def learn_category(category_id):
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Truy vấn tên chủ đề
#         cursor.execute("SELECT name FROM categories WHERE id = %s", (category_id,))
#         category = cursor.fetchone()
        
#         if not category:
#             abort(404, description="Chủ đề không tồn tại")

#         # Truy vấn danh sách từ vựng trong chủ đề
#         cursor.execute("SELECT word FROM words WHERE category_id = %s", (category_id,))
#         words = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template categories.html với danh sách từ vựng
#     return render_template('categories.html', category_name=category['name'], words=words)

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, abort
# import mysql.connector

# app = Flask(__name__)

# # Cấu hình kết nối cơ sở dữ liệu
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '12345',
#     'database': 'learning'
# }

# # Route trang chính
# @app.route('/')
# def index():
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách các chủ đề
#         cursor.execute("SELECT id, name FROM categories")
#         categories = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template index.html và truyền danh sách chủ đề
#     return render_template('index.html', categories=categories)

# # Route hiển thị từ vựng theo chủ đề
# @app.route('/learn')
# def learn():
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Truy vấn tên chủ đề
#         cursor.execute("SELECT name FROM categories WHERE id = %s", (category_id,))
#         category = cursor.fetchone()
        
#         if not category:
#             abort(404, description="Chủ đề không tồn tại")

#         # Truy vấn danh sách từ vựng trong chủ đề
#         cursor.execute("SELECT word, image FROM words WHERE category_id = %s", (category_id,))
#         words = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template categories.html với danh sách từ vựng
#     return render_template('categories.html', category_name=category['name'], words=words)

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, abort
# import mysql.connector

# app = Flask(__name__)

# # Cấu hình kết nối cơ sở dữ liệu
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '12345',
#     'database': 'learning'
# }

# # Route trang chính - hiển thị danh sách chủ đề
# @app.route('/')
# def index():
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách các chủ đề, bao gồm đường dẫn ảnh
#         cursor.execute("SELECT id, name, image_path FROM categories")
#         categories = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template index.html và truyền danh sách chủ đề
#     return render_template('index.html', categories=categories)

# # Route hiển thị từ vựng theo chủ đề
# @app.route('/learn/<int:category_id>')
# def learn_category(category_id):
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Truy vấn tên chủ đề
#         cursor.execute("SELECT name FROM categories WHERE id = %s", (category_id,))
#         category = cursor.fetchone()
        
#         if not category:
#             abort(404, description="Chủ đề không tồn tại")

#         # Truy vấn danh sách từ vựng trong chủ đề (bao gồm cả ảnh)
#         cursor.execute("SELECT word, image FROM words WHERE category_id = %s", (category_id,))
#         words = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template categories.html với danh sách từ vựng
#     return render_template('categories.html', category_name=category['name'], words=words)

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, jsonify, render_template, abort
# import mysql.connector

# app = Flask(__name__)

# # Cấu hình kết nối cơ sở dữ liệu
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': '12345',
#     'database': 'learning'
# }

# # Route trang chính
# @app.route('/')
# def index():
#     try:
#         # Kết nối tới cơ sở dữ liệu
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách các chủ đề bao gồm đường dẫn ảnh
#         cursor.execute("SELECT id, name, image_path FROM categories")
#         categories = cursor.fetchall()

#     finally:
#         cursor.close()
#         conn.close()

#     # Render template index.html và truyền danh sách chủ đề
#     return render_template('index.html', categories=categories)

# # Route hiển thị các chủ đề học
# @app.route('/learn')
# def learn():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Lấy danh sách chủ đề bao gồm đường dẫn ảnh
#         cursor.execute("SELECT id, name, image_path FROM categories")
#         categories = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template learn.html với danh sách chủ đề
#     return render_template('learn.html', categories=categories)

# # Route hiển thị từ vựng theo chủ đề
# @app.route('/learn/<int:category_id>')
# def learn_category(category_id):
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Truy vấn tên chủ đề
#         cursor.execute("SELECT name FROM categories WHERE id = %s", (category_id,))
#         category = cursor.fetchone()
        
#         if not category:
#             abort(404, description="Chủ đề không tồn tại")

#         # Truy vấn danh sách từ vựng trong chủ đề
#         # cursor.execute("SELECT word FROM words WHERE category_id = %s", (category_id,))
#         cursor.execute("SELECT word, image FROM words WHERE category_id = %s", (category_id,))
#         words = cursor.fetchall()
#     finally:
#         cursor.close()
#         conn.close()

#     # Render template categories.html với danh sách từ vựng
#     return render_template('categories.html', category_name=category['name'], words=words)
# # Route cho chức năng Text to Speech
# @app.route('/text-to-speech')
# def text_to_speech():
#     # Render template text-to-speech.html
#     return render_template('text-to-speech.html')
# # Route cho bài tập dịch nghĩa
# @app.route('/exercise')
# def exercise():
#     return render_template('exercise.html')

# # Route trả về từ vựng dưới dạng JSON
# @app.route('/get-words')
# def get_words():
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor(dictionary=True)

#         # Truy vấn danh sách từ vựng và nghĩa
#         cursor.execute("SELECT word, meaning FROM words")
#         words = cursor.fetchall()

#     finally:
#         cursor.close()
#         conn.close()
        
#     return jsonify(words)  # Trả về dữ liệu dưới dạng JSON

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash, abort
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Cấu hình kết nối cơ sở dữ liệu
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'learning'
}

# Hàm kết nối CSDL
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Route trang chính - hiển thị danh sách chủ đề
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, image_path FROM categories")
        categories = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return render_template('index.html', categories=categories)

# Route đăng ký (Register)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                           (username, password, email))
            conn.commit()
            flash("Đăng ký thành công!", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Lỗi: {str(e)}", "danger")
        finally:
            cursor.close()
            conn.close()

    return render_template('register.html')

# Route đăng nhập (Login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                flash("Đăng nhập thành công!", "success")
                return redirect(url_for('index'))
            else:
                flash("Sai tên đăng nhập hoặc mật khẩu.", "danger")
        except Exception as e:
            flash(f"Lỗi: {str(e)}", "danger")
        finally:
            cursor.close()
            conn.close()

    return render_template('login.html')

# Route hiển thị các chủ đề học
@app.route('/learn')
def learn():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Lấy danh sách chủ đề bao gồm đường dẫn ảnh
        cursor.execute("SELECT id, name, image_path FROM categories")
        categories = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

    # Render template learn.html với danh sách chủ đề
    return render_template('learn.html', categories=categories)

# Route hiển thị từ vựng theo chủ đề
@app.route('/learn/<int:category_id>')
def learn_category(category_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Truy vấn tên chủ đề
        cursor.execute("SELECT name FROM categories WHERE id = %s", (category_id,))
        category = cursor.fetchone()

        if not category:
            abort(404, description="Chủ đề không tồn tại")

        # Truy vấn danh sách từ vựng
        cursor.execute("SELECT word, image FROM words WHERE category_id = %s", (category_id,))
        words = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

    return render_template('categories.html', category_name=category['name'], words=words)

# Route trả về từ vựng dưới dạng JSON
@app.route('/get-words')
def get_words():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT word, meaning FROM words")
        words = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return jsonify(words)

# Route chức năng Text to Speech
@app.route('/text-to-speech')
def text_to_speech():
    return render_template('text-to-speech.html')

# Route chức năng Bài tập dịch nghĩa
@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

if __name__ == '__main__':
    app.run(debug=True)
