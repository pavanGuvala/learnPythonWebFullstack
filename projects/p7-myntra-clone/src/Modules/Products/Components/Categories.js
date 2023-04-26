import "../App.css";
function Categories(){
  return <div className="Categories">
    <h5>CATEGORIES</h5>
    <div>
        <div>
            <input htmlFor="tShirts" type="checkbox"/>
            <label id="tShirts">T Shirts</label>   
        </div>
        <div>
            <input htmlFor="longuetShirts "type="checkbox"/>
            <label id="lonnguetShirts">longue T Shirts</label>
        </div>
    </div>
  </div>
}
export default Categories;