import { redirect } from "react-router-dom";
// 5a. Import useFormik and yup
import { useFormik } from "formik";
import * as yup from "yup";

function ProductionForm() {

	// 5b. create yup schema where:
	// title: required
	// length: must be positive
	// year is a minimum of 1850
	// image: required
	// description: max length is 250
	// 5c. create formik with...
	// 5c. ...initial values of form...

	// 5c...yup schema for validation....
	// 5c. submit callback


	return (
		<section>
			{/* 6a. attach formik submit handler to form */}
			<form className="form">
				<label>Title </label>
				<input
					type="text"
					name="title"
					// 6b. attach formik change handler to inputs 
					// 6c. pass in formik values to make form controlled
					// 7a. add onBlur event to allow formik to update "formik.touched"
				/>
				{/* 7b. use formik.touched and formik.errors to render errors where needed */}
				

				<label> Genre</label>
				<input
					type="text"
					name="genre"
					
				/>

				<label>Length</label>
				<input
					type="number"
					name="length"
					
				/>
				

				<label>Year</label>
				<input
					type="number"
					name="year"
					
				/>
				
				<label>Image</label>
				<input
					type="text"
					name="image"
					
				/>
				
				<label>Language</label>
				<input
					type="text"
					name="language"
					
				/>

				<label>Director</label>
				<input
					type="text"
					name="director"
					
				/>

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					
				/>
				
				<label>Composer</label>
				<input
					type="text"
					name="composer"
					
				/>

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
