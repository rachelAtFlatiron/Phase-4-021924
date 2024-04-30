import { Link } from "react-router-dom";

function ProductionCard({ production }) {
	const { title, description, image, id } = production;
	
	return (
		<li className="card" style={{maxWidth: "300px"}} id={id}>
			<figure className="image">
				<img src={image} alt={title} />
			</figure>
			<section className="details">
				<Link to={`/productions/${id}`}>
					<h2>{title}</h2>
				</Link>
				<p>{description}</p>
			</section>
		</li>
	);
}

export default ProductionCard;
