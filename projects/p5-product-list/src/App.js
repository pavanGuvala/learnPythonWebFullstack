import React from "react";
import ProductList from "./ProductList";

export default function App() {
  
    const products = [
        {
          name: "pure cotton 1 shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Levis",
          ratings:"4.5",
          likes:"343.9"
        },
        {
          name: "pure cotton 2 shirt",
          price:"449",
          discountprice:"249",
          discountPercentage:"45%",
          brand:"Jack and joes",
          ratings:"4.5",
          likes:"34.9"
        },
        {
          name: "pure cotton shirt",
          price:"449",
          discountprice:"249",
          discountPercentage:"45%",
          brand:"Roadstar",
          ratings:"4.5",
          likes:"33.9"
        },
        {
          name: "pure cotton 1 shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Levis",
          ratings:"4.5",
          likes:"343.9"
        },
        {
          name: "pure cotton 2 shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Jack and joes",
          ratings:"4.5",
          likes:"343.9"
        },
        {
          name: "pure cotton  shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Roadstar",
          ratings:"4.5",
          likes:"343.9"
        },
        {
          name: "pure cotton 1 shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Levis",
          ratings:"4.5",
          likes:"343.9"
        },
        {
          name: "pure cotton 2 shirt",
          price:"449",
          discountprice:"150",
          discountPercentage:"45%",
          brand:"Jack and joes",
          ratings:"4.5",
          likes:"34.9"
        }
    ];
  
    return(
        <div className="App">
          <ProductList productsData={products} />
        </div>
    );
    }
    
    

        
      