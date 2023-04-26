import logo from './logo.svg';
import './App.css';

import Products from './Modules/Products/Container/Products';
import ProductDetails from './Modules/ProductDetails/ProductDetails';
import Orders from './Modules/Orders/Orders';
import Cart from './Modules/Cart/Cart';

import { Outlet, useRoutes } from 'react-router-dom';

 function App (){


  const routers = useRoutes([
    {
      path:"/",
      element: <Products />
    },
    {
      path:"product-details",
      element: <ProductDetails />
    },
    {
      path:"/cart",
      element: <Cart />
    },
    {
      path:"/orders",
      element: <Orders />
    }
  ]);
  return routers;
 }
 const AppRoot =() =>{
  return <div className='App'>
    {Outlet}
  </div>
 }

export default App;
