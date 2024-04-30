import { redirect } from "react-router-dom";
// 5a. Import useFormik and yup
import { useFormik } from "formik";
import * as yup from "yup";

//controlled forms
//1. values (formik.values)
//2. handlechange (formik.handleChange)
//3. setting form state (useFormik)
function ProductionForm({ addProduction }) {

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
	const schema = yup.object().shape({
		title: yup.string().required("title is required"),
		genre: yup.string(),
		length: yup.number().positive("length must be greater than 0"),
		year: yup.number().min(1850, "movies were only made after 1850"),
		image: yup.string().required("image is required"),
		language: yup.string(),
		director: yup.string(),
		description: yup.string().max(250, "too long"),
		composer: yup.string()
	})


	const formik = useFormik({
		initialValues: {
			title: '',
			genre: '',
			length: 0,
			year: 0,
			image: '',
			language: '',
			director: '',
			composer: ''
		},
		validationSchema: schema,
		onSubmit: (values) => {
			fetch('/productions', {
				method: 'POST',
				headers: {
					'content-type': 'application/json'
				},
				body: JSON.stringify(values)
			})
			.then(res => {
				if(res.ok){
					
					return res.json()
				} else {
					console.log('oops')
				}
			})
			.then(data => {
				addProduction(data)
			})
		}
	})

	return (
		<section>
			{/* 6a. attach formik submit handler to form */}
			<form className="form" onSubmit={formik.handleSubmit}>
				<label>Title </label>
				<input
					type="text"
					name="title"
					// 6b. attach formik change handler to inputs 
					value={formik.values.title}
					onChange={formik.handleChange}
					// 6c. pass in formik values to make form controlled

				/>

				{
					formik.touched.title && formik.errors.title ? <h3>{formik.errors.title}</h3> : ''
				}
				
				<label> Genre</label>
				<input
					type="text"
					name="genre"
					value={formik.values.genre}
					onChange={formik.handleChange}
					
				/>

				<label>Length</label>
				<input
					type="number"
					name="length"
					value={formik.values.length}
					onChange={formik.handleChange}
					onBlur={formik.handleBlur}
				/>
				{
					formik.touched.length && formik.errors.length ? <h3>{formik.errors.length}</h3> : ''
				}

				<label>Year</label>
				<input
					type="number"
					name="year"
					value={formik.values.year}
					onChange={formik.handleChange}
				/>
				{
					formik.errors.year ? <h3>{formik.errors.year}</h3> : ''
				}
				<label>Image</label>
				<input
					type="text"
					name="image"
					value={formik.values.image}
					onChange={formik.handleChange}
				/>
				{
					formik.errors.image ? <h3>{formik.errors.image}</h3> : ''
				}
				<label>Language</label>
				<input
					type="text"
					name="language"
					value={formik.values.language}
					onChange={formik.handleChange}
				/>

				<label>Director</label>
				<input
					type="text"
					name="director"
					value={formik.values.director}
					onChange={formik.handleChange}
				/>

				<label>Description</label>
				<textarea
					type="text"
					rows="4"
					cols="50"
					name="description"
					value={formik.values.description}
					onChange={formik.handleChange}
				/>
				{
					formik.errors.description ? <h3>{formik.errors.description}</h3> : ''
				}
				
				<label>Composer</label>
				<input
					type="text"
					name="composer"
					value={formik.values.composer}
					onChange={formik.handleChange}
				/>

				<input className="button" type="submit" />
			</form>
		</section>
	);
}

export default ProductionForm;
