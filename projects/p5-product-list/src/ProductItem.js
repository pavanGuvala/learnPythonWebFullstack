import React from "react";

function ProductItem(props){
    const {
        name,
        price,
        discountprice,
        discountpercentage,
        brand,
        likes,
        ratings,
    } = props.data;

    console.log(props)
    
    return(
        <div className="productItemBox">
            <div className="productphoto">
                <div className="productDetails">
                    <p>{brand}</p>
                    <p>{name}</p>
                    <div className="Feedback">
                        <span>{ratings}</span>
                        <span>{likes}</span>
                    </div>  
                    <div className="priceDetails">
                        <span>{discountprice}</span>
                        <span className="Actualprice"></span>
                        <span >{discountpercentage}</span>     
                    </div>
                </div>
            </div>
        </div>
    );
}
    
export default ProductItem;