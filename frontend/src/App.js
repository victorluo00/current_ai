import './App.css';
import { useState, useEffect } from 'react';
import PreferencesForm from './components/preferencesForm';

function App() {
  const [data, setData] = useState([]); // this is the data from the backend
  useEffect(() => {
    async function fetchData() {
      const response = await fetch('/load_data/');

      const data = await response.json();
      console.log('data', data);
      // Do something with the data, such as setting it to state
      setData(data);
    }
    fetchData();
  }, []);
  console.log('data', data);
  return (
    <div>
      <PreferencesForm data={data} />
    </div>
  );
}

export default App;
