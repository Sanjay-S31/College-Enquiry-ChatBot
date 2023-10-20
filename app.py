from flask import Flask, render_template, request, session, url_for, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import mysql.connector
import time

app = Flask(__name__)
app.secret_key = 'Secret Key'

#database connectivity
conn=mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='register')
cur=conn.cursor()

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(english_bot)

conversation = [
"Hi",
"Helloo!",
"Hey",
"Hello",
"Heyyy",

"How are you",
"How are you doing",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Good",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Fine",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about REC college.",

"What else can you do?",
"I can help you know more about REC",
    
    "Student",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
    "Curricular",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Moodle <br> 1.1.2 Academic Calendar <br> 1.1.3 Syllabus </b>",
    "Moodle",
    "<b> 1.1.1 Moodle <br>The link to Moodle 👉 <a href=" 'https://www.rajalakshmicolleges.net/moodle/login/index.php' ">Click Here</a> </b>",
    "Calender",
    "<b > 1.1.2 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://www.rajalakshmi.org/academic-calendar.php' ">Click Here</a> </b>",
    "Syllabus",
    "<b> 1.1.3 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://www.rajalakshmi.org/academics.php' ">Click Here</a> </b>",

    "Extra curricular",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Student Chapters <br> 1.2.3 Student's Council</b>",
    "Events",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://www.rajalakshmi.org/alumni/events' ">Click Here</a></b>",
    "Student chapters",
    "<b > 1.2.2 Student Chapters<br>The link to Student Chapters👉<a href=" 'https://www.rajalakshmi.org/studentlife-student-services.php' ">Click Here</a> </b>",
    "Students council",
    "<b > 1.2.3 Student's Council <br>The link to Student's Council👉 <a href=" 'https://www.rajalakshmi.org/studentlife-prizes.php' ">Click Here</a> </b>",

    "Administrative",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Portal<br> 1.3.2 Notices </b>",
    "Students portal",
    "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'http://rajalakshmi.in/UI/Modules/Login/UniLogin.aspx?' ">Click Here</a> </b>",
    "Notices",
    "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" 'https://www.rajalakshmi.org/alumni/notices' ">Click Here</a> </b>",

    "Exam",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Notices<br> 1.4.2 Examination Process <br> 1.4.3 Question Paper Archive </b>",
    "Exam notices",
    "<b > 1.4.1 Notices<br>The link to Notices👉 <a href=" 'https://www.rajalakshmi.org/coe.php' ">Click Here</a> </b>",
    "Examination process",
    "<b > 1.4.2 Examination Process<br>The link to Examination Process👉<a href=" 'https://www.rajalakshmi.org/coe.php' ">Click Here</a> </b>",
    "Question paper archive",
    "<b > 1.4.3 Question Paper Archive<br>The link to Archives👉 <a href=" 'https://www.rajalakshmi.org/coe.php' ">Click Here</a> </b>",

    "Placements",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Statistics </b>",
    "Placement details",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'https://www.rajalakshmi.org/placement.php' ">Click Here</a> </b>",
    "Recruiters",
    "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://www.rajalakshmi.org/placement-recruiters.php' ">Click Here</a> </b>",
    "Placement statistics",
    "<b > 1.5.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.rajalakshmi.org/placement-report.php' ">Click Here</a> </b>",

    "Faculty",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Change Personal Details<br>2.3  Examination </b>",
    
    "Portals and administration",
    "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 Biometric Attendance System <br>2.1.2 Moodle </b>",
    "Biometric attendance",
    "<b> 2.1.1 Biometric Attendance<br>The link to Biometric Attendance👉<a href=" 'http://rajalakshmi.in/UI/Modules/Login/UniLogin.aspx?' ">Click Here</a> </b>",
    "Faculty moodle",
    "<b> 2.1.2 Moodle<br>The link to Moodle👉<a href=" 'https://www.rajalakshmicolleges.net/moodle/login/index.php' ">Click Here</a> </b>",

    "Change personal details",
    "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
    "Site login",
    "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'https://www.rajalakshmi.org/alumni/login' ">Click Here</a> </b>",
   
    "Examination",
    "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 Notices<br> 2.3.2 Question Paper Archive </b>",
    "Examination notices",
    "<b> 2.3.1 Notices <br>The link to Notices 👉 <a href=" 'https://www.rajalakshmi.org/coe.php' ">Click Here</a> </b>",
    "Faculty question paper archive",
    "<b> 2.3.2 Question Paper Archive <br>The link to Archive👉<a href=" 'https://www.rajalakshmi.org/coe.php' ">Click Here</a> </b>",
  
    "Parents",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    "About us",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About REC<br> 3.1.2 Director's Address <br> 3.1.3 Principal's Address </b>",
    "About rec",
    "<b > 3.1.1 About REC<br>The link to About REC👉 <a href=" 'https://www.rajalakshmi.org/profile-college.php' ">Click Here</a> </b>",
    "Director address",
    "<b > 3.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://www.rajalakshmi.org/profile-message.php' ">Click Here</a> </b>",
    "Principal address",
    "<b > 3.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://www.rajalakshmi.org/profile-principal.php' ">Click Here</a> </b>",

    "Parents notices",
    "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    "All notices",
    "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'https://www.rajalakshmi.org/alumni/notices' ">Click Here</a> </b>",

    "About",
    "<b > ABOUT US<br>These are the top results:<br> <br>3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
    "Payment details",
    "<b > 3.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'https://www.rajalakshmi.org/onlinefeepayment.php' ">Click Here</a> </b>",
    "Payment portal",
    "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://payments.billdesk.com/bdcollect/pay?p1=518&p2=14' ">Click Here</a> </b>",

    "Parent placements",
    "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    "Parent placement details",
    "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'https://www.rajalakshmi.org/placement.php' ">Click Here</a> </b>",
    "Parent recruiters",
    "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://www.rajalakshmi.org/placement-recruiters.php' ">Click Here</a> </b>",
    "Parent placement statistics",
    "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.rajalakshmi.org/placement-report.php' ">Click Here</a> </b>",

    "Visitor",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
    "Visitor about us",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About REC<br> 4.1.2 Director's Address <br> 4.1.3 Principal's Address </b>",
    "Visitor about rec",
    "<b > 4.1.1 About REC<br>The link to About REC👉 <a href=" 'https://www.rajalakshmi.org/profile-college.php' ">Click Here</a> </b>",
    "Visitor director address",
    "<b > 4.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'https://www.rajalakshmi.org/profile-message.php' ">Click Here</a> </b>",
    "Visitor principal address",
    "<b > 4.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://www.rajalakshmi.org/profile-principal.php' ">Click Here</a> </b>",

    "Programs",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
    "Ug",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://www.rajalakshmi.org/admission-courses.php' ">Click Here</a> </b>",
    "Pg",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://www.rajalakshmi.org/admission-courses.php' ">Click Here</a> </b>",
    "Phd",
    "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href=" 'https://www.rajalakshmi.org/admission-courses.php' ">Click Here</a> </b>",

    "Student bodies",
    "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Students Council  <br> 4.3.2 Students Chapter <br> 4.3.3 Students Project Groups </b>",
    "Visitor student council",
    "<b > 4.3.1 Students Council  <br>The link to Students Council  👉 <a href=" 'https://www.rajalakshmi.org/studentlife-student-services.php' ">Click Here</a> </b>",
    "Visitor student chapter",
    "<b > 4.3.2 Students Chapter <br>The link to Students Chapter 👉<a href=" 'https://www.rajalakshmi.org/studentlife-student-services.php' ">Click Here</a> </b>",
    "Project",
    "<b > 4.3.3 Students Project Groups <br>The link to Students Project Groups👉 <a href=" 'https://www.rajalakshmi.org/iiic-7.php' ">Click Here</a> </b>",

    "Visitor extra curricular",
    "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Events  <br> 4.4.2 Institute Innovation Cell </b>",
    "Visitor events",
    "<b > 4.4.1 Events    <br>The link to Events   👉 <a href=" 'https://www.rajalakshmi.org/alumni/events' ">Click Here</a> </b>",
    "Innovation cell",
    "<b > 4.4.2 Institute Innovation Cell <br>The link to Institute Innovation Cell 👉<a href=" 'https://www.rajalakshmi.org/studentlife-iiic.php' ">Click Here</a> </b>",

]


