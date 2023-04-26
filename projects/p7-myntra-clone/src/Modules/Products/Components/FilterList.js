import "../App.css";
import Category from "./Categories";
import Brand from './Brand';
import Price from "./Price";
import Color from "./Color";

function FilterList(){
  return <div className="FilterList">
    <Category></Category>
    <Brand></Brand>
    <Price></Price>
    <Color></Color>
  </div>
}

export default FilterList;