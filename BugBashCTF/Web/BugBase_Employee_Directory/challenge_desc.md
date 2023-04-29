We have made an employee directory for recognizing BugBase employees. Now you can look for employees working in different departments.

Hint: SQL Wildcard 


Solution 
-------------------------------

On opening the page we find we have , a drop down option to get a list of users based on the department 

On inspecting the response, we get a link to a supersecret page url 


@app.route('/getEmployee', methods=['POST'])
def get():
    dept = request.form["dept"]
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    res = cur.execute("select * from employees where Department LIKE ?", (dept.replace("%", ""),))
    data = "id &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Department<br>"
    for r in res:
        for i in r:
            data = data + str(i) + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
        data = data + "<br>"
    return render_template('index.html', data=data)
    
    if __name__ == '__main__':
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, Department TEXT)")
    cur.execute(f'''
        INSERT INTO employees VALUES
            (0, "Random Employee", "{open('flag.txt').read()}"),
            (1, "Tuhin Bose", "Security"),
            (2, "Devang Solanki", "Security"),
            (3, "Sivadath K S", "Security"),
            (4, "Siddharth Johri", "Security"),
            (5, "Harshit Kataria", "Marketing"),
            (6, "Diya Patel", "Marketing"),
            (7, "Anushikha Mehta", "Sales"),
            (8, "Prachi Singh", "Sales"),
            (9, "Femin Justin", "Dev"),
            (10, "P Aditya Mohan", "Dev")
    ''')
    
    
The database was working on sqllite3 
and the query was using LIKE 

We learnt for LIKE  % was used to represent range of characters and _ for a single character. However, the code was designed to remove any % we entered 

So we focused on _ option 

When we entered 3 ___ we got Dev 
and if we entered 5 _____ we got Sales 

So, we would need to assume correct number of _ for the flag 

We started intruder and used character block to create _ from 1 to 20 .............no result

then we did 1 to 40 , at 37 we got the flag.
