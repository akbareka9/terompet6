from flask import Flask, render_template

app = Flask(__name__)  # Corrected here

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')  

# Ini akan menampilkan halaman HTML

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)