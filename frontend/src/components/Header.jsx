

function Header({ onLogout }) {
    return (
        <header>
            <h1>Education Notes</h1>
            <button type="button" onClick={onLogout}>
                Logout
            </button>
        </header>
    );
}

export default Header;