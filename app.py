from flask import Flask,render_template,request,session,flash
from db import connect
from flask_mail import Mail,Message

app=Flask(__name__)
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME='#',
	MAIL_PASSWORD='#'
	)
mail=Mail(app)

@app.route('/',methods=['POST','GET'])
def index():
	if request.method=='POST':
		fname=request.form.get("firstname",False)
		lname=request.form.get("lastname",False)
		emailid=request.form.get("email",False)
		uname=request.form.get("username",False)
		pwd=request.form.get("password",False)
		cpwd=request.form.get("confirm-password",False)
		a,b=connect()
		check=b.execute("select * from userinformation where email='%s' or username='%s'"%(emailid,uname))
		if check==0:
			b.execute("insert into userinformation(firstname,lastname,email,username,password,confirmpassword) values(%s,%s,%s,%s,%s,%s)",(fname,lname
				,emailid,uname,pwd,cpwd))
			b.execute("insert into users(username,email) values(%s,%s)",(uname,emailid))
			a.commit()
			a.close()
			b.close()
			msg=Message("Welcome Mail",sender="#",recipients=[emailid])
			msg.body="Dear "+uname+" ,Welcome to our app"
			mail.send(msg)
			
			
		else:
			flash('Username or Email already exisits..Try using another one')
	return render_template('index.html')

if __name__=='__main__':
	app.secret_key = 'super secret key '
	app.run(debug=True)