import React from "react";
import BredCrum from "./BredCrum";
import ProductFilterList from "./ProductFilterList";

function ProductsHome(){
  return <div className='ProductsHome'>
    <BredCrum></BredCrum>
    <ProductFilterList></ProductFilterList>
  </div>
}

export default ProductsHome;
