import ProductItem from './ProductItem';

const productItemData = {
  name: "T shirt",
  brand: "Roadstar",
  price: 340,
  discountprice: 300,
  discountpercentage:"40%"
};

function App() {
  return (
    <div className="App">
      <ProductItem data={productItemData}/>
    </div>
  );
}

export default App;
