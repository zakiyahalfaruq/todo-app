from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        tasks.append({'text': task_text, 'completed': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_index>', methods=['POST'])
def toggle_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = not tasks[task_index]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

