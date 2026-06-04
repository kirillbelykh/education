

function NoteCard({ note }) {
    return (
        <article>
            <h2>{note.title}</h2>
            <p>{note.content}</p>
        </article>
    );
}

export default NoteCard;