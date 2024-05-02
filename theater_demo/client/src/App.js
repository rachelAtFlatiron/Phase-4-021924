import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Home from "./components/Home";
import Navigation from "./components/Navigation";
import NotFound from "./components/NotFound";
import ActorForm from "./components/actor/ActorForm";
import ActorContainer from "./components/actor/ActorContainer";
import ActorDetail from "./components/actor/ActorDetail";
import ProductionContainer from "./components/production/ProductionContainer";
import ProductionForm from "./components/production/ProductionForm";
import ProductionDetail from "./components/production/ProductionDetail";
import Auth from "./components/Auth";

/*
- Signup
1. make POST route in app.py
2. make state in React
3. fetch POST route in React
4. update state in React on success

- Logout
1. make /logout route in app.py
2. fetch /logout in React
3. update state in React
4. use conditional rendering to check if user exists in React and to show appropriate information
*/
function App() {
	const [productions, setProductions] = useState([]);
	const [actors, setActors] = useState([]);
	const [user, setUser] = useState(null);
	// ✅ 4. Pass the new user to App.js
	// ✅ 4a. create user state and update user function

	useEffect(() => {
		fetch("/productions")
			.then((res) => res.json())
			.then(setProductions);
		fetch("/actors")
			.then((res) => res.json())
			.then(setActors);
		// ✅ 9a. fetch GETs `/authenticate-session` in `useEffect`
		// ✅ 9b. if res.ok update user with the response
		fetch("/authenticate-session")
		.then(res => {
			//if i got a 200
			if(res.ok){
				return res.json()
			} else { //if i got a 401
				console.log('user not found')
			}
		})
		.then(data => setUser(data))
	}, []);

	// ✅ 4a. update user function
	const updateUser = (user) => {
		setUser(user);
	};

	const addProduction = (production) =>
		setProductions((current) => [...current, production]);

	// ✅ 7a. if no user, return essential JSX
	// ✅ 11. Show user greeting in `Navigation.js`
	// ✅ 11a. pass down user as props
	// ✅ 11b. Conditionally render the logout button and a greeting
	if (!user) {
		return (
			<div className="App light">
				<Navigation updateUser={updateUser} user={user} />
				<Auth updateUser={updateUser} />
			</div>
		);
	} else {
		return (
			<div className="App light">
				<Navigation user={user} updateUser={updateUser} />
				<Routes>
					<Route path="/auth" element={<Auth updateUser={updateUser} />} />

					<Route path="/actors/new" element={<ActorForm />} />

					<Route
						path="/productions/new"
						element={<ProductionForm addProduction={addProduction} />}
					/>

					<Route path="/productions/:id" element={<ProductionDetail />} />

					<Route
						path="/productions"
						element={<ProductionContainer productions={productions} />}
					/>

					<Route path="/actors/:id" element={<ActorDetail />} />

					<Route path="/actors" element={<ActorContainer actors={actors} />} />

					<Route path="/not-found" element={<NotFound />} />

					<Route exact path="/" element={<Home />} />
				</Routes>
			</div>
		);
	}
}

export default App;
