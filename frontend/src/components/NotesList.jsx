import NoteCard from "./NoteCard";


function NotesList({ notes }) {
  if (notes.length === 0) {
    return (
      <section>
        <h2>No notes yet</h2>
      </section>
    );
  }

  return (
    <section>
      {notes.map((note) => (
        <NoteCard key={note.id} note={note} />
      ))}
    </section>
  );
}

export default NotesList;