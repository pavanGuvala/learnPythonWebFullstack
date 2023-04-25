
import './App.css';

let numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];

let products = [

  {name: "Shirt", price:200},
  {name: "TShirt", price:300},
  {name: "Pant", price:250},
  {name: "Shirt3", price:500},
  {name: "Shirt4", price:600},
  {name: "Shirt5", price:700},

];

function ProductList(){
  return <div className="ProductList">
    {
      products.map(function(item){
        return <ProductItem data={item}></ProductItem>
      })
    }
    

  </div>
}

function ProductItem(props){
  const {name,price} = props.data;
  return <div>
    <p>{name}</p>
     <p>{price}</p>
  </div>
}


function App() {
  return (
    <div className="App">
      <ProductList></ProductList>
    </div>
  );
}

export default App;