trainer.train(conversation)

@app.route('/')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register',methods=['POST','GET'])
def register_submit():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(username,email,password))
        conn.commit()
        cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
        myuser=cur.fetchall()
        session['id']=myuser[0][0]
        time.sleep(1.5)
        return redirect('/home')

@app.route('/login',methods=['POST','GET'])
def login_submit():
    email=request.form.get('email')
    password=request.form.get('password')
    sqlstmt="SELECT * FROM `users` where email='{}' and password='{}'".format(email,password)
    cur.execute(sqlstmt)
    users=cur.fetchall()
    k=len(users)
    if(k==1):
        session['id']=users[0][0]
        time.sleep(1.5)
        return redirect('/home')
    time.sleep(1.5)
    return redirect('/login')


@app.route('/home')
def home():
    if 'id' in session:
        return render_template('home.html')
    else:
        return redirect('/login ')

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    op=user_text.capitalize()
    try:
        if op in conversation:
            bot_response = str(english_bot.get_response(op))
        else:
            bot_response = "I'm sorry, I don't understand. Can you please try again?"
    except:
        bot_response = "I'm sorry, I don't understand. Can you please try again?"
    return bot_response



@app.route('/suggestion',methods=['POST','GET'])
def suggestion():
    email=request.form.get('email')
    sugg=request.form.get('suggestion')
    cur.execute("""INSERT INTO  suggestion(email,message) VALUES('{}','{}')""".format(email,sugg))
    conn.commit()
    return redirect("/home")


@app.route('/logout')
def logout():
    session.pop('id')
    time.sleep(1.5)
    return redirect('/login')


if __name__ == "__main__":
    # app.secret_key=""
    app.run(debug=True)