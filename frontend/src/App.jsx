import { useEffect, useState } from "react";
import parseUrl from "./util/url"
function App() {
  const [text, setText] = useState('');
  useEffect(
    () => {
      fetch(parseUrl('/api/demo/hello'))
        .then((res) => res.json())
        .then((data) => setText(data.message))
        .catch((err) => setText(err.message));
    }, []
  );
  return (
    <div>
      <p>{text}</p>
    </div>
  );
}

export default App;
