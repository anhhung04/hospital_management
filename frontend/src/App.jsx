import { useEffect, useState } from "react";

function App() {
  const [text, setText] = useState('');
  useEffect(
    () => {
      fetch('/api/demo/hello')
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
