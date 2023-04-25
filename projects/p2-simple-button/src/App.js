import logo from './logo.svg';
import './App.css';

function App() {

  const handleClick = () => {
    alert('Clicked on Button ')
  };

  return (
    <div className="App">

      <button onClick={handleClick}>
        click me
      </button>
       
    </div>
  );
}

export default App;
