import { useNavigate } from 'react-router-dom'
import { useState } from "react";
import { useFormik } from 'formik'
import * as yup from 'yup'

function Auth({ updateUser }) {
	const [signup, setSignup] = useState(true);
    const navigate = useNavigate()
	const toggleSignup = () => setSignup((prev) => !prev);
	console.log(signup)
    // ✅ 3. Create a form for the user to signup
	const schema = yup.object().shape({
		name: yup.string(),
		username: yup.string().required("enter a username")
	})
    // ✅ 3a. create a validations schema using yup
    // ✅ 4c. pass result to updateUser to set state
    // ✅ 4d. redirect to homepage if login is successful
	const formik = useFormik({
		initialValues: {
			username: '',
			name: ''
		},
		validationSchema: schema,
		onSubmit: (values) => {
			fetch(signup ? '/users' : '/login' , {
				method: 'POST',
				headers: {'content-type': 'application/json'},
				body: JSON.stringify(values)
			})
			.then(res => {
				if(res.ok){
					return res.json()
				} else {
					console.log('error')
				}
			})
			.then(data => {
				//update user state in react
				updateUser(data)
			})
		}
	})

    
	return (
		<section>
			{signup ? (
				<form className="form" onSubmit={formik.handleSubmit}>
					<label>Name</label>
					<input type="text" name='name' value={formik.values.name} onChange={formik.handleChange} />
					<label>Username</label>
					<input type="text" name='username' value={formik.values.username} onChange={formik.handleChange}  />
					<input type="submit" value="Sign Up" className="button" />
				</form>
			) : (
				<form className="form" onSubmit={formik.handleSubmit}>
					<label>Username</label>
					<input type="text" name='username' value={formik.values.username} onChange={formik.handleChange}  />
					<input type="submit" value="Log In" className="button" />
				</form>
			)}
			<section>
				<p>{signup ? "Already have an account?" : "Not a member?"}</p>
				<button className="button" onClick={toggleSignup}>
					{signup ? "Login" : "Sign Up"}
				</button>
			</section>
		</section>
	);
}

export default Auth;
