import ProductItem from "./ProductItem";

function ProductList(props){
    
    console.log(' props', props);

    const {productsData} = props;
    
    return(
        <div className="productList">
            {
                productsData.map((item) => {
                    return <ProductItem data={item} />;
                })
            }
        </div>
    );

}

 export default ProductList;