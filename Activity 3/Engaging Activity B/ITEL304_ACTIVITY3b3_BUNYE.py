from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	name = "HANNAH RAE PARUNGAO BUNYE"
	email = "hannahrae.bunye@lspu.edu.ph"
	contact = '09989591497'
	return """<html>
	<body style="background-color: #000000; padding-left: 25px; padding-right: 25px; padding-top: 10px; padding-bottom: 20px; text-align: center; color: white; font-size: 20px;">
		<div style="">
			<h1>{0}</h1>
				<p>BSIT Student</p>
				<a href="mailto:hannahrae.bunye@lspu.edu.ph" style="color:#A4E2F5; text-decoration: none;">{1}</a>
				<br><br>
				<a href="tel:09989591497" style="color:#A4E2F5; text-decoration: none;">{2}</a>
		</div>
		<div>
			<h2 class="h2">Profile</h2>
				<p>My name is Hannah Rae Parungao Bunye and I’m 20 years old. My birthday is December 12, 2001 at Sta. Cruz, Laguna. 
				I live in Paete, Laguna. My parents are Ana P. Bunye and Renato G. Bunye. I have two siblings,
				my older sister and  my little sister. Their names are Rae Anne P. Bunye and Riana P. Bunye. I graduated elementary in
				Paete Elementary School and for junior and senior high school is in
				Paete Science and Business College Inc. I’m currently taking a Bachelor of Science in Information Technology course.</p>
		</div>

		<div>
			<h2 class="h2">Education</h2>
        			 <h3 class="h3">Elementary</h3>
					  <p>Paete Elementary School</p>
					  <p>2008 - 2014</p>
         			<h3 class="h3">Junior High School</h3>
					  <p>Paete Science and Business College Inc.</p>
					  <p>2014 - 2018</p>
         			<h3 class="h3">Senior High School</h3>
					  <p>Paete Science and Business College Inc.</p>
					  <p>2018 - 2020</p>
				 <h3 class="h3">College</h3>
					  <a href="https://lspu.edu.ph/" target="_blank" style="color:#A4E2F5; text-decoration: none;">Laguna State Polytechnic University</a>
					  <p>2020 and so on</p>
		</div>
	</body>
	</html>
		""".format(str(name), str(email), str(contact))

app.run(host="localhost", debug=True)
