import ProductionCard from './ProductionCard'


function ProductionContainer({productions}) {

    return (
     <section>
         <ul className='cards'>
             {productions.map(production => <ProductionCard  key={production.id} production={production}  />)}
         </ul>
     </section>
    )
  }

  /*

  productions = [{movie: dune}, {movie: inception}]
  [<ProductionCard production={dune} />, <ProductionCard production={inception} />]
  */
  
export default ProductionContainer
