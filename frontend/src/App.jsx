import { useEffect, useState } from "react";
import {useCookies} from 'react-cookie'
function App() {
  const [text, setText] = useState('');
  const [cookies, setCookie, removeCookie] = useCookies(['session'])
  useEffect(
    () => {
      fetch('/api/demo/hello', {
        headers: {
          Authorization: `Bearer ${cookies.session}`
        }
      })
        .then((res) => res.json())
        .then((data) => setText(data.message))
        .catch((err) => setText(err.message));
    }, [cookies.session]
  );
  return (
    <div>
      <p>{text}</p>
    </div>
  );
}

export default App;
