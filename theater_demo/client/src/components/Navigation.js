import { Link, NavLink, useNavigate } from "react-router-dom";




function Navigation({user, updateUser}) {
	const navigate = useNavigate();

	// ✅ 6a. write logout function that fetches `/logout`
	const handleLogout = () => {
		fetch('/logout')
		.then(res => res.json())
		.then(data => updateUser(null))
	}
			// ✅ 6b. if res.ok....
				// ✅ 6b. update the user to be no one....
				// ✅ 6c. navigate to the login page
				
	return (
		<header>
			<h1>
				<Link to={"/"}>{"//"} Not the Oscars</Link>
			</h1>

			<div className="menu">
				<NavLink className="button" to="/productions" end>
					All Productions
				</NavLink>
				<NavLink className="button" to="/actors" end>
					All Actors
				</NavLink>
				<NavLink className="button" to="/actors/new">
					New Actor
				</NavLink>
				<NavLink className="button" to="/productions/new">
					New Production
				</NavLink>
				<NavLink className="button" to="/auth">
					Log In
				</NavLink>
				{	// ✅ 11b. Conditionally render the logout button and a greeting 
					user ? (
						<>
						<button onClick={handleLogout} className="button">
							Log Out
						</button>
						<p style={{'margin-top': '8px'}}>Hello, {user.username}</p>
						</>
					) : ''
				}
					
			</div>
		</header>
	);
}

export default Navigation;
