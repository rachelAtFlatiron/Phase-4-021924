import { Link, NavLink, useNavigate } from "react-router-dom";


function Navigation({}) {
	const navigate = useNavigate();

	// ✅ 6a. write logout function that fetches `/logout`
	
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
				}
					
			</div>
		</header>
	);
}

export default Navigation;
