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

function App() {
	const [productions, setProductions] = useState([]);
	const [actors, setActors] = useState([]);

	// 3a. create a useEffect to fetch from /productions and /actors
	useEffect(() => {
		fetch('/productions')
		.then(res => {
			if(res.ok){
				return res.json()
			} else {
				console.log('productiosn not found')
			}
		})
		.then(data => setProductions(data))
	}, [])

	useEffect(() => {
		fetch('/actors')
		.then(res => {
			if(res.ok){
				return res.json()
			} else {
				console.log('actors not found')
			}
		})
		.then(data => setActors(data))
	}, [])
	// 3b. save the result in state

	const addProduction = (newProduction) => {
		setProductions([...productions, newProduction])
	}
	return (
		<div className="App light">
			<Navigation />
			<Routes>
				<Route path="/actors/new" element={<ActorForm />} />

				<Route path="/productions/new" element={<ProductionForm addProduction={addProduction} />}
				/>
				<Route path="/productions/:id" element={<ProductionDetail />} />

				{/* 3c. pass productions here down  */}
				<Route path="/productions" element={<ProductionContainer productions={productions} />} />

				<Route path="/actors/:id" element={<ActorDetail />} />

				{/* 3c. pass actors here down  */}
				<Route path="/actors" element={<ActorContainer actors={actors} />} />
				<Route path="/not-found" element={<NotFound />} />

				<Route exact path="/" element={<Home />} />
			</Routes>
		</div>
	);
}

export default App;
