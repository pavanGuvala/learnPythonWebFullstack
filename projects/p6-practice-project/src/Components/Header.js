import react from "react";
import "../App.css";

function Header(){
  return <Header className='Header-Section'>
    <nav>
        <ul>
            <li>MEN</li>
            <li>WOMEN</li>
            <li>KIDS</li>
            <li>HOME & LIVING</li>
            <li>BEAUTY</li>
            <li>STUDIO</li>
        </ul>
        
        <input className="Search-button" placeholder="Search for products, brands and more"/>
        <div className="Cart-section">
            <div className="Profile-icon">PROFILE</div>
            <div color="Cart-bag">Cart</div>
        </div>
    </nav>
  </Header>
}

export default Header;