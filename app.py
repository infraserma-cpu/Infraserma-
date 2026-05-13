from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # هاد البيانات ممكن من بعد نزيدو قاعدة بيانات (SQLite) باش تحفظهم
    workers_data = [
        {'name': 'عزالدين بوعنان', 'rate': 120, 'days': 1, 'advance': 20},
        {'name': 'محمد', 'rate': 100, 'days': 5, 'advance': 300}
    ]
    
    total_to_pay = 0
    for worker in workers_data:
        # الحساب التلقائي للباقي
        worker['balance'] = (worker['rate'] * worker['days']) - worker['advance']
        total_to_pay += worker['balance']
        
    return render_template('pointing.html', workers=workers_data, total=total_to_pay)

if __name__ == "__main__":
    app.run(debug=True)
