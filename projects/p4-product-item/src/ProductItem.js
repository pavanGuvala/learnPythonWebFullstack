import React from "react";

function productItem(props)  {

    const{ name, brand, discountprice, discountpercentage} = props.data;
    return(
        <div>
            <p>{name}</p>
            <p>{brand}</p>
            <p>{discountpercentage}</p>
            <p>{discountprice}</p>
        </div>
    );
}

export default productItem;