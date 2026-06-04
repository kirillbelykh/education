import { useEffect, useState } from "react";

import Header from "./components/Header";
import NotesList from "./components/NotesList";

function App() {
  const [notes, setNotes] = useState([]);
  useEffect(() => {
    async function loadNotes() {
      const accessToken = localStorage.getItem("accessToken");
      if (!accessToken) {
        console.log("No access token");
        return;
      }

      const response = await fetch("http://127.0.0.1:8000/notes", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (!response.ok) {
        console.log("Failed to load notes");
        return;
      }

      const notesFromBackend = await response.json();

      setNotes(notesFromBackend);
    }
    loadNotes();
  }, []);

  return (
    <div>
      <Header />
      <NotesList notes={notes} />
    </div>
  );
}

export default App;