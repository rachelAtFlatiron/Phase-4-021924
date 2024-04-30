import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function ProductionDetail() {
	const [production, setProduction] = useState({
		roles: []
	});

	const params = useParams()
	const navigate = useNavigate()
	// 4a. fetch current production based on params
	// 4c. if response is not ok, navigate to /not-found
	useEffect(() => {
		fetch(`/productions/${params.id}`)
		.then(res => {
			if(res.ok){
				return res.json()
			} else {
				navigate('/not-found')
			}
		})
		.then(data => setProduction(data))
	}, [])


	// 4b. destructure the values and display them on page
	const { id, title, genre, image, description, director, length, composer } = production;
	
	return (
		<div className="project-detail" id={id}>
			<h1>{title}</h1>
			<p>{description}</p>

			<div className="project-card">
				<figure className="image">
					<img src={image} alt={title} />
					<section>
						<p>Genre: {genre}</p>
						<p>Director: {director}</p>
						<p>Composer: {composer}</p>
						<p>Length: {length}</p>
					</section>
				</figure>
				<section className="details">
					
					<h3 style={{ margin: "16px auto" }}>Cast: </h3>
					<ul className="crew">
						{production.roles.map((crew) => (
							<li>
								<img
									width={"100px"}
									src={crew.actor.image}
									alt={crew.actor.name}
								/>

								<div className="crew-member">
									<Link to={`/actors/${crew.actor.id}`}>
										<p style={{ "font-style": "italic" }}>{crew.actor.name}</p>
									</Link>
									<p>{crew.role_name}</p>
								</div>
							</li>
						))}
					</ul>
				</section>
			</div>
		</div>
	);
}

export default ProductionDetail;
