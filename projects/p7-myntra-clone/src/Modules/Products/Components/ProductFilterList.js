import FilterList from "./FilterList";
import ProductList from "./ProductList";
import "../App.css";
function ProductFilterList(){
  return <div className="ProductFilterList">
    <FilterList></FilterList>
    <ProductList></ProductList>
  </div>
}

export default ProductFilterList;