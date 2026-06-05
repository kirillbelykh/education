import { useEffect, useState } from "react";

import Header from "./components/Header";
import NotesList from "./components/NotesList";
import LoginForm from "./components/LoginForm";

function App() {
  const [notes, setNotes] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [accessToken, setAccessToken] = useState(
    localStorage.getItem("accessToken")
  );

  useEffect(() => {
    async function loadNotes() {
      if (!accessToken) {
        console.log("No access token");
        return;
      }

      setIsLoading(true);
      setError("");

      const response = await fetch("http://127.0.0.1:8000/notes", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        console.log("Failed to load notes");
        setError("Failed to load notes");
        setIsLoading(false);

        if (response.status === 401) {
          localStorage.removeItem("accessToken");
          setAccessToken(null);
          setNotes([]);
        }

        return;
      }

      const notesFromBackend = await response.json();

      setNotes(notesFromBackend);
      setIsLoading(false);
    }
    loadNotes();
  }, [accessToken]);

  function handleLogin(token) {
    setAccessToken(token);
  }

  function handleLogout() {
    localStorage.removeItem("accessToken");
    setAccessToken(null);
    setNotes([]);
    setError("");
    setIsLoading(false);
  }

  return (
    <div>
      <Header onLogout={handleLogout} />
      {accessToken ? (
        <>
          {isLoading && <p>Loading notes...</p>}
          {error && <p>{error}</p>}
          {!isLoading && <NotesList notes={notes} />}
        </>
      ) : (
        <LoginForm onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;